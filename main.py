import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')
SCOPES = "user-library-read user-library-modify"

def get_all_songs_from_albums(client):
    songs = []
    max_albums = 50
    offset = 0
    next_exists = True

    while next_exists:
        albums = client.current_user_saved_albums(limit=max_albums, offset=offset)

        for album in albums.get("items"):
            songs += [track.get("uri") for track in album.get("album").get("tracks").get("items")]
        offset += max_albums

        next_exists = bool(albums.get("next"))

    return songs

def batch(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]

def like_unliked_songs(client, songs):
    processed = 0
    for b in batch(songs, n=50):
        truth_array = client.current_user_saved_tracks_contains(b)
        songs_to_like = [b[i] for i in range(len(b)) if not truth_array[i]]
        if len(songs_to_like) > 0:
            client.current_user_saved_tracks_add(songs_to_like)

        processed += len(b)
        print(f'Processed {processed} / {len(songs)}')

    print('Proccessing complete.')
    return songs_to_like

def main():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPES))
    songs = get_all_songs_from_albums(sp)
    like_unliked_songs(sp, songs)

if __name__ == '__main__':
    main()
