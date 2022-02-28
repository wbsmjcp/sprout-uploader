# Script to upload video files to both Sprout Video and Otter.ai.

### Required: store login details as .env file within folder. See main.py for variables.

Uses otterai-api from https://github.com/chadlohrli/otterai-api
needs to be cloned into project repository and installed via pipenv install .

to run script, navigate CLI to project folder and run:
pipenv shell
pipenv run python main.py

script requests file path.

Script stores video title as new variable and removes filetype.
Script attempts to upload video file to Otter.ai using supplied login credentials
Script then uploads to SproutVideo with new title and returns upload information for both otter and sprout as a csv that contains links and embed codes.