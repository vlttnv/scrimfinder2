var redis = require('redis'), red_client = redis.createClient();
var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

// Redis
red_client.on("error", function (err) {
  console.log("Redis error: " + err);
});


io.on('connection', function(socket){
  console.log('a user connected');
  var usr = undefined;

    // Auth the user
    socket.on('auth', function(msg){
      console.log('Authing: ' + msg);
      if (msg == "1") {
        red_client.set(msg, "online");
        usr = msg;
        console.log("Logged in");
      } else {
        socket.disconnect()
      }
    });


  socket.on('disconnect', function(){
    console.log('user disconnected');
    red_client.del(usr)
  });

});



http.listen(8080, function(){
  console.log('listening on *:3000');
});
