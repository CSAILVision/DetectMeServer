

function beginListening(){
	window.WebSocket = window.WebSocket || window.MozWebSocket;

	var websocket = new WebSocket('ws://128.31.34.0:9000',
		'echo-protocol');

	websocket.onopen = function () {
		console.log('socket opened');
	};

	websocket.onerror = function () {
		console.log('socket error');
	};

	websocket.onmessage = function (message) {

		console.log('Received a box');
		
		var messageContent = JSON.parse(message.data);

		//draw bb
		var msg = '<li>' + messageContent.bb.xcoord + ',' + messageContent.bb.ycoord + '</li>';
		boundingBox.drawBox(messageContent.bb);
		$('#replaceable').replaceWith(msg);
		console.log('received bounding box:',messageContent.bb);

		//output video
		document.getElementById('video').src="data:image/jpeg;base64,"+ messageContent.imageBase64;

	};

}

$('#connectButton').click(function(e) {
	beginListening();
});