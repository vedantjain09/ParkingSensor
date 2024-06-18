from flask import Flask, render_template
import threading
import socket

app = Flask(__name__)

# Global variables to store the latest distance and alert message
latest_distance = "Waiting for data..."
alert_message = ""  # Empty when there is no alert
# List to store the last N distances for moving average calculation
distances = []
# Number of measurements to consider for the moving average
MOVING_AVERAGE_WINDOW = 5


def receive_data():
    global latest_distance, alert_message, distances
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Replace '192.168.1.48' with the actual server IP address
    s.connect(('192.168.1.48', 12346))

    try:
        while True:
            data = s.recv(1024).decode()
            if not data:
                print("No more data received.")
                break
            try:
                distance = float(data)
                distances.append(distance)
                if len(distances) > MOVING_AVERAGE_WINDOW:
                    distances.pop(0)  # Remove the oldest distance

                if len(distances) == MOVING_AVERAGE_WINDOW:
                    smoothed_distance = sum(distances) / MOVING_AVERAGE_WINDOW
                    latest_distance = f"{smoothed_distance:.2f} cm"  # Update latest distance
                    if smoothed_distance < 2.0:  # Check if too close
                        alert_message = "TOO CLOSE"
                    else:
                        alert_message = ""
            except ValueError:
                print("Invalid data received:", data)
            print("Received:", data)
    finally:
        s.close()
        print("Connection closed.")


@app.route('/')
def index():
    return render_template('index2.html', distance=latest_distance, alert=alert_message)


if __name__ == '__main__':
    # Starting the background thread to receive data from the server
    thread = threading.Thread(target=receive_data)
    thread.daemon = True  # Daemonize thread
    thread.start()

    # Run the Flask app
    app.run(host='0.0.0.0', port=3500, debug=False)
