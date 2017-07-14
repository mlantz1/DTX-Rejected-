# DTX-Rejected-

## Flask data server

### Running the server

To run the flask data server, be sure python is installed and also flask and requests python modules.
In the man folder, execute:

`./run.sh`

If you are running on a Windows machine, execute this in git bash or some other program providing bash functionallity. It is possible that the path to flask is different on Windows. If so, try `which flask` in your bash terminal to find the path. Create a new file for running on Windows copied from `run.sh` and replace the path with your Windows path.

If you do not want to use the script to run, use the following commands:

`export FLASK_APP=app.py`

`flask run`
