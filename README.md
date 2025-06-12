# youtube-music-importer
Import music from a text file into youtube music. These scripts use the [ytmusicapi](https://github.com/sigma67/ytmusicapi) library to search for songs and add them to a playlist.
# Requirements
1. Song list in txt format (you can create one at https://tunemymusic.com/transfer , by selecting the "Export to file" option)
# Guide
1. Go to [Google Cloud Shell Editor](https://shell.cloud.google.com/?fromcloudshell=true&show=ide)
2. Clone this repo: `git clone https://github.com/c0lbarator/youtube-music-importer && cd youtube-music-importer`
3. Install ytmusicapi: `pip install ytmusicapi && export PATH=/home/YOUR_USERNAME/.local/bin`
4. Drag and drop the song list into the cloud shell, rename it to `songs.txt`.
5. Run the `mover.py` script. This script will find the video indexes of the songs in the list and store them in the `video_ids.txt` file.
6. [Authorize](https://ytmusicapi.readthedocs.io/en/stable/setup/oauth.html) and fill `client_id` and `client_secret` with your own values, rename the playlist
7. Run `adder.py`.
8. Now you have your own playlist on YT Music, enjoy!
