void setup() {
    Serial.begin(9600); // Start serial communication at 9600 baud rate for Arduino to PC communication
}

void loop() {
    int sensorValue = analogRead(A0);  // Read the analog value from the laser power detector sensor
    float voltage = sensorValue * (5.0 / 1023.0); // Convert ADC value to voltage (assuming a 5V reference voltage)
    float power = voltage / 0.130;  // Convert voltage to power based on the sensor's sensitivity (0.130 is a placeholder for calibration value)

    // Send the power value over serial to the PC, which will read and plot the data
    Serial.println(power);  // Send the power value to the PC
    delay(50);  // Delay for 50 milliseconds before taking the next reading
}
