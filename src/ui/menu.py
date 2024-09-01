from src.utils.logger import Logger


class Menu:
    def get_user_font_choice(self, default_font, available_fonts):
        print(f"SELECT FONT. Default: 0 ({default_font})")
        for name, id in available_fonts:
            print(f"{id}. {name}")

        try:
            choice = int(input("> "))
            if 0 <= choice < len(available_fonts):
                return choice
        except Exception:
            Logger.log(f"Invalid input. Using default font: {default_font}", Logger.Severity.WARNING)
            return default_font
