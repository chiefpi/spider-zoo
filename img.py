import requests

def fetch():
    url = "https://www.wikipedia.org/portal/wikipedia.org/assets/img/Wikipedia-logo-v2.png"
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
    resp = requests.get(url, headers=headers)
    return resp
    
if __name__ == '__main__':
    responce = fetch()
    with open("wiki_logo.jpg", "wb") as fp:
        fp.write(responce.content)
    
