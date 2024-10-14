#include <Servo.h>         // Load the Servo library
#include <Ultrasonic.h>    // Load the Ultrasonic distance measurement library (HC-SR04)

#define LDR_PIN A0
#define ULTRASONIC_TRIGGER_PIN 12
#define ULTRASONIC_ECHO_PIN 13
#define PROXIMITY_PIN 2
#define SERVO_PIN_1 4
#define SERVO_PIN_2 6

// Define LDR threshold values
#define LDR_THRESHOLD_PAPER 9
#define LDR_THRESHOLD_PLASTIC_LOWER 10
#define LDR_THRESHOLD_PLASTIC_UPPER 20

Ultrasonic ultrasonic(ULTRASONIC_TRIGGER_PIN, ULTRASONIC_ECHO_PIN);
Servo servo1, servo2;

void setup() {
  servo1.attach(SERVO_PIN_1);
  servo2.attach(SERVO_PIN_2);

  Serial.begin(9600);
  pinMode(PROXIMITY_PIN, INPUT); // Set inductive proximity switch to input mode
  moveServos(90, 90);
}

void loop() {
  int distance = ultrasonic.read();
  int proximitySensorValue = digitalRead(PROXIMITY_PIN);
  int ldrValue = analogRead(LDR_PIN);

  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.print(" cm, Proximity: ");
  Serial.print(proximitySensorValue);
  Serial.print(", LDR: ");
  Serial.println(ldrValue);

  delay(500);

  if (proximitySensorValue == LOW) {
    // Proximity sensor is low, print "Not Metal"
    Serial.println("Not Metal");
    servo1.write(0);
    delay(500);
    servo1.write(90);
    delay(500);

    if (distance <= 5) {
      if (ldrValue <= LDR_THRESHOLD_PAPER) {
        // Detected paper - move right from the back
        Serial.println("Paper detected");
        servo2.write(180);
        delay(500);
        servo2.write(90);
        delay(500);
      } else if (ldrValue >= LDR_THRESHOLD_PLASTIC_LOWER && ldrValue <= LDR_THRESHOLD_PLASTIC_UPPER) {
        // Detected plastic - move left from the back
        Serial.println("Plastic detected");
        servo2.write(0);
        delay(500);
        servo2.write(90);
        delay(500);
      } else {
        Serial.println("No valid LDR range detected");
      }
    } else {
      servo1.write(90);
      printSensorValues(distance, ldrValue, proximitySensorValue);
    }
  } else {
    // Proximity sensor is high, print "Metal"
    Serial.println("Metal");
    servo1.write(180);
    delay(500);
    servo1.write(90);
    delay(500);
  }
}

void moveServos(int angle1, int angle2) {
  servo1.write(angle1);
  servo2.write(angle2);
}

void printSensorValues(int distance, int ldrValue, int proximitySensorValue) {
  Serial.print("Distance in CM: ");
  Serial.println(distance);

  Serial.print("LDR Value: ");
  Serial.println(ldrValue);

  if (proximitySensorValue == LOW) {
    Serial.println("No Object");
  } else {
    Serial.println("Object Detected");
  }

  delay(2000);
}
