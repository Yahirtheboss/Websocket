import asyncio
import websockets
import serial
from websockets.exceptions import ConnectionClosedError

ser = serial.Serial('COM8', 115200, timeout=1)  # Replace 'COM8' with your port for NANO '/dev/ttyUSB0'

class WebSocketServer:
    def __init__(self, host="0.0.0.0", port=8765):
        self.host = host
        self.port = port
        self.latest_command = None
        self.command_event = asyncio.Event()
   
    async def handle_websocket(self, websocket):
        try:
            print(f"New client connected from {websocket.remote_address}")
            async for message in websocket:
                print(f"Command received: {message}")
               
                if message in ["Forward", "Reverse", "Turn Right", "Turn Left"]:
                    self.latest_command = message
                    self.command_event.set()  # Notify that a new command is available
                    response = f"Executing: {message}"
                else:
                    response = "Unknown command"
               
                await websocket.send(response)
               
        except ConnectionClosedError:
            print(f"Client {websocket.remote_address} disconnected")
        except Exception as e:
            print(f"Error handling client {websocket.remote_address}: {e}")
        finally:
            print(f"Connection closed with {websocket.remote_address}")
   
    async def send_latest_command_to_mcu(self):
        while True:
            await self.command_event.wait()  # Wait for a new command to be available
            if self.latest_command:
                try:
                    ser.write(f"{self.latest_command}\n".encode())
                    print(f"Sent command to MCU: {self.latest_command}")
                except serial.SerialException as e:
                    print(f"Serial communication error: {e}")
                finally:
                    self.command_event.clear()  # Clear the event until a new command is received


    async def start(self):
        try:
            server = await websockets.serve(
                self.handle_websocket,
                self.host,
                self.port,
                ping_interval=1,    # Reduced ping interval to better handle connections
                ping_timeout=600    
            )
            print(f"WebSocket server is running on ws://{self.host}:{self.port}")
           
            # Run both the WebSocket server and the command sender concurrently
            await asyncio.gather(
                server.wait_closed(),  # Keeps the server running
                self.send_latest_command_to_mcu()  # Keeps sending commands to the MCU
            )
        except Exception as e:
            print(f"Server error: {e}")


def main():
    server = WebSocketServer()  # Will use "129.113.1.74" by default


    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(server.start())
    except KeyboardInterrupt:
        print("\nServer shutdown by user")
    finally:
        loop.close()
        print("Server shutdown complete")


if __name__ == "__main__":
    main()
