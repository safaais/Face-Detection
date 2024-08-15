

import os
import cv2
import numpy as np
from flask import Flask, render_template, Response, request

app = Flask(__name__)

# Configure file uploads
app.config['UPLOAD_FOLDER'] = 'uploads'  # Create a 'uploads' folder to store images
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Set a maximum file size (16MB)

# Load the pre-trained face detector
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def generate_frames():
    """Captures video frames and detects faces."""
    camera = cv2.VideoCapture(0)  # Access your webcam
    if not camera.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        success, frame = camera.read()  # Grab a frame from the camera
        if not success:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

        # Get user-selected options
        color = request.args.get('color', 'green')
        scale_factor = float(request.args.get('scale_factor', '1.1'))
        min_neighbors = int(request.args.get('min_neighbors', '3'))

        # Detect faces with user-selected parameters
        faces = face_cascade.detectMultiScale(gray, scale_factor, min_neighbors)

        # Draw rectangles around the faces with the selected color
        for (x, y, w, h) in faces:
            if color == 'green':
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            elif color == 'red':
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            elif color == 'blue':
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        ret, buffer = cv2.imencode('.jpg', frame)  # Encode the frame
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    camera.release()
    cv2.destroyAllWindows()

@app.route('/')
def index():
    """Renders the HTML template."""
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    """Returns the video feed."""
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)