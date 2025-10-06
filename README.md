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

## 💻 Software Requirements

- **Arduino IDE** (for uploading the code)
- **Python 3.x**
- **Required Python libraries:**
  ```bash
  pip install pyserial matplotlib

##📁 Project Structure
```
Gentec_310_Series_Monitor/
├── Gentec_310_Series_Manual.pdf
├── README.md
├── arduino_readingSignal.ino
└── python_inputGraph.py
```
