/************** WEB SOCKET *****************/

// Establish the connection with the server
var socket = io.connect('http://127.0.0.1:7000');

socket.on('bc_begin_connection', function(address){
  console.log('Initiating connection to:' + address);
  webSocketClient.setIOSAddress(address);
  webSocketClient.beginListening();
});

socket.on('bc_end_connection', function(){
  webSocketClient.endListening();
});

// Create a new socket connection
socket.on('connect', function() {
  socket.emit('set clientid', 'browser');
});