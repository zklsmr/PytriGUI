import numpy as np

import cv2


class Camera:
    def __init__(self, cam_num):
        self.cam_num = cam_num
        self.cap = None
        self.last_frame = np.zeros((1,1))

    def initialize(self):
        self.cap = cv2.VideoCapture(self.cam_num)

    def get_frame(self):
        ret, self.last_frame = self.cap.read()
        return self.last_frame

    def save_image(self):
        import datetime
        dt_image = datetime.datetime.now()
        import os
        pw = os.getcwd()
        fname = "Pytri" + str(dt_image)
        self.image_view.export(str(pw)+ "/"+fname+".png")

    def close_camera(self):
        self.cap.release()

    def __str__(self):
        return 'OpenCV Camera {}'.format(self.cam_num)


if __name__ == '__main__':
    cam = Camera(0)
    cam.initialize()
    print(cam)
    frame = cam.get_frame()
    print(frame)

    cam.close_camera()