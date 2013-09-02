var http = require('http').createServer();
var io = require('socket.io').listen(http);
 

http.listen(7000, function() {
    console.log((new Date()) + ' Server is listening on port 8080');
});

// creating a new websocket for the transmission of the detections
io.sockets.on('connection', function (socket){

  // socket.emit('greeting', { hello: 'world' });
  console.log("New connection!");

  // New client connecting
  socket.on('set clientid', function (clientid) {
    socket.set('clientid', clientid, function () {
      console.log(clientid + 'has just connected.');
    });
  });

  // Client sending detected bounding box
  socket.on('emit_bb', function(bb){
    console.log('received bb:', bb);
    io.sockets.volatile.emit('broadcast_bb', bb);
  });

  // Handle disconnection of clients
  socket.on('disconnect', function () {
    socket.get('clientid', function (err, clientid) {
      console.log(clientid + 'has disconnected.');
    });
  });

});


