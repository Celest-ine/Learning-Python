def make_album(artist_name, album_title):
    """A function that returns a dictionary describing an album."""

    music_album = {'artist': artist_name, 'album': album_title}
    return music_album

print("Enter an artist name and their album")
print("Enter q to quit at any time.")
while True:

    artist_n = input("Artist name: ")
    if artist_n.lower() == 'q':
        break

    album_t = input("Album name: ")
    if album_t.lower() == 'q':
        break
    the_music_album = make_album(artist_n.title(), album_t.title())
    print(the_music_album)