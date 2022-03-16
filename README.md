# Script to upload video files to both Sprout Video and Otter.ai.

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
``` git clone https://github.com/twentynineteen/sprout-uploader```

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
### Updating the script to work on your machine

You will need to update the 'main.py' and 'Upload Video.sh' file for your machines file directory. It's easy to do with a text editor like TextEdit or VS Code.


### updating main.py
Right click and open main.py with TextEdit.

Scroll down to the bottom, looking for the line:    

```def_transposed.to_csv(f"/Users/dan_1/Desktop/Upload Ticket - {title}.csv")```
<br>
you need to replace the '/Users/dan_1/Desktop/' section with the file path for your own desktop (or somewhere else you'd like the upload ticket csv files to go). <br>

Click save and close the script when you are done.

### updating upload video.sh
Right click and open 'Upload Video.sh' with TextEdit. It's in the 'desktop scripts' folder. <br>

The code inside will look like this:
```
cd "/Users/dan_1/Documents/VSCODE/SPROUTUPPER"
pipenv run python3 main.py
open "/Users/dan_1/Documents/VSCODE/SPROUTUPPER"
exit
```

replace the '/Users/dan_1/Documents/VSCODE/SPROUTUPPER' section with the pathname to folder you've saved the files to. In the earlier image, we saved the sprout-uploader folder to our documents folder so we would replace with '/Users/dan_1/Documents/sprout-uploader'.

When you have replaced the text on line 1 and 3, click save and close the file.

---
# Creating a shortcut to your mac dock
At this point, you should be able to run the upload script by clicking the 'upload video.sh' file. If you'd like to put it on your dock, you need to rename the .sh file to .app (it will ask for confirmation).

From here, drag the .app file to your dock. It won't run in this state as a .app file so we need to rename it back using the terminal.

Open the terminal and navigate to the desktop scripts folder the .sh file is located.

once in, run the following code:<br>

```
mv "Upload Video.app" "Upload Video.sh"
```

![dock view](/images/image3.png)

You can close the terminal here and run the script from your dock now or, if you wish, you can test the script from the terminal using the steps in the next section. Before then, you need to go up a directory with the following command:
<br>
`cd ..`

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

display progress from upload  <br>
get from otter and upload to video file - not currently able to do this  <br>
share otter speech with designated user / group   <br>
collect and upload posterframe to video file?  <br>
future versions: upload all files within folder?  <br>
