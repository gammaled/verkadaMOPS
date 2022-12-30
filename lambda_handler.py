#!/usr/bin/env python3

import json
import re
import requests

# Import any libraries you need

## Do not edit
class VerkadaDB():
    def __init__(self):
        self._data = {}
	      ## You may add to the class definition below this line
        
## To-do: add class methods
    def addTable(self, tableName):
        db = self._data
        db[tableName] = {}
        
    def addRow(self,tableName, rowData):
        db = self._data
        db[tableName][rowData["email"]] = rowData
    
    def getRows(self,tableName, matchingCriteria):
        pass
    
    def updateRows(self, tableName, matchingCriteria, updateInformation):
        pass
    
    def deleteRows(self,tableName, matchingCriteria):
        pass

## Do not edit   
dbInstance = VerkadaDB()
dbInstance.addTable("table1")

def get_response(name):
    agify_url = "https://api.agify.io?name=" + name
    genderize_url = "https://api.genderize.io?name=" + name
    nationalize_url = "https://api.nationalize.io?name=" + name

    age_response = requests.get(agify_url).json()
    gender_response = requests.get(genderize_url).json()
    country_response = requests.get(nationalize_url).json()

    age = age_response["age"]
    gender = gender_response["gender"]
    country = country_response["country"][0]["country_id"]

    return [age, gender, country]

## To-do: Implement Function (mimics AWS Lambda handler)
## Input: JSON String which mimics AWS Lambda input
def lambda_handler(json_input):
    global dbInstance
    json_input = json.loads(json_input)
    split_result = re.split(r"[@\.]", json_input["email"])
    email = json_input["email"]
    name = split_result[0]
    domain = split_result[1]
    topLevelName = split_result[-1]

    response = get_response(name)
    age = response[0]
    gender = response[1]
    nationality = response[2]

    if domain != "verkada":
        personal_details = {
            "name": name,
            "email": email,
            "domain": domain,
            "topLevelName": topLevelName,
            "age": age,
            "gender": gender,
            "nationality": nationality
        }
        json_output = json.dumps(personal_details)
        dbInstance.addRow("table1", personal_details)
        print(dbInstance._data)
        #print(json_output)
        ## Output: JSON String which mimics AWS Lambda Output
        return json_output
    else:
        return

## To Do: Create a table to hold the information you process
    

## Do not edit
#lambda_handler(json.dumps({"email":"John@acompany.com"}))
#lambda_handler(json.dumps({"email":"Willy@bcompany.org"}))
#lambda_handler(json.dumps({"email":"Kyle@ccompany.com"}))
#lambda_handler(json.dumps({"email":"Georgie@dcompany.net"}))
#lambda_handler(json.dumps({"email":"Karen@eschool.edu"}))
#lambda_handler(json.dumps({"email":"Annie@usa.gov"}))
#lambda_handler(json.dumps({"email":"Elvira@fcompay.org"}))
#lambda_handler(json.dumps({"email":"Juan@gschool.edu"}))
#lambda_handler(json.dumps({"email":"Julie@hcompany.com"}))
#lambda_handler(json.dumps({"email":"Pierre@ischool.edu"}))
#lambda_handler(json.dumps({"email":"Ellen@canada.gov"}))
#lambda_handler(json.dumps({"email":"Craig@jcompany.org"}))
#lambda_handler(json.dumps({"email":"Juan@kcompany.net"}))
#lambda_handler(json.dumps({"email":"Jack@verkada.com"}))
lambda_handler(json.dumps({"email":"Jason@verkada.com"}))
#lambda_handler(json.dumps({"email":"Billy@verkada.com"}))
#lambda_handler(json.dumps({"email":"Brent@verkada.com"}))

## Put code for Part 2 here