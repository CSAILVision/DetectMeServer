var http = require('http').createServer();
var io = require('socket.io').listen(http);
// var redis = require('redis').createClient();


http.listen(7000, function() {
    console.log((new Date()) + ' Server is listening on port 7000');
});

// creating a new websocket for the transmission of the detections
io.sockets.on('connection', function (socket){

  // socket.emit('greeting', { hello: 'world' });

  // New client connecting
  socket.on('set clientid', function (clientid) {
    socket.set('clientid', clientid, function () {
      console.log(clientid + 'has just connected.');
    });
  });

  socket.on('mobile_connecting', function(sessionData){});
  socket.on('web_connecting', function(sessionData){});

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


