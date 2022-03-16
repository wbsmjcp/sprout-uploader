# Script to upload video files to both Sprout Video and Otter.ai.

---

This script is designed to be used from the command line. 
If you don't have it, you will need to download Python 3 from the official website.  
`https://www.python.org/downloads/`  

You will also need to have pipenv installed. Open terminal and paste this in:  
`sudo -H pip3 install -U pipenv `  
It will ask for your password and then install.

## Setting up your login credentials
### Required: store login details as .env file within folder. See below for variables.

Create a file called .env in your sprout-uploader folder:
```
touch .env
```

Using your text editor, enter these variables and update accordingly: 

``` 
sprout_id = 'your sprout login email'
sprout_pass = 'your sprout password'
otter_id = 'your otter login email'
otter_pass = 'your otter password'
SproutVideoApiKey = 'your sprout video api key'
list_Videos = "https://api.sproutvideo.com/v1/videos"
upload_Videos = "https://api.sproutvideo.com/v1/videos" 
```


---
## Installing the Python environment

To install the modules needed to run your script you will need to use pipenv.

Navigate back up to your 'Sprout-uploader' folder:  
`cd ..`

Install your pipenv environment:  
`pipenv install`

---

## Installing the Otter Api script

Uses otterai-api from https://github.com/chadlohrli/otterai-api
needs to be cloned into project repository and installed via:

```
git clone https://github.com/chadlohrli/otterai-api
cd otterai-api
'pipenv install .'
```

otterai-api folder should be in the same folder as you your project files.

---

###  Running the script from the terminal

to run script, navigate terminal to project folder and run:
```
pipenv run python3 main.py
```

script requests file path.
You can get this from the status bar at the bottom of your finder window (with the video selected). Right click the file path to get the option to copy to your clipboard.   
![File path example](/images/image1.png)

Script stores video title as new variable and removes filetype.
Script attempts to upload video file to Otter.ai using supplied login credentials
Script then uploads to SproutVideo with new title and returns upload information for both otter and sprout as a csv that contains links and embed codes.

---
### Future versions?

display progress from upload  
get from otter and upload to video file - not currently able to do this  
share otter speech with designated user / group   
collect and upload posterframe to video file?  
future versions: upload all files within folder?  
