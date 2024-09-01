from datetime import timedelta
import os
import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from moviepy.editor import VideoFileClip
from ..utils import utils
from ..utils.colors import Colors

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
            f"{Colors.WARNING}[WARNING]{Colors.ENDC} Video metadata not found! Skipping..."
        )
        return

    original_bitrate = video_metadata["format"]["bit_rate"]
    original_audio = VideoFileClip(video_file)
    original_video = cv2.VideoCapture(video_file)
    
    try:
        creation_date = utils.get_formatted_creation_date(video_metadata)
        day_name = utils.get_day_name(creation_date)

        if language == "spanish":
            day_name = utils.get_spanish_day_name(creation_date)

    except KeyError:
        print(
            f"{Colors.WARNING}[WARNING]{Colors.ENDC} Creation date not found in metadata! Skipping..."
        )
        return

    width, height, fps = utils.get_video_properties(original_video)
    
    temporal_video_name = f"{video_name}_temp.mp4"
    temporal_video = cv2.VideoWriter(
        temporal_video_name, cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height)
    )

    add_timestamp_to_frames(original_video, temporal_video, height, font, color, day_name, creation_date, fps)
    
    save_final_video_with_audio(
        temporal_video_name, video_name, original_audio, original_bitrate
    )


def add_timestamp_to_frames(videoCapture, out, height, font, color, day, creation_date, fps):
    frame_number = 0
    font_size = 50
    margin = 15

    text_position = (margin + (margin / 2), (height - font_size) - margin)

    while videoCapture.isOpened():
        ret, frame = videoCapture.read()
        if not ret:
            break
        frame_number += 1

        frame_time = creation_date + timedelta(seconds=frame_number / fps)
        final_frame_time_str = frame_time.strftime("%d-%m-%Y %H:%M:%S")
        date_part, time_part = final_frame_time_str.split(" ")

        text = f"{day}, {date_part} {time_part}"

        img_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(img_pil)
        font = ImageFont.truetype(
            # utils.resource_path(".\\assets\\fonts\\pixelart_1.ttf"), font_size
            utils.resource_path(".\\assets\\fonts\\VCR_OSD_MONO_1.001.ttf"), font_size
        )

        draw.text(text_position, text, font=font, fill=color)

        edited_frame = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

        out.write(edited_frame)
    videoCapture.release()
    out.release()
    cv2.destroyAllWindows()


def save_final_video_with_audio(temp_video_name, original_video_name, audio, bitrate):
    edited_video = VideoFileClip(temp_video_name).set_audio(audio)
    final_video_path = f"{original_video_name}_timestamp.mp4"
    edited_video.write_videofile(
        final_video_path,
        codec="libx264",
        audio_codec="aac",
        bitrate=f"{int(bitrate)/1369}k",
    )
    os.remove(final_video_path)
    print(
        f"{Colors.OKGREEN}[INFO]{Colors.ENDC} Final video saved successfully at {final_video_path}!"
    )
