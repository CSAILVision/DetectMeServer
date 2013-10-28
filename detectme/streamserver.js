var http = require('http').createServer();
var io = require('socket.io').listen(http);
// var redis = require('redis').createClient();
var iphoneAddress;
var browser_clients = {}; // 'id': socket
var iphone_clients = {}; // 'id': 'iphone_ip'

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
  

  socket.on('browser_connect', function(username){
    console.log(username + ' browser connected');

    browser_clients[username] = socket;

    iphone_ip = iphone_clients[username];
    if(iphone_ip!==undefined){
      socket.emit('start_listening_iphone', iphone_ip);
    }
  });

  socket.on('iphone_connect', function(username){
    var address = socket.handshake.address;
    console.log(username + ' iphone connected from ' + address.address + ':' + address.port);
    
    iphone_clients[username] = address.address;

    browser_socket = browser_clients[username];
    if(browser_socket!==undefined){
      browser_socket.emit('start_listening_iphone', address.address);
    }
  });

  socket.on('iphone_disconnect', function(username){
    console.log(username + ' iphone has disconnected');
    
    browser_socket = browser_clients[username];
    if(browser_socket!==undefined){
      browser_socket.emit('stop_listening_iphone', '');
    }
  });

    // Handle disconnection of clients
  socket.on('disconnect', function () {
    socket.get('clientid', function (err, clientid) {
      console.log(clientid + 'has disconnected.');
    });
  });


  // // New client connecting
  // socket.on('set clientid', function (clientid) {
  //   socket.set('clientid', clientid, function () {
  //     console.log(clientid + ' has just connected.');
  //   });

  //   // io.sockets.volatile.emit('bc_begin_connection', address.address);
  //   io.sockets.volatile.emit('start_listening_iphone', iphoneAddress);
  // });

  // // socket.on('mobile_connecting', function(sessionData){
  // //   redis.set(socket.id, sessionData.username + '_mobile', function(err) {
  // //     if (err) throw err;
  // //     console.log('Registered mobile user with id: ' + socket.id + 'and username: ' + sessionData.username);
  // //   });
  // // });

  // // socket.on('web_connecting', function(sessionData){
  // //   redis.set(sessionData.username + '_web', socket.id, function(err) {
  // //     if (err) throw err;
  // //     console.log('Registered web user with id: ' + socket.id + 'and username: ' + sessionData.username);
  // //   });
  // // });

  // // Notify web browser that the iphone is transmitting
  // socket.on('begin_connection', function(){
  //   var address = socket.handshake.address;
  //   console.log("New iphone connection from " + address.address + ":" + address.port);
  //   iphoneAddress = address.address;
  //   io.sockets.volatile.emit('start_listening_iphone', address.address);
  // });

  // // Notify web browser that the iphone has stopped transmitting
  // socket.on('end_connection', function(){
  //   io.sockets.volatile.emit('stop_listening_iphone', '');
  // });

  // // Handle disconnection of clients
  // socket.on('disconnect', function () {
  //   socket.get('clientid', function (err, clientid) {
  //     console.log(clientid + 'has disconnected.');
  //   });
  // });

});


