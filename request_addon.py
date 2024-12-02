import requests
import urllib.request
def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_yt_mp3(link):
    urllib.request.urlretrieve("https://youtube-download-api.matheusishiyama.repl.co/mp4?url="+link,"temp.mp3")