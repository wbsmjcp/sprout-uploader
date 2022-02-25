import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import os
import json
import sys
sys.path.insert(0, 'otterai-api/otterai')
from otterai import OtterAI
import os
from decouple import config

sprout_id = config('sprout_id', default='')
sprout_pass = config('sprout_pass', default='')
otter_id = config('otter_id', default='')
otter_pass = config('otter_pass', default='')
SproutVideoApiKey = config('SproutVideoApiKey', default='')
upload_Videos = config('upload_Videos', default='')

otter = OtterAI()
otter.login(otter_id, otter_pass)

print('enter file path')
file = input()
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
        # print(upload['status'])
        # print(upload['data'])
        speech_id = upload['data']['otid']
        # print(speech_id)
        rendered_URL = otter_URL + speech_id
        print('''The link to speech is ... ''' + rendered_URL)
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
    # print('saved JSON file to sample_otter.json')

def upload_sprout(video_file, video_title):
    m = MultipartEncoder(
        fields={
            'source_video': (video_file, open(video_file, 'rb'), 'text/plain'),
            'video_title': video_title
        }
    )

    r = requests.post(upload_Videos, data=m, headers={'Content-Type': m.content_type, 'SproutVideo-Api-Key': SproutVideoApiKey})
    print(f"Video uploading to sprout under the name {video_title}.")
 
    with open('sprout_upload.json', 'w') as outfile:
        json.dump(r.text, outfile)
    print('saved JSON file to sprout_upload.json')

    with open('sprout_upload.json', 'r') as new_file:
        data = new_file.read()
    obj1 = json.loads(data)
    new_obj = json.loads(obj1)
    new_embed = new_obj['embed_code'].replace('630', '632').replace('354', '352')
    print('Embed code is as follows:')
    print(new_embed)
    

def run_all(file, title):
    upload_speech(file)
    upload_sprout(file, title)

#TO DO --- create function
# display progress from upload
# get from otter and upload to video file - unable
# share otter speech with designated user / group
# collect and upload posterframe to video file?
# future versions: upload all files within folder?
# create a database/spreadsheet that stores all uploads and information in local folder
# Return all values as a ticket


run_all(file, title)