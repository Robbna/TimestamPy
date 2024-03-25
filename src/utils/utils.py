import subprocess
import json
import os
from datetime import datetime, timedelta
import cv2
import sys


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def get_day_name(creation_date):
    days = {
        "Monday": "Monday",
        "Tuesday": "Tuesday",
        "Wednesday": "Wednesday",
        "Thursday": "Thursday",
        "Friday": "Friday",
        "Saturday": "Saturday",
        "Sunday": "Sunday",
    }
    day = creation_date.strftime("%A")
    return days[day]

def get_spanish_day_name(creation_date):
    spanish_days = {
        "Monday": "Lunes",
        "Tuesday": "Martes",
        "Wednesday": "Miércoles",
        "Thursday": "Jueves",
        "Friday": "Viernes",
        "Saturday": "Sábado",
        "Sunday": "Domingo",
    }
    day = creation_date.strftime("%A")
    return spanish_days[day]


def get_video_metadata(file_path):
    ffprobe_cmd = [
        resource_path(".\\libs\\ffprobe.exe"),
        "-v",
        "quiet",
        "-print_format",
        "json",
        "-show_format",
        "-show_streams",
        file_path,
    ]
    result = subprocess.run(ffprobe_cmd, capture_output=True, text=True)
    if result.returncode == 0:
        metadata = json.loads(result.stdout)
        return metadata
    else:
        print("Error al obtener los metadatos del video.")
        return {}


def get_formatted_creation_date(metadata):
    raw_creation_date = metadata["streams"][0]["tags"]["creation_time"]
    formatted_creation_date = datetime.fromisoformat(
        raw_creation_date.replace("Z", "+00:00")
    )
    return formatted_creation_date


def get_video_properties(cap):
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    return width, height, fps


def add_timestamp_to_frame(
    frame, frame_number, fps, height, font, color, spanish_day, creation_date
):
    frame_time = creation_date + timedelta(seconds=frame_number / fps)
    final_frame_time_str = frame_time.strftime("%d-%m-%Y %H:%M:%S")
    date_part, time_part = final_frame_time_str.split(" ")
    text_position = (20, height - 20)
    cv2.putText(
        frame,
        f"{spanish_day}, {date_part} {time_part}",
        text_position,
        font,
        1,
        color,
        2,
        cv2.LINE_4,
    )
