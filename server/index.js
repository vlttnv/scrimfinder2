var redis = require('redis'), red_client = redis.createClient();
var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

var user_socket = {};

// Redis
red_client.on("error", function (err) {
  console.log("Redis error: " + err);
});


io.on('connection', function(socket){
  console.log('a user connected');
  var usr = undefined;

    // Auth the user
    socket.on('auth', function( msg){
      console.log('Authing: ' + msg);
      json_msg = JSON.parse(msg);
      user_socket[json_msg['id']] = socket;

      usr = json_msg;
      var token = undefined;
      red_client.get(json_msg['id']+":token", function(err, reply){
        try {
          token = reply.toString();
        } catch(err) {
          console.log("Oh boy...");
        }
      });
      if (token == json_msg['token']) {
        red_client.set(json_msg['id'], "online");
        console.log("Logged in");
        red_client.del(json_msg['id'] + ":token");

        // Add to online list
        var online_users;
        red_client.get("online_users", function(err, reply){
          try {
            online_users = reply.toString();
            json_online_users = JSON.parse(online_users);

            json_online_users[json_msg['id']] = JSON.stringify(json_msg);
            red_client.set("online_users", JSON.stringify(json_online_users));
          } catch (err) {
            ob = {};
            ob[usr.id] = JSON.stringify(usr);
            red_client.set("online_users", JSON.stringify(ob));
          }
        });

      } else {
        socket.disconnect()
      }
    });

    socket.on('get_on', function(msg){
      // if authed
      var onl_list = undefined;
      red_client.get("online_users", function(err, reply) {
        if (err==null) {
          onl_list = reply.toString();
          socket.emit("popu_on", onl_list);
        } else {
          onl_list = "0";
          socket.emit("popu_on", onl_list);
        }
      });

    });


    socket.on('send_msg', function(private_id, msg){
      the_msg = {};
      the_msg.txt = msg;
      the_msg.id = usr.id;
      console.log(the_msg.txt);
      socket.to(user_socket[private_id].id).emit('my_message', JSON.stringify(the_msg));
      console.log(user_socket[private_id].id);
    });

    socket.on('disconnect', function(){
      console.log('user disconnected');
      try {
        red_client.set(usr['id'], "offline");
      } catch(err) {
        console.log("Oh boy...");
      }
      // Add to online list
      var online_users;
      red_client.get("online_users", function(err, reply){
        try {
          online_users = reply.toString();
          json_online_users = JSON.parse(online_users);
          delete json_online_users[usr['id']];
          red_client.set("online_users", JSON.stringify(json_online_users));
        } catch(err) {
          console.log("Well crap...")
        }
      });
    });
});



http.listen(8080, function(){
  console.log('listening on *:3000');
});
