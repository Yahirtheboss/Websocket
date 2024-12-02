import asyncio
import websockets


async def send_commands():
    uri = "ws://localhost:8765"  # URL of the WebSocket server


    async with websockets.connect(uri) as websocket:
        print("Connected to WebSocket server.")
        print("Type 'off' to quit.")
       
        while True:
            # Prompt the user for a command
            command = input("Enter a command (Forward, Reverse, Turn Right, Turn Left): ")
           
            # Exit the loop if the user types 'off'
            if command.lower() == "off":
                print("Exiting...")
                break


            # Send the command to the server
            await websocket.send(command)
            print(f"Sent command: {command}")


            # Wait for the response from the server
            response = await websocket.recv()
            print(f"Server response: {response}")


if __name__ == "__main__":
    asyncio.run(send_commands())  # Run the async function
