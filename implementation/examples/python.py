from urllib.request import urlopen
from urllib.error import URLError
import json

def map(UID, activity):
    try:
        response = urlopen(f"https://apicopperheadsoftware.co/heatmpa/?UID={UID}&activity={activity}")
    except URLError:
        print("Error 504!\nI'm very sorry, our heatmap service seems to be under maintenance. Please try again later.")
        return
    data = json.loads(response.read().decode("utf-8"))
    return data

print(map("UID", "activity"))