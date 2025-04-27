from flask import Flask, render_template
from flask_socketio import SocketIO, emit

# Initialize the Flask app and SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('index.html')

# Event to handle message sending
@socketio.on('send_message')
def handle_message(data):
    message = data['message']
    # Emit the message to all connected clients
    emit('receive_message', {'message': message}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)

