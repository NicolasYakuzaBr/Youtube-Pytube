from pytube import YouTube
from pytube.cli import on_progress
import os

print('Youtube Vídeo Donwloader')
print('*******-------*********')
link = input('\nDigite o link do vídeo: ')
youtube = YouTube(link, on_progress_callback=on_progress)
stream = youtube.streams.get_audio_only()
file_name = stream.default_filename
folder_name = os.path.splitext(file_name)[0]

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
stream.download(output_path=folder_name)
print('\nDonwload Finalizado!')
















