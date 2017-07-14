# DTX-Rejected-

## Running the Server

### Running the Server Locally

To run the flask data server, be sure python is installed and also flask and requests python modules.
In the man folder, execute:

`./run_local.sh`

If you are running on a Windows machine, execute this in git bash or some other program providing bash functionallity. It is possible that the path to flask is different on Windows. If so, try `which flask` in your bash terminal to find the path. Create a new file for running on Windows copied from `run.sh` and replace the path with your Windows path.

If you do not want to use the script to run, use the following commands:

`export FLASK_APP=app.py`

`flask run`

### Pushing to Predix

To push to Predix, use the script

`./push_remote`

Again, if you are on Windows, you may need to create another script with a different path.

If you do not want to use the script, the commands are

`px login`

`px push`


## Configurations

### Tech Stack

We are using flask in python to serve up data from the backend and to serve html. Javascript is being used in the html to retrieve data from the backend in anticipation of a request for continuous updating from the customer. Style sheets are using bootstrap. Persistent data storage has not yet been decided on.
