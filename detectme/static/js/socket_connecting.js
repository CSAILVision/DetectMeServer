/************** WEB SOCKET *****************/

// Establish the connection with the server
var socket = io.connect('http://128.52.160.100:7000');

socket.on('start_listening_iphone', function(address){
  console.log('Initiating connection to:' + address);

  // Set the address and begin listening to the iphone as a server
  webSocketClient.setIOSAddress(address);
  webSocketClient.beginListening();
});

socket.on('stop_listening_iphone', function(){
  webSocketClient.endListening();
});

// Create a new socket connection
socket.on('connect', function() {
  socket.emit('browser_connect', 'username');
});

