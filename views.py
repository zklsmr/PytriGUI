import numpy as np

from PyQt5.QtCore import Qt, QThread, QTimer
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QVBoxLayout, QApplication, QSlider
from pyqtgraph import ImageView


class StartWindow(QMainWindow):
    def __init__(self, camera = None):
        super().__init__()
        self.camera = camera

        self.central_widget = QWidget()
        self.button_frame = QPushButton('Take Pitcute', self.central_widget)
        self.button_save = QPushButton('Save Picture', self.central_widget)

        self.image_view = ImageView()

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.addWidget(self.button_frame)
        self.layout.addWidget(self.button_save)
        self.layout.addWidget(self.image_view)

        self.setCentralWidget(self.central_widget)

        self.button_frame.clicked.connect(self.update_image)
        self.button_save.clicked.connect(self.save_image)


        self.update_timer = QTimer()


    def update_image(self):
        frame = self.camera.get_frame()
        self.image_view.setImage(frame.T)
      
    def save_image(self):
        frame_to_save = self.camera.save_image()

        import datetime
        dt_image = datetime.datetime.now()
        import os
        pw = os.getcwd()
        fname = "Pytri" + str(dt_image)
        self.image_view.export(str(pw)+ "/"+fname+".png")


    def update_brightness(self, value):
        value /= 10
        self.camera.set_brightness(value)
