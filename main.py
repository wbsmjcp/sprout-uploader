import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import os
import json
from decouple import config

sprout_id = config('sprout_id', default='')
sprout_pass = config('sprout_pass', default='')
otter_id = config('otter_id', default='')
otter_pass = config('otter_pass', default='')
SproutVideoApiKey = config('SproutVideoApiKey', default='')
upload_Videos = config('upload_Videos', default='')


print('Enter video file path')
video_file = input()
video_title = os.path.basename(video_file)

m = MultipartEncoder(
    fields={
        'source_video': (video_file, open(video_file, 'rb'), 'text/plain'),
        'video_title': video_title
    }
)

r = requests.post(upload_Videos, data=m, headers={'Content-Type': m.content_type, 'SproutVideo-Api-Key': SproutVideoApiKey})

print(r.text)

#TO DO --- create function
#  edit filename to remove filetype for upload
# upload to otter
# 