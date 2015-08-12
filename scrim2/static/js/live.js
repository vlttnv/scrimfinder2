var socket = io("128.199.45.141:8080");

socket.emit('auth', document.getElementById('nick').value);



