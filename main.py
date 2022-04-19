import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import os
import json
import sys
sys.path.insert(0, 'otterai-api/otterai')
from otterai import OtterAI, OtterAIException
import os
from decouple import config
import pandas as pd

sprout_id = config('sprout_id', default='')
sprout_pass = config('sprout_pass', default='')
otter_id = config('otter_id', default='')
otter_pass = config('otter_pass', default='')
SproutVideoApiKey = config('SproutVideoApiKey', default='')
upload_Videos = config('upload_Videos', default='')

otter = OtterAI()
otter.login(otter_id, otter_pass)

print('enter file path')
filePath = input()
print(filePath)

file = filePath
print('file entered...')

old_title = os.path.basename(file)
title = old_title.replace('.mp4', '')

speech_id = ''
otter_URL = 'https://otter.ai/u/'
rendered_URL = ''

def upload_speech(file):
    """
    It uploads the speech file to the OtterAI platform
    
    :param file: The file you want to upload
    :return: The speech_id is being returned.
    """
    global speech_id
    global rendered_URL
    print('Attempting to upload speech: ' + title + ' to Otter.ai')
    try:
        upload = otter.upload_speech(file)
        speech_id = upload['data']['otid']
        rendered_URL = otter_URL + speech_id

    except OtterAIException as e:
        print("Didn't work for some reason")

    return speech_id

def get_speech(id):
    """
    The function takes in a string of the Otter otid and returns the user's speech
    
    :param id: The id of the speech you want to get
    """
    global url
    print('looking for speech...')
    try:
        speech = otter.get_speech(id)
        # url = speech['data']['speech']['download_url']
    except OtterAIException as e:
        print("Couldn't find the speech")
    return speech

def save_to_JSON(speech_id):
    file = get_speech(speech_id)

    print(f"Status is - {file['status']} ")
    with open('sample_otter.json', 'w') as outfile:
        json.dump(file, outfile)

def upload_sprout(video_file, video_title):
    global sprout_link
    global sprout_id
    global new_embed

    m = MultipartEncoder(
        fields={
            'source_video': (video_file, open(video_file, 'rb'), 'text/plain'),
            'title': video_title
        }
    )

    r = requests.post(upload_Videos, data=m, headers={'Content-Type': m.content_type, 'SproutVideo-Api-Key': SproutVideoApiKey})
    print(f"Video uploading to sprout under the name {video_title}.")
 
    with open('sprout_upload.json', 'w') as outfile:
        json.dump(r.text, outfile)

    with open('sprout_upload.json', 'r') as new_file:
        data = new_file.read()
    obj1 = json.loads(data)
    new_obj = json.loads(obj1)
    new_embed = new_obj['embed_code'].replace('630', '632').replace('354', '352')
    sprout_id = new_obj['id']
    sprout_link = "https://sproutvideo.com/videos/" + new_obj['id']
    
def run_all(file, title):
    print("upload to Otter? Y/N")
    responseOtter = input()
    resp1 = responseOtter.upper()

    try:
        if resp1 == "Y":
            upload_speech(file)
        if resp1 == "N":
            print("Skipping Otter.ai submission")
    except:
        if resp1 != "N" or resp1 != "Y":
            print("Didn't recognise input, skipping Otter upload")       
        
    upload_sprout(file, title)

run_all(file, title)

# - Build Ticket
database = {
    "Otter URL": rendered_URL,
    "Sprout ID": sprout_id,
    "Sprout URL": sprout_link,
    "Embed Code": new_embed
}

df = pd.DataFrame([database])
def_transposed = df.T
def_transposed.to_csv(f"Upload Ticket - {title}.csv")

print("Complete. Please see csv file for info")
