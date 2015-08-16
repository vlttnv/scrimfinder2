var convs = [];
var forms = [];

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
    link.href="javascript:start_a_chat(" + usr.id + "," +nested_msg['id'] + ");";
    link.className="list-group-item";
    var linkText = document.createTextNode(" " + nested_msg['nick']);
    link.appendChild(img);
    link.appendChild(linkText);
    $('#user_box').append(link);
  }
});


socket.on('my_message', function(msg){
  var msg_json = JSON.parse(msg);
  var id = usr.id + "_" + msg_json.id;
  console.log(convs);
  console.log(msg_json.id);

  if (convs.indexOf(parseInt(msg_json.id)) == -1) {
    console.log("pop a new chat");
    start_a_chat(usr.id, msg_json.id);
    $('#' + id +'_messages').append($('<li>').text(msg_json.txt));
  } else {
    console.log('just add msg');
    $('#' + id +'_messages').append($('<li>').text(msg_json.txt));
  }
});


function start_a_chat(id1, id2) {
  if (convs.indexOf(id2) != -1) {

  } else {
    console.log("starting a cat");
    convs.push(id2);
    var id = id1 + "_" + id2;
    var tab_element = document.createElement('li');
    tab_element.class = "active";

    var tab_li = document.createElement('a');
    tab_li.href =  "#" + id + "_" + "tab";
    tab_li.setAttribute("aria-expanded", "true");
    tab_li.setAttribute("data-toggle", "tab");
    var linkText = document.createTextNode(id2);

    tab_li.appendChild(linkText);
    tab_element.appendChild(tab_li);

    var tab_line = document.getElementById('tab_line');
    tab_line.appendChild(tab_element);

    var tab_content_div = document.createElement('div');
    tab_content_div.className = "tab-pane fade";
    tab_content_div.id = id + "_" + "tab";
    tab_content_div.style = "overflow-y: scroll;";

    var messages_ul = document.createElement('ul');
    messages_ul.id = id + "_" + "messages";
    messages_ul.className = "chatty";
    messages_ul.setAttribute("style", "overflow-y: scroll; word-wrap: break-word;");

    var form_el = document.createElement('form');
    form_el.id = id + "_" + "form";

    var form_input = document.createElement('input');
    form_input.className = "form-control";
    form_input.setAttribute("autocomplete", "off");
    form_input.id = id + "_" + "inputmsg";
    form_input.type = "text";

    form_el.appendChild(form_input);

    tab_content_div.appendChild(messages_ul);
    tab_content_div.appendChild(form_el);

    var myTabContent = document.getElementById("myTabContent");
    myTabContent.appendChild(tab_content_div);
    $('#' + id+ '_messages').height($('#main_box').height()-100);

    $('#' + id + '_form').submit(function(){
      socket.emit('send_msg', id2, $('#' + id + '_inputmsg').val());
      //console.log($('#inputmsg').val());
      $('#' + id + '_messages').append($('<li>').text($('#' + id + '_inputmsg').val()));

      $('#' + id + '_inputmsg').val('');
      $("#" + id + "_messages").scrollTop($("#" + id + "_messages")[0].scrollHeight);
      return false;
    });
  }

}
