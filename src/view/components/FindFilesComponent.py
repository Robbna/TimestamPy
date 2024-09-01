from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class FindFilesComponent:
  def __init__(self):
    self.video_files = []
    pass
  
  def build(self):
    scan_button = QPushButton("Scan mp4 files")
    scan_button.clicked.connect(self.__find_mp4_files)
    return scan_button
  
  def __find_mp4_files(self):
    pass