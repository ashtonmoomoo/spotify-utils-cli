# spotify-utils-cli
Spotify "Utils" but for CLI. BYO API keys

## Usage
- Get a developer account on Spotify (it's free if you have a premium account already - not sure otherwise)
- Create a Spotify App to get some API keys.
- In the overview for the app click `Edit Settings` and under `Redirect URIs` add `https://localhost:5000`, click save
- Clone this repo somewhere
- Open a terminal in the folder that `main.py` is in, and run the following commands:
- `export SPOTIFY_CLIENT_ID='your app client id'`
- `export SPOTIFY_CLIENT_SECRET='your app secret'`
- (assuming you already have Python installed) run `pip3 install spotipy`
- When that finishes run `python3 main.py` and you're off to the races (probably)