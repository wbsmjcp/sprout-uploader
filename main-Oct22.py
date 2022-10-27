#! python3
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import os
from pathlib import Path
import json
import sys
import math
sys.path.insert(0, 'otterai-api/otterai')
from otterai import OtterAI, OtterAIException
from decouple import config
import pandas as pd
import pyperclip
import cv2
import pyinputplus as pyip
from datetime import datetime

start_time=datetime.now()

sprout_id = config('sprout_id', default='')
sprout_pass = config('sprout_pass', default='')
otter_id = config('otter_id', default='')
otter_pass = config('otter_pass', default='')
SproutVideoApiKey = config('SproutVideoApiKey', default='')
upload_Videos = config('upload_Videos', default='')
video_title = () 
output_folder=config('outputFolder', default='')

otter = OtterAI()
otter.login(otter_id, otter_pass)

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
    print('\n Attempting to upload speech: ' + title + ' to Otter.ai')
    try:
        upload = otter.upload_speech(file)
        speech_id = upload['data']['otid']
        rendered_URL = otter_URL + speech_id

    except OtterAIException as e:
        print("/n !!!! Didn't work for some reason !!!!")

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
    global embed_title
    global width
    global height
    global gcdaspect

    m = MultipartEncoder(
        fields={
            'source_video': (video_file, open(video_file, 'rb'), 'text/plain'),
            'title': video_title
        }
    )

    r = requests.post(upload_Videos, data=m, headers={'Content-Type': m.content_type, 'SproutVideo-Api-Key': SproutVideoApiKey})
    print(f"\n Video uploading to sprout under the name {video_title}.")
 
    with open('sprout_upload.json', 'w') as outfile:
        json.dump(r.text, outfile)

    with open('sprout_upload.json', 'r') as new_file:
        data = new_file.read()
    obj1 = json.loads(data)
    new_obj = json.loads(obj1)
    sprout_id = new_obj['id']
    
    #Get video res
    vid = cv2.VideoCapture(str(video_file))
    height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))

    #Aspect Ratio 
    asp = (width * 100) / (height * 100)
    gcd = int(math.gcd(height, width))
    gcdaspect = str(width//gcd) + ' x ' + str(height//gcd)

    #Embed code
    new_height = 350
    new_width = round(int(new_height)*asp)
    new_embed = new_obj['embed_code'].replace('630', str(new_width)).replace('354', str(new_height))
    embed_title = new_embed.replace('Video Player', title.replace('\'', ''))
    #Sprout video link
    sprout_link = "https://sproutvideo.com/videos/" + new_obj['id']

def run_all(file, title):
    #Otter upload query

    # responseOtter = input("\n --- upload to Otter? Y/N --- \n").upper()
    print('\n Uploading to otter')
    upload_speech(file)
    # try:
    #     if responseOtter == "Y":
    #         upload_speech(file)
    #     if responseOtter == "N":
    #         print("Skipping Otter.ai submission")
    # except:   
    #     if responseOtter != "N" or responseOtter != "Y":
    #         print("Didn't recognise input, skipping Otter upload")       

    # upload_speech(file)
    print('Uploading to sprout')
    upload_sprout(file, title)

def print_ascii(asc):
    f= open(asc,'r')
    print(''.join([line for line in f]))

#Acceptable Formats list
with open("formats.txt", "r") as f:
    formats = [line.strip() for line in f]

#Program start
print_ascii('images/ascii-art.txt')
print('\n---Sprout and Otter Uploader---')

while True:
    #Ask for user input
    filePath = Path(input('\nPlease paste your video file/folder location:\n'))

    #Check if file is a valid format or in a folder
    while not filePath.is_dir() and filePath.suffix not in formats:
        print('That\'s not a valid file format or folder location. Please try again \n')
        filePath = Path(input('Paste your video file/folder location: '))

    #Determine if file or folder and set Path
    if filePath.is_file():file = [filePath]
    else:
        file = list(p.resolve() for p in Path(filePath).glob("**/*") if p.suffix in formats)

    print('\n path entered... \n --------')

    copyClip=[]
    database = {
        "Video Title":[],
        "Embed Code": [],
        "Sprout ID": [],
        "Sprout URL": [],
        "Aspect Ratio": [],
        "Otter URL":  [],
        "Video Title TLE":[],
        "TLE Embed": []
            }

    for fp in range(0, len(file)):
        title = file[fp].stem
        print('\n Processing file %s' % (title))
        run_all(str(file[fp]), title)
        
        #Add to dictionary for ticket
        database["Video Title"] += [title]
        database["Embed Code"] += [embed_title]
        database["Sprout ID"] += [sprout_id]
        database["Sprout URL"] += [sprout_link]
        database["Aspect Ratio"] += [gcdaspect]
        database["Otter URL"] += [rendered_URL]
        database["Video Title TLE"] += [title]
        database["TLE Embed"] += [new_embed]

        #Create copy to clipboard variable
        copyTitle = database.get('Video Title')[fp]
        copyCode = database.get('Embed Code')[fp]
        copyClip.extend(['\n' + copyTitle + '\n' + copyCode])
        print('\n Finished uploading file %s to sprout.' % (title))

    #Create ticket for all files
    timeStamp = datetime.now().strftime('%d-%b-%y - %H-%M')
    df = pd.DataFrame.from_dict(database, orient ='index')
    df.to_csv(f"{output_folder}/Upload Ticket - {timeStamp}.csv", index=True, header=False)

    #You are done
    pyperclip.copy('\n'.join(copyClip))
    print(df)
    print(" Complete. Please see csv file for info \n --- Titles and Embed codes copied to clipboard")
    end_time=datetime.now()
    elapsed_time=end_time-start_time
    print('Time to complete program ', elapsed_time, ' seconds')
    prompt_rerun = 'Do you want to upload more files? \n'
    response=pyip.inputYesNo(prompt_rerun)
    if response == 'no':
        break
print('\n Thank you and good night!')

#TODO - Add while True loop to run until user breaks out
#TODO - Add print out of copied info to console
#TODO - Tickets/files in alphabetical order?
#TODO - Flash/Django/REACTJS integration, web app instead of command line console
#TODO - Public web app for academics to upload directly?????