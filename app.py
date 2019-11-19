from flask_socketio import SocketIO
from flask import Flask, render_template
from time import sleep
from threading import Thread, Event
from stellar_base.address import Address

app = Flask(__name__)

app.config['DEBUG'] = False

# turn the flask app into a socketio app
socketio = SocketIO(app)

# create Thread
thread = Thread()
thread_stop_event = Event()

class getAddressDetailsThread(Thread):

    def __init__(self):
        self.delay = 5
        super(getAddressDetailsThread, self).__init__()

    def getAddressDetails(self):

        while not thread_stop_event.isSet():

            publickey = 'GBCCC62LUXPDL7DLNQPYJWASA672CCJOLCJRBSIFXNIPRMQRRQ2HCWW6'
            target = 1000
            address = Address(address=publickey)  # testnet
            # address = Address(address=publickey, network='public')  # livenet
            address.get()  # Get the latest information from Horizon

            last_payment = address.payments(order='desc', limit=1)

            if 'transaction_successful' in last_payment['_embedded']['records'][0]:
                success = bool(last_payment['_embedded']['records'][0]['transaction_successful'])
            else:
                success = False

            if 'amount' in last_payment['_embedded']['records'][0] and success:
                amount = int(float(last_payment['_embedded']['records'][0]['amount']))
            else:
                amount = ''

            if 'asset_code' in last_payment['_embedded']['records'][0] and success:
                asset_code = last_payment['_embedded']['records'][0]['asset_code']
            elif 'asset_code' not in last_payment['_embedded']['records'][0] and success:
                asset_code = 'XLM'
            else:
                asset_code = ''

            balance = address.balances
            if 'balance' in balance[-1] and success:
                balance = int(float(balance[-1]['balance']))
            else:
                balance = ''

            last_transaction = address.transactions(order='desc', limit=1)
            if 'memo' in last_transaction['_embedded']['records'][0] and success:
                memo = last_transaction['_embedded']['records'][0]['memo']
            else:
                memo = ''

            socketio.emit('address_details', {'publickey': publickey, 'target': target, 'balance': balance, 'memo': memo, 'amount': amount, 'asset_code': asset_code}, namespace='/test')
            sleep(self.delay)

    def run(self):
        self.getAddressDetails()


@app.route('/')
def index():
    # only by sending this page first will the client be connected to the socketio instance
    return render_template('index.html')


@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    global thread
    print('Client connected')

    # Start the random number generator thread only if the thread has not been started before.
    if not thread.isAlive():
        print("Starting Thread")
        thread = getAddressDetailsThread()
        thread.start()


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app)
