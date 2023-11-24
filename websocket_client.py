import websocket
import json

#  Websocket URL
websocket_url="wss://functionup.fintarget.in/ws?id=fintarget-functionup"

# Function to handle received messages
def on_message(ws,message):
    data=json.loads(message)
    print("Received Data:",data)

# Connect to Webscocket
ws= websocket.WebSocketApp(websocket_url, on_message=on_message)
ws.run_forever()