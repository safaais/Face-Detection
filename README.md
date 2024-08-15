# Face-Detection

These steps guide you through creating a Flask web application that performs real-time face detection
## Set Up the Environment
### Install Dependencies: Ensure you have Python and the necessary libraries installed:
•	Flask: Web framework for Python.
•	OpenCV: Library for computer vision tasks.
•	NumPy: Library for numerical operations.
```
pip install Flask opencv-python numpy
```


## Create the Flask Application
### Initialize Flask: Create a new Python file (e.g., app.py) and initialize a Flask app.

### Configure File Uploads: Set up a directory for uploaded files and define a maximum file size for uploads.

### Load the Haar Cascade: Load a pre-trained Haar Cascade classifier for face detection.


## Define the Video Feed Function

### Capture Video: Write a function (generate_frames) to capture video frames from the webcam using OpenCV.

### Face Detection: Inside the function, convert each frame to grayscale and apply the face detection algorithm. Draw rectangles around detected faces with user-defined colors and parameters.

### Stream Video: Encode the processed frames and yield them as a continuous stream.


##  Set Up Routes

### Home Route: Create a route (/) that renders the main HTML template for the user interface.

### Video Feed Route: Create a route (/video_feed) that streams the video feed by calling the generate_frames function.

      
##  Create the HTML Template

### Design the UI: Create an HTML file (e.g., index.html) that includes:

•	A title and header.

•	Dropdowns for selecting rectangle color, scale factor, and minimum neighbors for face detection.


•	An <img> tag to display the video feed.


### Responsive Design: Use CSS to style the page and ensure it is responsive for different screen sizes.


## Add Interactivity

### JavaScript Functions: Include JavaScript functions to handle changes in the dropdown selections. When a user selects an option, the page reloads with the new parameters.

## Run the Application:

### Start the Server: Run the Flask application using:

```
python app.py
```

![image alt](https://github.com/safaais/Face-Detection/blob/654e728912fb5833de1a05d066fa52fb4e93e07b/Screenshot%202024-08-15%20231230.png)


### Problem in Testing:

We have to allow the application to access your webcam and test the face detection feature by observing the rectangles drawn around faces in the video feed.
