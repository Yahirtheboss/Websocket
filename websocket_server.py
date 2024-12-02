## Send information would be POST Request
## Get information would be GET Request

import asyncio
import websockets
import serial

## Configure serial communication
ser = serial.Serial('COM8', 115200, timeout=0.1)  # Replace 'COM8' with your port, port for ROLIE

async def handle_websocket(websocket):
    async for message in websocket:
        print(f"Command received: {message}")
        
        ## Validate the command
        if message in ["Forward", "Reverse", "Turn Right", "Turn Left"]:
            response = f"Executing: {message}"
            ser.write(f"{message}\n".encode())  ## Send command via serial
        else:
            response = "Unknown command."
        
        await websocket.send(response)  ## Respond back to the WebSocket client
        
async def main():
    async with websockets.serve(handle_websocket, "localhost", 8765):
        print("WebSocket server is running on ws://localhost:8765")
        await asyncio.Future()  # Run forever

# Run the server
if __name__ == "__main__":
    asyncio.run(main())

