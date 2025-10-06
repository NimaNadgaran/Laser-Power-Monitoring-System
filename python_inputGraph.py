import serial  # Import the serial library to communicate with the Arduino
import matplotlib.pyplot as plt  # Import the matplotlib library to plot data

# Initialize the serial connection to your Arduino
ser = serial.Serial('COM9', 9600)  # Replace 'COM9' with the correct serial port for your Arduino

# Initialize lists to store x (time) and y (power) values for the plot
x_values = []
y_values = []

# Set up the plot window
plt.ion()  # Enable interactive mode to update the plot in real-time
fig, ax = plt.subplots(figsize=(8, 6))  # Create a new plot window with a specific size
ax.set_xlim(0, 10)  # Set the x-axis range (time in seconds)
ax.set_ylim(0, 10)  # Set the y-axis range (power values from the Arduino)
ax.set_xlabel('Time (s)')  # Label for the x-axis
ax.set_ylabel('Power (W)')  # Label for the y-axis
ax.set_title('Laser Power Over Time')  # Title of the plot
plt.grid(True)  # Enable grid for easier visualization

# Initialize time variable
time = 0

# Infinite loop to continuously read data from the Arduino and update the plot
while True:
    try:
        # Read the incoming data from the Arduino, decode it, and convert it to a float
        y_input = round(float(ser.readline().decode('utf-8').strip()), 2)
        print(y_input)  # Print the current power value for debugging purposes
    except ValueError:
        # If the data cannot be converted to a float, skip this iteration
        print("Received non-numeric data, skipping this iteration")
        continue  # Skip to the next iteration if the data is not a number

    # Append the current time and power to the respective lists
    x_values.append(time)  # Add the current time to the x-values list
    y_values.append(y_input)  # Add the current power reading to the y-values list

    time = time + 0.050  # Increment the time by 50 milliseconds for the next reading

    # Update the plot with the new data
    ax.cla()  # Clear the current plot
    ax.plot(x_values, y_values, 'bo-', label='Laser Power')  # Plot the data points (blue circles)

    # Redraw the plot with updated labels, title, and grid
    ax.set_xlim(0, int(time) + 3)  # Update the x-axis range
    ax.set_ylim(0, 1)  # Update the y-axis range (assumes power values are between 0 and 1)
    ax.set_xlabel('Time (s)')  # Redraw the x-axis label
    ax.set_ylabel('Power (W)')  # Redraw the y-axis label
    ax.set_title('Laser Power Over Time')  # Redraw the title
    ax.grid(True)  # Redraw the grid
    ax.legend()  # Add a legend

    plt.draw()  # Redraw the plot
    plt.pause(0.001)  # Pause briefly to update the plot in interactive mode

# After the loop ends, turn off interactive mode and keep the plot open
plt.ioff()  # Turn off interactive mode
plt.show()  # Display the plot

# Close the serial connection when the program ends
ser.close()  # Close the serial port connection
