/************** WEB SOCKET *****************/

// Establish the connection with the server
var socket = io.connect('http://127.0.0.1:7000');

// socket.on('greeting', function(data){
//   msg = '<li class="list-group-item">' + data.hello +'</li>';
//   $('#broadcast-msg').append(msg);
//   console.log('received greeting data:',data);
// });

// //When receiving bb data from other users
// socket.on('broadcast_bb', function (bb) {
//   var msg = '<li>' + bb.xcoord + ',' + bb.ycoord + '</li>';
//   boundingBox.drawBox(bb);
//   $('#replaceable').replaceWith(msg);
//   console.log('received bounding box:',bb);
// });

// // When receiving image data
// socket.on('broadcast_image', function(imageBase64){
//   document.getElementById("detecting-image").src="data:image/jpeg;base64,"+imageBase64;
// });

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