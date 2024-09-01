import os
from src.utils.logger import Logger


class FilesService:

    def __init__(self):
        pass

    def find_mp4_files(self):
        Logger.log("Searching mp4 files in current directory", Logger.Severity.INFO)
        video_files = [f for f in os.listdir() if f.lower().endswith(".mp4")]
        if not video_files:
            Logger.log("No video files found in current directory.", Logger.Severity.WARNING)
            return None
        Logger.log(f"\nFound {len(video_files)} video files.", Logger.Severity.SUCCESS)
        Logger.log(f"Video files found: {video_files}", Logger.Severity.INFO)
        return video_files
