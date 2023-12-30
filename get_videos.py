from pexelsapi.pexels import Pexels
import random
import requests

pexel = Pexels(PEXELSAPIKEY)

def download_video(url, file_name):
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        print(f"Download complete. Video saved as {file_name}")
    else:
        print(f"Failed to download video. Status code: {response.status_code}")


def download_videos(number, niche):
    id_videos = []
    search_videos = pexel.search_videos(query=niche, orientation='portrait', size='', color='', locale='', page=1, per_page=15)
    
    for _ in range(number):
        random_index = random.randrange(0, 15)
        video = search_videos['videos'][random_index]
        video_id = video.get('id')

        if video_id:
            id_videos.append(video_id)
        else:
            print(f"Video ID not found for random index {random_index}. Skipping.")

    for video_id in id_videos:
        try:
            video_info = pexel.get_video(video_id)
            video_files = video_info.get('video_files', [])

            if video_files:
                video_link = video_files[0].get('link')

                if video_link:
                    print(f"Downloading video with ID {video_id} from {video_link}")
                    download_video(video_link, f"{video_id}.mp4")
                else:
                    print(f"Video link not found for video ID {video_id}. Skipping.")
            else:
                print(f"Video files not found for video ID {video_id}. Skipping.")

        except Exception as e:
            print(f"Error downloading video with ID {video_id}: {e}")

    return id_videos