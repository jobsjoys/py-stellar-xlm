
$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');

    //receive details from server
    socket.on('address_details', function(msg) {
        console.log('Balance: '  + msg.balance + ' XLM | Last tx: ' + msg.amount + ' ' + msg.asset_code + ' | Memo: ' + msg.memo);

        $('#label').html('Balance: '  + msg.balance + ' XLM | Last tx: ' + msg.amount + ' ' + msg.asset_code + ' | Memo: ' + msg.memo);
        $('body').css('background-color',msg.memo);
    });

});