
$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');

    //receive details from server
    socket.on('address_details', function(msg) {
        console.log('Balance: '  + msg.balance + ' XLM | Last tx: ' + msg.amount + ' ' + msg.asset_code + ' | Memo: ' + msg.memo);

        $('#label').html('Balance: '  + msg.balance + ' XLM | Last tx: ' + msg.amount + ' ' + msg.asset_code + ' | Memo: ' + msg.memo);
        //$('body').css('background-color',msg.memo);
        $('#funded').html(Math.floor((msg.balance/100000)*100) + '%');
        $('#progress').css('width',Math.floor((msg.balance/100000)*100) + '%');
        $('#raised').html(msg.balance + ' XLM');
        $('#last_tx').html(msg.amount + ' ' + msg.asset_code);
        $('#memo').html(msg.memo);

    });

});