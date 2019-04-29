import requests
def get_quotes():
    url = "http://quotes.stormconsultancy.co.uk/random.json"
    res = requests.get(url)
    if res.status_code == 200:
        data =res.json()
        return data
    return False 