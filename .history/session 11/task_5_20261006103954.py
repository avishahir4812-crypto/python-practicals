import random

songs = [
    "Kesariya",
    "Shape of You",
    "Believer",
    "Blinding Lights",
    "Perfect",
    "Levitating",
    "Senorita",
    "Despacito"
]

today_playlist = random.sample(songs, 3)

print("Today's Playlist:")

for song in today_playlist:
    print(song)