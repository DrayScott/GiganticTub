import os
from mutagen import File
from mutagen.easyid3 import EasyID3
import shutil



unsorted_folder = "M:\\Music\\filtered"
sorted_folder = "M:\\Music\\Music"


for filename in os.listdir(unsorted_folder):
    if filename.endswith(('.mp3', '.flac', '.wav', '.aiff')):
        file_path = os.path.join(unsorted_folder, filename)
        print(f'Checking file {file_path} .... \n')

        #Open the file, easy allows for easy access of tags such as genre
        audio_data = File(file_path, easy=True)

        if audio_data:
            
            genre_data = audio_data.get('genre', ['Unknown']) #This will default to unknown
            
            if isinstance(genre_data, list) and len(genre_data) == 1:
                genres = [g.strip() for part in genre_data[0].split(',') for g in part.split(';') for g in part.split('/')] #split multiple genres, by some common separaters
            else: 
                genres = genre_data 

            print(f'{filename} sounds like it will fit best in the {genres[0]} category, let me move it for you!\n')

            dst_folder = os.path.join(sorted_folder, genres[0])

            #Create a Folder for that genre if it doesn't exist 
            os.makedirs(dst_folder, exist_ok=True)
            shutil.move(file_path, dst=dst_folder)
            print(f'Alright, {filename} has a new home in {dst_folder} \n')


        else:
            print(f'Unfortunately, I could get the meta data for {filename}')


print("Finished sorting all your new Tunes! Come back when you have more \n")


