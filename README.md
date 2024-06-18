# Distance Monitoring System (Parking Sensor)

## Team Members
- Vedant Jain
- Jacob Rojit

## Overview
This project consists of a Flask web application that displays real-time distance measurements. The data is smoothed using a moving average method to provide a stable reading. The system alerts the user when the measured distance is "TOO CLOSE" (under 2 cm).

## Installation and Execution Instructions

### Prerequisites
- Python 3.x
- Flask
- Any operating system (Windows, macOS, Linux)
- Raspberry Pi with Dexter (GrovePi) installed

### Setup and Running
1. Ensure Python 3.x is installed on your system.
2. Install Flask using pip: pip install Flask
3. To run the server, navigate to the directory containing `server.py` on the raspberry pi and execute: python server.py
4. To run the client, navigate the directory containing 'client.py' and execute: python client.py
5. Open a web browser and access the application at: http://localhost:3400


### External Libraries
- Flask: Used for creating the web server and handling HTTP requests.
- GrovePi: Reading data from sensors connected to the Raspberry Pi
- Sockets: For server/client handling
- Threading: To handle simultaneous data reception and web serving without blocking
- Time: Manage polling intervals



