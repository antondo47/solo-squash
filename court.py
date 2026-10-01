import numpy as np
import cv2

# court calibration per UPLOAD
# A homography is a mathematical transformation that maps points from one flat surface (plane) to another
def build_homography(pixel_points, court_points):
    """4 clicked pixel points + known court coords -> homography H."""
    H, _ = cv2.findHomography(np.float32(pixel_points), np.float32(court_points))
    return H

def make_pixel_to_court(H): 
    # return a FUNCTION. Put in a pixel location (px, py) -> gives back a court location (court_x, court_y)
    # give it the pixel at the player's feet
    def pixel_to_court(px, py):
        pt = np.array([[[px, py]]], dtype=np.float32)
        result = cv2.perspectiveTransform(pt, H)
        x, y = result[0][0]
        return float(x), float(y)
    return pixel_to_court

# get the 4 points
if __name__ == "__main__":
    points = []
    # handle the click
    def mouse_click(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            points.append((x, y))
            print(f"point {len(points)}: ({x}, {y})") # to see the current point in terminal
            cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
            cv2.imshow("calibrate", frame) # show the dot that appears

    # grab a frame
    cap = cv2.VideoCapture("squashtung1.mp4")
    ret, frame = cap.read()
    cap.release() # close the video

    if not ret: 
        print("Error: cant read the frame")
    else:
        cv2.imshow("calibrate", frame)
        cv2.setMouseCallback("calibrate", mouse_click) # to capture mouse events on a specific display window and pass them to a custom function
        # keep the window alive until 4 points are collected
        while len(points) < 4:
            if cv2.waitKey(1) & 0xFF == ord('q'):   # press q to give up early
                break
        cv2.destroyAllWindows() # clean up
        print("all points: ", points)


