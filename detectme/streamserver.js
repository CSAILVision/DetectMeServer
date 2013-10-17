var http = require('http').createServer();
var io = require('socket.io').listen(http);
// var redis = require('redis').createClient();
var iphoneAddress;

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
      console.log(clientid + ' has just connected.');
    });

    // io.sockets.volatile.emit('bc_begin_connection', address.address);
    io.sockets.volatile.emit('bc_begin_connection', iphoneAddress);
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

  // Notify web browser that the iphone is transmitting
  socket.on('begin_connection', function(){
    var address = socket.handshake.address;
    console.log("New connection from " + address.address + ":" + address.port);
    iphoneAddress = address.address;
    io.sockets.volatile.emit('bc_begin_connection', address.address);
  });

  // Notify web browser that the iphone has stopped transmitting
  socket.on('end_connection', function(){
    io.sockets.volatile.emit('bc_end_connection', '');
  });

  // Handle disconnection of clients
  socket.on('disconnect', function () {
    socket.get('clientid', function (err, clientid) {
      console.log(clientid + 'has disconnected.');
    });
  });

});


