var socket = io.connect('http://' + document.domain + ':' + location.port);

document.getElementById('send-btn').addEventListener('click', function() {
    var message = document.getElementById('message-input').value;
    socket.emit('send_message', {message: message});
});

socket.on('receive_message', function(data) {
    var msgDiv = document.createElement('div');
    msgDiv.textContent = data.message;
    document.getElementById('messages').appendChild(msgDiv);
});
