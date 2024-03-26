import os
import time
import random
import src.services.VideoService as VideoService
from src.utils.colors import colors, rgb_colors


class VideoProcessor:
    def __init__(self):
        self.video_files = self.find_mp4_files()
        self.selected_font = self.get_user_font_choice()
        self.rgb_color = self.get_user_color_choice()
        self.language_selected = self.get_language_choice()
        self.process_directory_videos()

    def get_user_font_choice(self):
        self.print_separator()
        print(f"SELECT FONT. Default: 0 ({VideoService.DEFAULT_FONT_NAME})")
        print()
        [print(f"{id}. {name}") for name, id in VideoService.FONTS_AVAILABLE.items()]
        return self.prompt_font_selection()

    def get_language_choice(self):
        self.print_separator()
        print(f"SELECT LANGUAGE. Default: 0 (English)")
        print()
        print(f"0. English")
        print(f"1. Spanish")
        print()

        try:
            choice = int(input("> "))
            if choice == 1:
                return "spanish"
        except ValueError:
            pass

        return "english"

    def get_user_color_choice(self):
        self.print_separator()
        print(f"SELECT COLOR. Default: 0 (White)")
        print()
        print(f"0. White")
        print(f"1. {colors.BOLD}Black{colors.ENDC}")
        print(f"2. {colors.RED}Red{colors.ENDC}")
        print(f"3. {colors.GREEN}Green{colors.ENDC}")
        print(f"4. {colors.BLUE}Blue{colors.ENDC}")
        print("5. Custom RGB")
        print()

        try:
            choice = int(input("> "))
            if 0 <= choice < 5:
                return rgb_colors.COLORS[choice]
            if choice == 5:
                return self.prompt_color_selection()
        except ValueError:
            pass

        print(
            f"{colors.BOLD}{colors.WARNING}[WARNING]{colors.ENDC} Invalid input. Using default color: white"
        )
        return rgb_colors.COLORS[0]

    def prompt_color_selection(self):
        print()
        print("Enter RGB values (0-255) separated by commas (e.g. 255,0,0 for red): ")
        print()
        try:
            rgb = input("> ").split(",")
            if len(rgb) == 3:
                return tuple(map(int, rgb))
        except ValueError:
            pass

        print(
            f"{colors.BOLD}{colors.WARNING}[WARNING]{colors.ENDC} Invalid input. Using default color: white"
        )
        return (255, 255, 255)

    def prompt_font_selection(self):
        try:
            print()
            choice = int(input("> "))
            if 0 <= choice < len(VideoService.FONTS_AVAILABLE):
                return choice
        except ValueError:
            pass
        print(
            f"{colors.BOLD}{colors.WARNING}[WARNING]{colors.ENDC} Invalid input. Using default font: {VideoService.DEFAULT_FONT_NAME}"
        )
        return VideoService.DEFAULT_FONT_VALUE

    def process_directory_videos(self):

        if self.video_files:
            [
                self.process_video(file, language=self.language_selected)
                for file in self.video_files
            ]
        else:
            print(
                f"{colors.BOLD}{colors.WARNING}[WARNING]{colors.ENDC} No video files found."
            )

    def print_dot_animation(self):
        for _ in range(random.randint(2, 5)):
            for _ in range(3):
                print(".", end="", flush=True)
                time.sleep(0.6)
            print("\b\b\b   \b\b\b", end="", flush=True)
        print("...", end="", flush=True)

    def find_mp4_files(self):
        print()
        print(
            f"{colors.BOLD}{colors.OKBLUE}[INFO]{colors.ENDC} Searching mp4 files in current directory",
            end="",
            flush=True,
        )
        self.print_dot_animation()
        print()
        video_files = [f for f in os.listdir() if f.lower().endswith(".mp4")]
        time.sleep(random.randint(1, 3))
        if not video_files:
            print(
                f"{colors.BOLD}{colors.WARNING}[WARNING]{colors.ENDC} No video files found in current directory."
            )
            exit()
        print(
            f"{colors.BOLD}{colors.OKGREEN}[SUCCESS]{colors.ENDC} Found {len(video_files)} video files."
        )
        print(
            f"{colors.BOLD}{colors.OKBLUE}[INFO]{colors.ENDC} Video files found: {video_files}"
        )
        time.sleep(random.randint(1, 2))
        print()
        return video_files

    def process_video(self, file_name, language):
        self.print_separator()
        print(
            f"{colors.BOLD}{colors.OKBLUE}[INFO]{colors.ENDC} Processing video: {file_name}..."
        )
        try:
            VideoService.process_video(
                file_name,
                language=language,
                font=self.selected_font,
                color=self.rgb_color,
            )
        except Exception as e:
            print(
                f"{colors.BOLD}{colors.FAIL}[ERROR]{colors.ENDC} Failed to process video: {file_name}\nError: {e}"
            )
        self.print_separator()

    def print_separator(self):
        print("=====================================")


if __name__ == "__main__":
    print(
        """
████████╗██╗███╗   ███╗███████╗███████╗████████╗ █████╗ ███╗   ███╗██████╗ ██╗   ██╗
╚══██╔══╝██║████╗ ████║██╔════╝██╔════╝╚══██╔══╝██╔══██╗████╗ ████║██╔══██╗╚██╗ ██╔╝
   ██║   ██║██╔████╔██║█████╗  ███████╗   ██║   ███████║██╔████╔██║██████╔╝ ╚████╔╝ 
   ██║   ██║██║╚██╔╝██║██╔══╝  ╚════██║   ██║   ██╔══██║██║╚██╔╝██║██╔═══╝   ╚██╔╝  
   ██║   ██║██║ ╚═╝ ██║███████╗███████║   ██║   ██║  ██║██║ ╚═╝ ██║██║        ██║   
   ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝        ╚═╝   

                                                                        Version: 1.1.0
Author: @Robbna
Repository: https://github.com/Robbna/TimestamPy
"""
    )
    VideoProcessor()
    input("Press any key to exit...")
