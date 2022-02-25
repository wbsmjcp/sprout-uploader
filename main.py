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

file = '/Users/dan_1/Documents/VSCODE/SPROUTUPPER/VID_18.mp4'
title = os.path.basename(file)
speech_id = ''
rendered_speech_id = 'byo1ubKeTln7k4xzbkT7bbpsUBA'


def upload_speech(file):
    """
    It uploads the speech file to the OtterAI platform
    
    :param file: The file you want to upload
    :return: The speech_id is being returned.
    """
    global speech_id
    try:
        upload = otter.upload_speech(file)
        print(upload['status'])
        print(upload['data'])
        speech_id = upload['data']['otid']
        print(speech_id)
    except OtterAIException as e:
        print("Didn't work for some reason")

    return speech_id

# upload_speech(file)

def get_speech(id):
    """
    The function takes in a string of the Otter otid and returns the user's speech
    
    :param id: The id of the speech you want to get
    """
    global rendered_speech_id
    try:
        speech = otter.get_speech(id)
    except OtterAIException as e:
        print("Couldn't find the speech")
    return speech


file = get_speech("byo1ubKeTln7k4xzbkT7bbpsUBA")
# print(json.dumps(file, indent = 4))
print(file['status'])
with open('sample_otter.json', 'w') as outfile:
    json.dump(file, outfile)



# print('Enter video file path')
# video_file = input()
# video_title = os.path.basename(video_file)

# m = MultipartEncoder(
#     fields={
#         'source_video': (video_file, open(video_file, 'rb'), 'text/plain'),
#         'video_title': video_title
#     }
# )

# r = requests.post(upload_Videos, data=m, headers={'Content-Type': m.content_type, 'SproutVideo-Api-Key': SproutVideoApiKey})

# print(r.text)

#TO DO --- create function
#  edit filename to remove filetype for upload
# upload to otter
# python api from github
# display progress from upload
# generate embed / print embed?
# get from otter and upload to video file
