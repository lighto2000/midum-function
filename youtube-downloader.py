from pytube import YouTube
from termcolor import colored
path = 'C:\\Users\\Toshiba\\Desktop\\videos'
file = open('links.txt','r')

for link in file.readlines():
    try:
        video = YouTube(str(link))
        video.streams.filter(progressive=True).get_highest_resolution().download(output_path=path)
        print(colored(f'{video.title}  was  downloaded ','green'))
    except Exception as a:
        print(colored('download filed ','red'))
