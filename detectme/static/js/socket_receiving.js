// Connects as a client to the iphone to get the images send

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
			boundingBox.drawBox(messageContent.bb);
		};
	},

	endListening: function(){
		websocket.close();
	}

  };

}());