import asyncio
import websockets
import serial
from websockets.exceptions import ConnectionClosedError

class WebSocketServer:
    def __init__(self, host="0.0.0.0", port=8765):  # Changed host to "0.0.0.0"
        self.host = host
        self.port = port
    
    async def handle_websocket(self, websocket):
        try:
            print(f"New client connected from {websocket.remote_address}")
            async for message in websocket:
                print(f"Command received: {message}")
                
                if message in ["Forward", "Reverse", "Turn Right", "Turn Left"]:
                    response = f"Executing: {message}"
                    # try:
                    #     ser.write(f"{message}\n".encode())
                    # except serial.SerialException as e:
                    #     response = f"Serial communication error: {e}"
                else:
                    response = "Unknown command"
                
                await websocket.send(response)
                
        except ConnectionClosedError:
            print(f"Client {websocket.remote_address} disconnected")
        except Exception as e:
            print(f"Error handling client {websocket.remote_address}: {e}")
        finally:
            print(f"Connection closed with {websocket.remote_address}")
    
    async def start(self):
        try:
            async with websockets.serve(
                self.handle_websocket, 
                self.host, 
                self.port,
                ping_interval=600,    # Reduced ping interval to better handle connections
                ping_timeout=10    
            ) as server:
                print(f"WebSocket server is running on ws://{self.host}:{self.port}")
                await asyncio.Future()  # Run forever
        except Exception as e:
            print(f"Server error: {e}")

def main():
    server = WebSocketServer()  # Will use "0.0.0.0" by default now
    try:
        asyncio.run(server.start())
    except KeyboardInterrupt:
        print("\nServer shutdown by user")
    finally:
        print("Server shutdown complete")

if __name__ == "__main__":
    main()