from pytube import YouTube

url = "https://www.youtube.com/watch?v=PdwwNKwjxXI"

youtube_video = YouTube(url)

print("Titre :", youtube_video.title)
print("Auteur :", youtube_video.author)
print("Description :", youtube_video.description)
print("Sous-titres :", youtube_video.captions)
print("Vues :", youtube_video.views)