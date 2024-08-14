import yt_dlp

URL = 'https://youtu.be/EsHQB9gT96k?si=xOVGl0GOpbTt2zU6'
DIR = 'C:\Users\Youtube'    

ydl_opts_video = {
    'format': 'bestvideo[ext=mp4][height<=2160]', 
    'outtmpl': f'{DIR}/video.mp4',
}

try:
    with yt_dlp. YoutubeDL (ydl_opts_video) as ydl:
        info_dict_audio = ydl.extract_info(URL, download=True)
        video_itag = info_dict_audio.get("format_id", None)
        print(f"Audio downloaded: {DIR}\\audio.mp4")
        print(f"Audio itag: (audio_itag)")
except Exception as e:
    print(f"An unexpected error occurred while downloading audio: {e}")

ydl_opts_audio = {
    'format': 'bestaudio[ext=mp4]',
    'outtmpl': f'{DIR}/audio.mp4',
}

try:
    with yt_dlp.YoutubeDL (ydl_opts_audio) as ydl:
        info_dict_audio = ydl.extract_info(URL, download=True)
        audio_itag = info_dict_audio.get("format_id", None)
        print(f"Audio downloaded: {DIR}\\audio.mp4")
        print(f"Audio itag: {audio_itag}")
except Exception as e:
    print(f"An unexpected error occurred while downloading audio: {e}")