import os
import winreg
from src.utils.logger import Logger


class FontService:

    WINDOWS_REGISTRY_PATH = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts"

    def find_font_file(self, font_name):
        font_path = self.__find_font_in_registry(font_name)
        if not font_path:
            font_path = self.__find_font_in_user_directory(font_name)

        if font_path:
            Logger.log(f"Font path found: {font_path}", Logger.Severity.SUCCESS)
            return font_path
        else:
            print("Font not found.")

    def __find_font_in_registry(self, font_name):
        with winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE, FontService.WINDOWS_REGISTRY_PATH
        ) as key:
            try:
                i = 0
                while True:
                    value_name, value_data, _ = winreg.EnumValue(key, i)
                    if font_name.lower() in value_name.lower():
                        return os.path.join(os.environ["WINDIR"], "Fonts", value_data)
                    i += 1
            except WindowsError:
                pass
        return None

    def __find_font_in_user_directory(
        self, font_name, user_directory=os.path.expanduser("~")
    ):
        possible_paths = [
            os.path.join(
                user_directory, "AppData", "Local", "Microsoft", "Windows", "Fonts"
            ),
        ]
        for path in possible_paths:
            for root, dirs, files in os.walk(path):
                for file in files:
                    if font_name.lower() in file.lower() and file.endswith(
                        (".ttf", ".otf")
                    ):
                        return os.path.join(root, file)
        return None
