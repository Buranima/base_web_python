import socketio

socketio_Client = socketio.Client()

socketio_Client.connect("http://127.0.0.1:5000", transports=["websocket"])

@socketio_Client.on("test")
def test_Socketio_Client(response):
    print("Received from server:", response)

socketio_Client.emit("test", {"text": "Hello from Client"})

if __name__ == "__main__":
    while True:
        while not socketio_Client.connected:
            socketio_Client.connect("http://127.0.0.1:5000", transports=["websocket"])