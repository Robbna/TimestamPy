from src.view.MainWindow import MainWindow
from src.services.FontService import FontService

import os
import winreg


if __name__ == "__main__":
    window = MainWindow()
    # font_service = FontService()
    
    # font_file_name = font_service.find_font_file("Arial")
    
    # print(font_file_name)
    # font_file_name = find_font_file("Arial")
    # if font_file_name:
    #     print(f"Found font file: {font_file_name}")
    #     font_path = os.path.join(os.environ['WINDIR'], 'Fonts', font_file_name)
    #     print(f"Assumed full path: {font_path}")
    # else:
    #     print("Font not found.")
