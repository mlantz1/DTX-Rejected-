#Get the data from all turbines.
import requests
from flask import Flask, render_template

#create the application instance
app = Flask(__name__)

@app.route("/")
def index():
	return render_template('display_data.html')

#Return
@app.route("/getdatastring")
def getCurrentData():
	#Use https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/:turbine_id/sensors/:sensor_id
	turbine1_temp = requests.get("https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/1/sensors/temperature")
	turbine1_volt = requests.get("https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/1/sensors/voltage")
	turbine2_temp = requests.get("https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/2/sensors/temperature")
	turbine2_volt = requests.get("https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/2/sensors/voltage")
	turbine3_temp = requests.get("https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/3/sensors/temperature")
	turbine3_volt = requests.get("https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/3/sensors/voltage")

	data = '{' + turbine1_temp.content + turbine1_volt.content + turbine2_temp.content + turbine2_volt.content + turbine3_temp.content + turbine3_volt.content + '}'
	return data

#Get the data in a list instead of JSON
# def getDataList():
# 	data = ()
# 	for i in range(1, 4):
# 		data.add(requests.get("https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/" + str(i) + "/sensors/temperature"))
# 		data.add(requests.get("https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/" + str(i) + "/sensors/voltage"))
# 	return data