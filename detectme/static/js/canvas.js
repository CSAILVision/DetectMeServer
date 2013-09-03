
var canvasModule =  (function(){
  var _canvas = document.getElementById("boxPositionCanvas");
  var _ctx = _canvas.getContext("2d");
  
  return{
    settings: {
      numArticles: 5,
      articleList: $("#article-list"),
      moreButton: $("#more-button")
    },

    drawDot: function(x,y){
      _ctx.fillRect(x,y,2,2);
    },

    drawRectangle: function(x,y,w,h){
      _ctx.strokeStyle = 'black';
      _ctx.strokeRect(x,y,w,h);
    },

    drawUnitaryRectangle: function(x,y,w,h){
      console.log('drawing unitary rectangle:'+x+','+y+','+w+','+h);
      this.drawRectangle(x*_canvas.width, y*_canvas.height, w*_canvas.width, h*_canvas.height);
    },

    clearScreen: function(){
      _canvas.width = _canvas.width;
    },

    setColor: function(color){
      _ctx.strokeStyle = color;
    }
  };

}());

// EVENT HANDLERS

$('#clearButton').click(function() {
  canvasModule.clearScreen();
});

$('#selectColor').change(function () {
  canvasModule.setColor($('#selectColor option:selected').val());
});



// window.onload = function() {
//     var myCanvas = document.getElementById("boxPosition");
//     var curColor = $('#selectColor option:selected').val();
//     if(myCanvas){
//       var isDown      = false;
//       var ctx = myCanvas.getContext("2d");
//       var canvasX, canvasY;
//       ctx.lineWidth = 5;
       
//       $(myCanvas)
//       .mousedown(function(e){
//         isDown = true;
//         ctx.beginPath();
//         canvasX = e.pageX - myCanvas.offsetLeft;
//         canvasY = e.pageY - myCanvas.offsetTop;
//         ctx.moveTo(canvasX, canvasY);
//       })
//       .mousemove(function(e){
//         if(isDown !== false) {
//         canvasX = e.pageX - myCanvas.offsetLeft;
//         canvasY = e.pageY - myCanvas.offsetTop;
//         ctx.lineTo(canvasX, canvasY);
//         ctx.strokeStyle = curColor;
//         ctx.stroke();
//         }
//       })
//       .mouseup(function(e){
//         isDown = false;
//         ctx.closePath();
//       });
//     }
    
//     function drawDot(x,y){
//       ctx.fillRect(x,y,2,2); // fill in the pixel at (10,10)
//     }


//     $('#selectColor').change(function () {
//     curColor = $('#selectColor option:selected').val();
//     });
//   };