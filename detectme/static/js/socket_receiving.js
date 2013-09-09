
var webSocketClient =  (function(){
  var _address = '127.0.0.1';

  return{

    setIOSAddress: function(address){
      _address = address;
    },

    beginListening: function(){
		window.WebSocket = window.WebSocket || window.MozWebSocket;
		var websocket = new WebSocket('ws://'+_address+':9000','echo-protocol');
		
		websocket.onopen = function () {
			console.log('socket opened');
		};

		websocket.onerror = function () {
			console.log('socket error');
		};

		websocket.onmessage = function (message) {

			var messageContent = JSON.parse(message.data);

			// output video
			document.getElementById('detecting-image').src="data:image/jpeg;base64,"+ messageContent.imageBase64;

			// draw bb
			var msg = '<li>' + messageContent.bb.xcoord + ',' + messageContent.bb.ycoord + '</li>';
			boundingBox.drawBox(messageContent.bb);
			$('#replaceable').replaceWith(msg);
			//console.log('received bounding box:',messageContent.bb);
		};
	},

	endListening: function(){
		websocket.close();
	}

  };

}());




$('#connect-button').click(function(e) {
	webSocketClient.beginListening();
});