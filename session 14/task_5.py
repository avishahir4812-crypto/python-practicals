playlists = {
    "user1": {
        "Favourites": ["Song1", "Song2"]
    }
}

# Create user2 if it does not exist
if "user2" not in playlists:
    playlists["user2"] = {}

# Create Chill playlist if it does not exist
if "Chill" not in playlists["user2"]:
    playlists["user2"]["Chill"] = []

# Add Song3
playlists["user2"]["Chill"].append("Song3")

# Print complete playlists
print("Playlists:")
print(playlists)