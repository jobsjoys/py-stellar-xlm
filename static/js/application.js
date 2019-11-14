$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');

    //receive details from server
    socket.on('address_details', function(msg) {
        $('#funded').html(Math.floor((msg.balance/msg.target)*100) + '%');
        $('#progress').css('width',Math.floor((msg.balance/msg.target)*100) + '%');
        $('#raised').html(msg.balance + ' XLM');
        $('#last_tx').html(msg.amount + ' ' + msg.asset_code);
        $('#publickey').html(msg.publickey);
        $('#target').html(msg.target + ' XLM');
        $('#memo').html(msg.memo);
    });
});