from playlist import add_song, remove_song

playlist = []

add_song("Kesariya", playlist)
add_song("Shape of You", playlist)
add_song("Believer", playlist)

print("Before Removing:", playlist)

remove_song("Shape of You", playlist)

print("After Removing:", playlist)