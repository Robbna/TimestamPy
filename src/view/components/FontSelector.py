from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class FontSelector(QPushButton):
  def __init__(self, text, fonts, onClick):
    super().__init__(text)
    self.setStyleSheet("font-family: 'Arial'; font-size: 20px; border: 10px solid red;")
    self.text = text
    self.fonts = fonts
    self.parent_click = onClick
    self.clicked.connect(self.__on_click)
    
  def __on_click(self):
    self.parent_click(self.fonts)