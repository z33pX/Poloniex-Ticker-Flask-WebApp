
$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/tiDa');
    var numbers_received = [];

    //receive details from server
    socket.on('tickerData', function(msg) {

        // Header
        header = '<thead><tr>'
        header += '<th></th>'
        for (i = 0; i < msg.ticker_label.length; i++) {
            header += '<th>' + msg.ticker_label[i] + '</th>';
        }
        header += '</tr></thead>'

        // Column last
        last = '<tr><td>Last</td>'
        for (i = 0; i < msg.ticker_label.length; i++) {
            last += '<td id="' + msg.ticker_label[i] + '_last">' + msg.ticker_data[msg.ticker_label[i]]['last'] + '</td>';
        }
        last += '</tr>'

        // Column percentChange
        percentChange = '<tr><td>Percent change</td>'
        for (i = 0; i < msg.ticker_label.length; i++) {
            percentChange += '<td id="' + msg.ticker_label[i] + '_percentChange">' + msg.ticker_data[msg.ticker_label[i]]['percentChange'] + '</td>';
        }
        percentChange += '</tr>'

        // Column Last
        quoteVolume = '<tr><td>Quote volume</td>'
        for (i = 0; i < msg.ticker_label.length; i++) {
            quoteVolume += '<td id="' + msg.ticker_label[i] + '_quoteVolume">' + msg.ticker_data[msg.ticker_label[i]]['quoteVolume'] + '</td>';
        }
        quoteVolume += '</tr>'

        // Body
        body = '<tbody>' + last + percentChange + quoteVolume + '</tbody>'

        table = header + body

        $('#app').html(table);
    });

});