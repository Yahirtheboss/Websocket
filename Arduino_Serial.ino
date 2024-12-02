const int ledPin = 13; // LED connected to digital pin 13 (can change to any suitable pin)

void setup() {
  // Initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);

  // Initialize serial communication at 9600 baud rate:
  Serial.begin(57600);
}

void loop() {
  // Check if data is available to read from the serial port:
  if (Serial.available() > 0) {
    // Read the incoming string:
    String incomingData = Serial.readStringUntil('\n');
    incomingData.trim(); // Remove any extra whitespace

    // Check if the command is "Forward" or "Reverse":
    if (incomingData == "Forward") {
      // Turn the LED on:
      digitalWrite(ledPin, HIGH);
      Serial.println("LED turned ON"); // Send feedback
    } else if (incomingData == "Reverse") {
      // Turn the LED off:
      digitalWrite(ledPin, LOW);
      Serial.println("LED turned OFF"); // Send feedback
    } else {
      Serial.println("Unknown command");
    }
  }
} 
