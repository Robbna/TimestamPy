import os
import cv2
from moviepy.editor import VideoFileClip
from ..utils import utils
from ..utils.colors import colors

# Definición de constantes para fuentes disponibles y nombres predeterminados.
DEFAULT_FONT_NAME = "hershey_simplex"
DEFAULT_FONT_VALUE = cv2.FONT_HERSHEY_SIMPLEX
FONTS_AVAILABLE = {
    "hershey_simplex": cv2.FONT_HERSHEY_SIMPLEX,
    "hershey_plain": cv2.FONT_HERSHEY_PLAIN,
    "hershey_duplex": cv2.FONT_HERSHEY_DUPLEX,
    "hershey_complex": cv2.FONT_HERSHEY_COMPLEX,
    "hershey_triplex": cv2.FONT_HERSHEY_TRIPLEX,
    "hershey_complex_small": cv2.FONT_HERSHEY_COMPLEX_SMALL,
    "hershey_script_simplex": cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
    "hershey_script_complex": cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
}


def process_video(video_file, font, color, language):
    video_metadata = utils.get_video_metadata(video_file)
    video_name = os.path.splitext(video_file)[0]

    if not video_metadata:
        print(
            f"{colors.WARNING}[WARNING]{colors.ENDC} Video metadata not found! Skipping..."
        )
        return

    original_bitrate = video_metadata["format"]["bit_rate"]

    try:
        creation_date = utils.get_formatted_creation_date(video_metadata)
        
        day_name = utils.get_day_name(creation_date)
        
        if language == "spanish":
            day_name = utils.get_spanish_day_name(creation_date)
        
    except KeyError:
        print(
            f"{colors.WARNING}[WARNING]{colors.ENDC} Creation date not found in metadata! Skipping..."
        )
        return

    cap = cv2.VideoCapture(video_file)
    width, height, fps = utils.get_video_properties(cap)
    out = cv2.VideoWriter(
        f"{video_name}_temp.mp4", cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height)
    )

    add_timestamp_to_frames(
        cap, out, height, font, color, day_name, creation_date, fps
    )

    original_audio = extract_audio_from_original(video_file)
    save_final_video_with_audio(
        f"{video_name}_temp.mp4", video_name, original_audio, original_bitrate
    )


def add_timestamp_to_frames(
    cap, out, height, font, color, spanish_day, creation_date, fps
):
    frame_number = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_number += 1
        utils.add_timestamp_to_frame(
            frame, frame_number, fps, height, font, color, spanish_day, creation_date
        )
        out.write(frame)
    cap.release()
    out.release()
    cv2.destroyAllWindows()


def extract_audio_from_original(video_file):
    original_video = VideoFileClip(video_file)
    return original_video.audio


def save_final_video_with_audio(temp_video_path, video_name, audio, original_bitrate):
    edited_video = VideoFileClip(temp_video_path).set_audio(audio)
    final_video_path = f"{video_name}_timestamp.mp4"
    edited_video.write_videofile(
        final_video_path,
        codec="libx264",
        audio_codec="aac",
        bitrate=f"{int(original_bitrate)/1369}k",
    )
    os.remove(temp_video_path)
    print(
        f"{colors.OKGREEN}[INFO]{colors.ENDC} Final video saved successfully at {final_video_path}!"
    )
