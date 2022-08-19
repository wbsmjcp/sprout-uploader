# Script to upload video files to both Sprout Video and Otter.ai.

This script uploads to the video service Sprout Video and the speech to text service Otter.ai using both API's.

The user provides a video file path which uploads to both services (user is given a choice to upload to Otter or not) and is returned a .csv file containing the web URL links for both uploads and a custom embed code that fits on the WBS VLE, my.wbs. 

It also renames the file on Sprout, removing the file extension. (Sprout does this now by default as of August 2022)

-- New features/Changes -- August 2022
Creates aspect size appropriate embed code and copies it to clipboard.

Adds second code to CSV where Title is not included, to be adjusted manually.

CSV reconfigured and easier to read, adds aspect ratio to ticket for determining appropriate thumbnail frame.

Shows elapsed time of process.

Will loop if non appropriate file format is found.

Will accept folder or file paths, will list and process through all files individually in a folder path.

Added clearer command comments and Ascii art. 

---

This script is designed to be used from the command line. 
If you don't have it, you will need to download Python 3 from the official website.  
`https://www.python.org/downloads/`  

You will also need to have pipenv installed. Open terminal and paste this in:  
`sudo -H pip3 install -U pipenv `  
It will ask for your password and then install.

## Saving your script folder
Download the folder as a zip from the green code button at the top of the page:  
`https://github.com/twentynineteen/sprout-uploader`  

If you have git installed you can clone it  using the command: 
``` 
git clone https://github.com/twentynineteen/sprout-uploader
```

Using the terminal, navigate to the folder you've saved the script files in.  
if you saved it to your documents folder the command would look like this:  
```cd documents/sprout-uploader```

## Setting up your login credentials
### Required: store login details as .env file within folder. See below for variables.

Create a file called .env in your sprout-uploader folder:
```
touch .env
```

Using your text editor, enter these variables and update accordingly: 

``` 
sprout_id = '' # Your sprout email ID
sprout_pass = '' # Your sprout ID password
otter_id = '' # Your otter email ID
otter_pass = '' # Your otter ID password
outputFolder = '' # Your output folder path. e.g. 'USERS/MyUploads/UploadTickets'
SproutVideoApiKey = "" #Sprout API Key
list_Videos = "https://api.sproutvideo.com/v1/videos"
upload_Videos = "https://api.sproutvideo.com/v1/videos"
```
The email addresses and passwords need to be wrapped in quotation marks (single or double is fine).

Your Sprout Api key is accessible from your account info when you log in at:

https://sproutvideo.com/settings/api

Do not share your API key with anyone! 

---
## Installing the Python environment

To install the modules needed to run your script you will need to use pipenv.

Navigate to your 'Sprout-uploader' folder, if not already there:  
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
pipenv install .
```

If you don't have git installed, go to the url and download the zip folder from the green code button at the top of the page. Unzip it into your sprout-uploader folder.  

Once unzipped, navigate your terminal into the otterai-api folder and run the pipenv install . command:

```
cd otterai-api
pipenv install .
```

otterai-api folder should now be in the same folder as your project files.

![folder directory](/images/image2.png)

---
## Updating the script to work on your machine

You will need to update the 'main.py' and 'Upload Video.sh' file for your machines file directory. It's easy to do with a text editor like TextEdit or VS Code.


### updating upload video.sh
Right click and open 'Upload Video.sh' with TextEdit. It's in the 'desktop scripts' folder. <br>

The code inside will look like this:
```
cd ""
pipenv run python3 main.py
open ""
exit
```

Find and copy the file path to where Sprout-Uploader is installed. Paste the code into the quote marks above (under cd and open). Once done it should look like the below. You can save and close the shell file. 

```
cd "/Users/mycomputer/github/sprout-uploader"
pipenv run python3 main.py
open "/Users/mycomputer/github/sprout-uploader"
exit
``` 

---
## Creating a shortcut to your mac dock
At this point, you should be able to run the upload script by clicking the 
```
upload video.sh
``` 
file. If you'd like to put it on your dock, you need to rename the .sh file to .app (it will ask for confirmation).

From here, drag the .app file to your dock. It won't run in this state as a .app file so we need to rename it back using the terminal.

Open the terminal and navigate to the desktop scripts folder the .sh file is located.

once in, run the following code:<

```
mv "Upload Video.app" "Upload Video.sh"
```

![dock view](/images/image3.png)

You can close the terminal here and run the script from your dock now or, if you wish, you can test the script from the terminal using the steps in the next section. Before then, you need to go up a directory with the following command:

```
cd ..
```

---

###  Running the script from the terminal

to run script, navigate terminal to project folder and run:
```
pipenv run python3 main.py
```

Next up, the script requests file path.<br>
You can get this from the status bar at the bottom of your finder window (with the video selected). <br>
Right click the file path to get the option to copy to your clipboard.   
![File path example](/images/image1.png)

Script stores video title as new variable and removes filetype.<br>
Script attempts to upload video file to Otter.ai using supplied login credentials. <br>
Script then uploads to SproutVideo with new title and returns upload information for both otter and sprout as a csv that contains links and embed codes.

---
### Future versions?

display progress from upload  <br>
get from otter and upload to video file - not currently able to do this  <br>
share otter speech with designated user / group   <br>
collect and upload posterframe to video file?  <br>
