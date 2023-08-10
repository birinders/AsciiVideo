# AsciiVideo
## See (for) yourself on the terminal!
Run ```pip install -r requirements.txt``` to get started, or check out the C++ implementation here.

AsciiVideo--Py is a very simple project at heart-

Take what you see, and show it on the terminal. The project uses OpenCV library in order to convert anything your webcam captures from a series of colourful dots to a series of black and white letters. The program uses the cv2 module to capture data from any camera connected to your device, and then converts it into a b&w image. This allows us to index every pixel in this image array, and convert it into suitable ascii characters according to their brightness.

Eg- A pixel with high brightness value is converted to a character with a larger area, like $ or #, whereas darker characters might get converted to dots("."), commas(",") or even blank spaces (" ") if the pixel is too dim.

- Note-
The default behaviour is to choose the external camera before the built in camera. You can change this behaviour in the main.py file.

Ratio correction is an extremely important step for this project to work correctly. Since we know that characters are not equally wide, but are taller than they are wide, like a vertical rectangle, we need to account for this differnce factor in order to produce the outputs in the correct ratio.

<p>The above can be calculated using the following formula- <br>
  <p align = "center">
  <img src="https://github.com/birinders/AsciiVideo/assets/102192983/247c3ad2-fc3b-4ef1-80dc-d218b4cbaa9f" alt="Image Description" width = 300>
  </p>
</p>

The script will automatically check the aspect ratio of the incoming video stream, and readjust the output to match the input aspect ratio.

### And that's it! 
#### If everything has been set up correctly, you should now be seeing yourself on the terminal.
