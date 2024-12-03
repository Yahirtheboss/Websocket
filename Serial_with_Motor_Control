const int Motor1Pin1 = 32;   // Motor control pin 1 for clockwise rotation
const int Motor1Pin2 = 33;   // Motor control pin 2 for counterclockwise rotation




const int Motor2Pin1 = 25;   // Motor control pin 1 for clockwise rotation
const int Motor2Pin2 = 26;   // Motor control pin 2 for counterclockwise rotation




const int pwmFreq = 1;          // Frequency in Hz
const int pwmResolution = 8;    // Resolution of 8 bits (0-255)




// Motor speed control
const int maxMotorSpeed = 150; // Maximum speed (0-255)


// Deceleration step and delay
const int decelerationStep = 10; // Speed reduction per step
const int decelerationDelay = 50; // Delay per step in milliseconds


// Pulse duration
const int pulseDuration = 500; // Pulse duration in milliseconds




// Gets commands from the NANO through serial communication that gets it from websocket.




void setup()
{
  // Start serial communication
  Serial.begin(115200);




  // Set motor control pins as outputs
  pinMode(Motor1Pin1, OUTPUT);
  pinMode(Motor1Pin2, OUTPUT);
  pinMode(Motor2Pin1, OUTPUT);
  pinMode(Motor2Pin2, OUTPUT);




  // Stop all motors initially
  stopMotors();




  // Set PWM frequency and resolution for both motor pins
  // analogWriteFrequency(Motor1Pin1, pwmFreq);
  // analogWriteResolution(Motor1Pin1, pwmResolution);
  // analogWriteFrequency(Motor1Pin2, pwmFreq);
  // analogWriteResolution(Motor1Pin2, pwmResolution);




  // analogWriteFrequency(Motor2Pin1, pwmFreq);
  // analogWriteResolution(Motor2Pin1, pwmResolution);
  // analogWriteFrequency(Motor2Pin2, pwmFreq);
  // analogWriteResolution(Motor2Pin2, pwmResolution);
}




void loop()
{
  // When we read something from serial communication.
  if (Serial.available() > 0)
  {
    // Read the incoming string:
    String incomingData = Serial.readStringUntil('\n');
    incomingData.trim(); // Remove any extra whitespace


    // Serial.print(incomingData);


    if (incomingData == "Forward")
    {
      moveForward();
    }
    else if (incomingData == "Reverse")
    {
      moveReverse();
    }
    else if (incomingData == "Turn Left")
    {
      turnLeft();
    }
    else if (incomingData == "Turn Right")
    {
      turnRight();
    }
    else
    {
      stopMotors();
    }
  }
}




// Function to move forward
void moveForward()
{
  gradualStart(Motor1Pin1, Motor2Pin1);
  delay(pulseDuration);
  gradualStop(Motor1Pin1, Motor2Pin1);
}




// Function to move in reverse
void moveReverse()
{
  gradualStart(Motor1Pin2, Motor2Pin2);
  delay(pulseDuration);
  gradualStop(Motor1Pin2, Motor2Pin2);
}




// Function to turn left
void turnLeft()
{
  gradualStart(Motor1Pin2, Motor2Pin1);
  delay(pulseDuration);
  gradualStop(Motor1Pin2, Motor2Pin1);
}




// Function to turn right
void turnRight()
{
  gradualStart(Motor1Pin1, Motor2Pin2);
  delay(pulseDuration);
  gradualStop(Motor1Pin1, Motor2Pin2);
}


void gradualStart(int pin1, int pin2)
{
  for (int speed = 0; speed <= maxMotorSpeed; speed += decelerationStep)
  {
    analogWrite(pin1, speed);
    analogWrite(pin2, speed);
    delay(decelerationDelay);
  }
}


void gradualStop(int pin1, int pin2)
{
  for (int speed = maxMotorSpeed; speed >= 0; speed -= decelerationStep)
  {
    analogWrite(pin1, speed);
    analogWrite(pin2, speed);
    delay(decelerationDelay);
  }
  analogWrite(pin1, 0);
  analogWrite(pin2, 0);
}


// Function to stop all motors
void stopMotors()
{
  analogWrite(Motor1Pin1, 0);
  analogWrite(Motor1Pin2, 0);
  analogWrite(Motor2Pin1, 0);
  analogWrite(Motor2Pin2, 0);
}
