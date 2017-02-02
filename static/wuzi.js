/*状态事件*/
function status1(){
      //window.location.href=window.location;
      if(isbegin){
         alert("game has begun");
         return;
      }
      document.getElementById('qizi').src="static/black.png";
   }
function status2(){
      if(isbegin){
         alert("game has begun");
         return;
      }
      document.getElementById('qizi').src="static/white.png";
   }

/* 控件事件 */
function closeFunction() {
   if (confirm("是否退出游戏？")) {
      window.close();
   } else {
      history.back();
   }
}

/* 判断输赢 */
var cnt = (function() {
   var curr ='black';
   return function() {
      var tmp = curr;
      if (curr == 'black') {
         curr = 'white';
      } else {
         curr = 'black';
      }
      return tmp;
   }
})();

var tds = document.getElementsByTagName('td');
var iswin = false; // 有没有分出胜负
var isbegin = false;
// 负责下棋，即改变单元格的背景
var xia = function() {
   // 判断是否已分出胜负
   //var color = cnt();
   if (iswin) {
      alert('游戏结束!');
      return;
   }
   if (this.style.background.indexOf('.png') >= 0) {
      alert('不能重复放置棋子！');
      return;
   }
   //x: this.cellIndex,y: this.parentElement.rowIndex
   alert(this.cellIndex+"  "+this.parentElement.rowIndex);
   this.style.background = 'url(' + document.getElementById('qizi').src + ')';
   isbegin = true;
   xmlHttp = new XMLHttpRequest();
   xmlHttp.onreadystatechange = callback;
   xmlHttp.open("GET","/Step?x=1&y=1",true)
   xmlHttp.send(null);
   //todo 1.according to location show qizi 2.step need know where you hit and return where ai put
   //judge.call(this, color); // 下完棋后判断胜负
}

function callback(){
   if(xmlHttp.readyState == 4 && xmlHttp.status == 200){
      var responseText = xmlHttp.responseText;
      //var json = responseText.parseJSON();
      var obj = eval('(' + responseText + ')');
      alert(getCell(obj.x,obj.y));
      getCell(obj.x,obj.y).style.background = getAnotherPic();
   }
}

function getAnotherPic(){
   src = "static/white.png"
   if(document.getElementById('qizi').src == "static/white.png"){
      src = "static/black.png";
   }
   return 'url(' + src + ')';
}

function getCell(rowIndex,cellIndex){
   //return $("#chessboard").eq(rowIndex).find("td").eq(cellIndex);
   return document.getElementById("chessboard").rows[rowIndex].cells[cellIndex];
}

window.onload = function() {
   document.getElementsByTagName('table')[0].onclick = function(ev) {
      // 1. 下棋
      //alert(1);
      // 2. 判断胜负
      //alert(ev.target);
      xia.call(ev.target);
   };
}