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


# files = {
#     'source_video': (str(video_file), open(str(video_file), 'rb'), 'text/plain'),
#     'video_title'
#     }
# body, content_type = requests.models.RequestEncodingMixin._encode_files(files, {})

# this way you ensure having the same boundary defined in
# the multipart/form-data contetn-type header
# the form-data

# payload = {
#     'source_video': video_file,
#     'title': video_title,

#     }

# def upload_sprout(files):

#     response = requests.post(
#         upload_Videos, 
#         files=files, 
#         headers={
#             'SproutVideo-Api-Key': SproutVideoApiKey
#             }
#         )
#     print(response.text)

#     return response.json()

# upload_sprout(files)
