from ytmusicapi import YTMusic, OAuthCredentials

ytmusic = YTMusic('oauth.json', oauth_credentials=OAuthCredentials(client_id="CLIENT_ID_HERE", client_secret="CLIENT_SECRET_HERE"))
music_ids = []
with open("video_ids.txt", 'r') as f:
            for line in f:
                line = line.strip()
                if line and line != "None":
                    music_ids.append(line)
print(len(music_ids))
playlist = ytmusic.create_playlist(title="PLAYLIST_TITLE",description="DESCRIPTION", video_ids=music_ids)
