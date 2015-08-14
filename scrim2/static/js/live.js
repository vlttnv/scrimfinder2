function SetHeight(){
  var h = $(window).height();
  $("#user_box").height(h-205);
  $("#main_box").height(h-200);
  $('#messages').height($('#main_box').height()-100);
}

$(document).ready(SetHeight);
$(window).resize(function () {
      SetHeight();
});

var socket = io("128.199.45.141:8080", {
  'reconnection': false
});
var usr = {id: document.getElementById('id').value,
  rv: document.getElementById('rv').value,
  nick: document.getElementById('nick').value,
  avatar: document.getElementById('avatar').value,
  sid: document.getElementById('sid').value};

socket.emit('auth', JSON.stringify(usr));
socket.emit('get_on', "gim");
socket.on('popu_on', function(msg){
  json_msg = JSON.parse(msg);
  for (var item in json_msg) {
    var nested_msg = JSON.parse(json_msg[item]);
    var link = document.createElement('a');
    var img = document.createElement('img');
    img.src = nested_msg['avatar'];
    link.href="/profile/" + nested_msg['sid'];
    link.className="list-group-item";
    var linkText = document.createTextNode(" " + nested_msg['nick']);
    link.appendChild(img);
    link.appendChild(linkText);
    $('#user_box').append(link);
  }
});


socket.on('my_message', function(msg){
  console.log(msg);
  $('#messages').append($('<li>').text(msg));
});

$('form').submit(function(){
  socket.emit('send_msg', "2",$('#inputmsg').val());
  console.log($('#inputmsg').val());
  $('#messages').append($('<li>').text($('#inputmsg').val()));

  $('#inputmsg').val('');
  return false;
});

