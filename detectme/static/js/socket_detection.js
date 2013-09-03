/************** WEB SOCKET *****************/


var boundingBox =  (function(){

  var _x,_y,_w,_h;
  
  return{

    setBoxFromReceived: function(bb){
      _x=bb.xcoord;
      _y=bb.ycoord;
      _w=bb.width;
      _h=bb.height;
    },
    drawBox: function(bb){
      this.setBoxFromReceived(bb);
      canvasModule.clearScreen();
      canvasModule.drawUnitaryRectangle(_x,_y,_w,_h);
    }
  };

}());

// Establish the connection with the server
var socket = io.connect('http://127.0.0.1:7000');

socket.on('greeting', function(data){
  msg = '<li class="list-group-item">' + data.hello +'</li>';
  $('#broadcast-msg').append(msg);
  console.log('received greeting data:',data);
});

//When receiving bb data from other users
socket.on('broadcast_bb', function (bb) {
  var msg = '<li>' + bb.xcoord + ',' + bb.ycoord + '</li>';
  boundingBox.drawBox(bb);
  $('#replaceable').replaceWith(msg);
  console.log('received bounding box:',bb);
});

// Create a new socket connection
socket.on('connect', function() {
  socket.emit('set clientid', 123);
});