#Get the data from all turbines.
import requests
import json
from flask import Flask, render_template

#create the application instance
app = Flask(__name__)
app.config.from_object(__name__)

#Return all turbine data
@app.route("/getAllData")
def getCurrentData():
	#Use https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/:turbine_id/sensors/:sensor_id
	turbine1_temp = requests.get("https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/1/sensors/temperature")
	turbine1_volt = requests.get("https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/1/sensors/voltage")
	turbine1_stat = requests.get("https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/1/heartbeat")

	data = turbine1_temp.data()
	return data

#Return one turbine's data as a string
@app.route("/getTurbineData/<id>/")
def getTurbineDataString(id):
	return str(getTurbineData(id))

#Return one turbine's data
def getTurbineData(id):
	#Get data
	turbine_temp = requests.get("https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/" + str(id) + "/sensors/temperature")
	turbine_volt = requests.get("https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/" + str(id) + "/sensors/voltage")
	turbine_stat = requests.get("https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/" + str(id) + "/heartbeat")
	data = dict()

	#Populate Dictionary
	data["id"] = str(id)
	data["timestamp"] = json.loads(turbine_temp.text)['timestamp']
	data["temp"] = json.loads(turbine_temp.text)['value']
	data["voltage"] = json.loads(turbine_volt.text)['value']
	data["status"] = json.loads(turbine_stat.text)['status']

	return data

#Get the data in a list instead of JSON
# def getDataList():
# 	data = ()
# 	for i in range(1, 4):
# 		data.add(requests.get("https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/" + str(i) + "/sensors/temperature"))
# 		data.add(requests.get("https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/" + str(i) + "/sensors/voltage"))
# 	return data
