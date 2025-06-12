from ytmusicapi import YTMusic

def search_songs_from_file(filepath):
    """
    Searches for songs from a text file using ytmusicapi.

    The text file should have one song per line in the format "Artist - Song_name".

    Args:
        filepath (str): The path to the text file.

    Returns:
        dict: dictionary
              representing the top search result for a single song.
    """
    ytmusic = YTMusic()
    results = []

    try:
        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    search_result = ytmusic.search(line)
                    results.append(search_result[0])
                    if len(results)%50==0:
                        print(len(results))
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return results

if __name__ == '__main__':
    filepath = 'songs.txt'  # Replace with your file path

    search_results = search_songs_from_file(filepath)
    with open("video_ids.txt", "r") as f:
        if search_results:
            for result in search_results:
                if result:
                    f.write(f"{result.get('videoId', '')}\n")
        else:
            print("No songs found in the file or an error occurred.")
