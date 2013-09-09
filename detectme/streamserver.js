var http = require('http').createServer();
var io = require('socket.io').listen(http);
// var redis = require('redis').createClient();


var connection = (function(){

}());



http.listen(7000, function() {
    console.log((new Date()) + ' Server is listening on port 7000');
});

// redis.on("error", function (err) {
//     console.log("Error " + err);
// });

// creating a new websocket for the transmission of the detections
io.sockets.on('connection', function (socket){

  console.log('new connection');
  
  // New client connecting
  socket.on('set clientid', function (clientid) {
    socket.set('clientid', clientid, function () {
      console.log(clientid + 'has just connected.');
    });
  });

  // socket.on('mobile_connecting', function(sessionData){
  //   redis.set(socket.id, sessionData.username + '_mobile', function(err) {
  //     if (err) throw err;
  //     console.log('Registered mobile user with id: ' + socket.id + 'and username: ' + sessionData.username);
  //   });
  // });

  // socket.on('web_connecting', function(sessionData){
  //   redis.set(sessionData.username + '_web', socket.id, function(err) {
  //     if (err) throw err;
  //     console.log('Registered web user with id: ' + socket.id + 'and username: ' + sessionData.username);
  //   });
  // });

  // socket.on('emit_bb', function(bb){
  //   client.get(socket.id, function(err, username) {
  //     if (err) throw err;
  //     username = username.replace('_mobile','');

  //     client.get(username, function(err, webSocketId) {
  //       if (err) throw err;
  //       io.sockets.socket(webSocketId).emit('broadcast_bb', bb);
  //     });
  //   });
  // });

  // Client sending detected bounding box
  socket.on('emit_bb', function(bb){
    console.log('received bb:', bb);
    io.sockets.volatile.emit('broadcast_bb', bb);
  });

  socket.on('emit_image', function(imageBase64){
    io.sockets.volatile.emit('broadcast_image', imageBase64);
  });

  // Handle disconnection of clients
  socket.on('disconnect', function () {
    socket.get('clientid', function (err, clientid) {
      console.log(clientid + 'has disconnected.');
    });
  });

});


