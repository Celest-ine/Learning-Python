def make_album(artist_name, album_title, songs=None):
    """A function that returns a dictionary describing an album."""

    music_album = {
        'artist': artist_name.title(),
        'album': album_title.title()
        }
    
    if songs is not None:
        music_album['songs'] = songs
    return music_album
    
lemonade_album = make_album('beyonce', 'lemonade', 5)
planet_her_album = make_album('doja cat', 'planet her', 5)
anti_album = make_album('rihanna', 'anti')

print(lemonade_album)
print(planet_her_album)
print(anti_album)