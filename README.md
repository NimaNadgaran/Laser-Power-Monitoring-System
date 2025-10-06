# Gentec 310 Series Laser Power Monitor (Arduino + Python Visualization)

This project allows you to **read and visualize real-time laser power measurements** from a **Gentec 310 Series Laser Power Detector** using an **Arduino Mega** and **Python (Matplotlib)**.

Instead of relying on the Gentec device’s built-in display, this setup enables you to capture the analog output signal directly and display live readings on your computer as a dynamic plot.

---

## 🧠 Overview

The **Gentec 310 Series** provides an analog voltage signal proportional to the measured laser power.  
By connecting this signal to an Arduino’s analog input, the voltage can be sampled, converted into a power value, and sent to your computer via USB.  
Python then reads these values in real time and plots them using **Matplotlib**.

---

## ⚙️ Hardware Setup

### 🧩 Components
- Gentec 310 Series Laser Power Detector  
- Arduino Mega (or any Arduino with analog input support)  
- USB cable (for Arduino-PC connection)  
- Jumper wires

### 🔌 Connections

| Gentec Pin | Arduino Pin | Description              |
|-------------|--------------|--------------------------|
| Signal Out  | A0           | Analog power output      |
| GND         | GND          | Ground connection        |

> ⚠️ **Important:**  
> Ensure that the signal voltage from the Gentec sensor does not exceed **5V** (Arduino analog input limit).  
> If it does, use a voltage divider or signal conditioning circuit.

---

## 🧪 Calibration

To get accurate power readings, you must calibrate your system:

1. Check your Gentec 310 Series Manual (included in Gentec_310_Series_Manual.pdf) for your sensor’s responsivity (V/W). (In this case it was *0.130*)

2. Replace the value in this line in your Arduino code:
```
float power = voltage / 0.130;
```

with your actual sensitivity constant, e.g.:
```
float power = voltage / 0.145; // if your sensor’s responsivity is 0.145 V/W
```

3. Optionally, use a known laser power source and compare measured readings to fine-tune this constant.

4. For higher precision, you can also log data in Python and perform linear regression calibration.

## 💻 Software Requirements

- **Arduino IDE** (for uploading the code)
- **Python 3.x**
- **Required Python libraries:**
  ```bash
  pip install pyserial matplotlib

## 🚀 How to Run

1. Upload the Arduino sketch using Arduino IDE.

2. Connect the Gentec sensor’s signal and ground to the Arduino.

3. Run the Python script:
```
python python_inputGraph.py
```

4. Observe a live plot of your laser power over time.

##📁 Project Structure
```
Gentec_310_Series_Monitor/
├── Gentec_310_Series_Manual.pdf
├── README.md
├── arduino_readingSignal.ino
└── python_inputGraph.py
```

**Nima Nadgaran**
**💻 GitHub Profile: https://github.com/NimaNadgaran**
