#!/usr/bin/python2.7

import re
import urllib
import urllib2
import requests



## Login URL : APIDomain + api/login/?apikey=APILoadTest&url=http%3A%2F%2Flocalhost%2Floadtest%2Fapi%2Fdemo.html";
## Return "token" string

APIKey = "QgGyUDJLNjT3tDAAN2mJ1";
authtoken="53A050436F976AEA3FB2775ACDA3108C22460F22FF3E2BD0214EE4937FF4055CB6D62A302927F0413B5BB98FB1E8671AF40AE3E12E6B52A36E15F031CB6225B0D1C930A7303D33F9722757DEEBBFB82EA3495FD1834EC4A087402337A305AAE28F7E7055D7BB04A2A9C3FAD2D88C1C4E03B966FBB6F226691A92FF765A2C46B5522B0DEFF8357E575F12E818F9FBAD605AFA3681FA76016C49FAA40A988F7830F9C3850183039B61E5B77A55CE1454448C6C0F44C0329CF6D1037BE73840231F589D09BAE379DA9FA6591EC2114BB59D"
APIDomain = "https://ivle.nus.edu.sg/";
APIUrl = APIDomain + "api/lapi.svc/";

## Validating User logged in
## Validate URL = https://ivle.nus.edu.sg/api/Lapi.svc/Validate?APIKey={System.String}&Token={System.String}
validateURL = APIUrl +"Validate?APIKey="+ APIKey+"&token="+ authtoken

validateResponse = requests.get(validateURL)		# Sending request
validateData = validateResponse.json()
if validateData['Success']:
	authtoken = validateData['Token']
# print validateData
## END

## Getting User ID
## URL = https://ivle.nus.edu.sg/api/Lapi.svc/UserID_Get?APIKey={System.String}&Token={System.String}
userIdURL = APIUrl +"UserID_Get?APIKey="+ APIKey+"&token="+ authtoken
userIdResponse = requests.get(userIdURL)		# Sending request
userIdData = userIdResponse.json()
print "UserID = "+ userIdData

## Getting User Name
## URL = https://ivle.nus.edu.sg/api/Lapi.svc/UserName_Get?APIKey={System.String}&Token={System.String}
userNameURL = APIUrl +"UserName_Get?APIKey="+ APIKey+"&token="+ authtoken
userNameResponse = requests.get(userNameURL)		# Sending request
userNameData = userNameResponse.json()
print "UserName = "+userNameData



## Getting list of all Modules
## Staff Module URL = https://ivle.nus.edu.sg/api/Lapi.svc/Modules_Staff?APIKey={System.String}&AuthToken={System.String}&Duration={System.Int32}&IncludeAllInfo={System.Boolean}
allModuleURL = APIUrl +"Modules_Student?APIKey="+ APIKey+"&AuthToken="+authtoken+"&Duration=0&IncludeAllInfo=false&output=json"
moduleList=[]
print allModuleURL
print '###########################################'
allModuleResponse = requests.get(allModuleURL)		# Sending request
allModuledata = allModuleResponse.json()
for i in (allModuledata['Results']):
	if (i['ID'] != '00000000-0000-0000-0000-000000000000'):
		print i['ID'] + ', ' + i['CourseName'] + ', ' + i['CourseCode']
		moduleList.append(i['ID'])
# print moduleList

# Getting details of particular module
# Module_Student = https://ivle.nus.edu.sg/api/Lapi.svc/Module_ReadingFormatted?APIKey={System.String}&AuthToken={System.String}&CourseID={System.String}&Duration={System.Int32}
moduleURL = APIUrl + "Module?APIKey="+ APIKey+"&AuthToken="+authtoken+"&Duration=0&IncludeAllInfo=true&output=json&CourseID="
moduleDetails = []

for i in list(x for x in moduleList if len(x) > 0):
	moduleResponse = requests.get(moduleURL+i)
	moduleData = moduleResponse.json()
	# print moduleData['Results']
	for m in moduleData['Results']:
		print m['CourseCode']+', '+m['CourseName']
	# print moduleDetails.append()
	print "----------------------------------------------------------------------------------------------------"

## Getting Polls/Quiz for a module
## https://ivle.nus.edu.sg/api/Lapi.svc/Polls?APIKey={System.String}&AuthToken={System.String}&CourseID={System.String}&PollID={System.String}&TitleOnly={System.Boolean}
pollsURL = APIUrl + "Polls?APIKey="+ APIKey+"&AuthToken="+authtoken+"&PollID=&TitleOnly=false&CourseID="
polls=[]

for i in moduleList:
	rosterResponse = requests.get(pollsURL+i)
	rosterData = rosterResponse.json()
	for rec in rosterData['Results']:
		if (rec['Published']):
			# print "Poll ID = " + rec['ID'] + " - " + rec['Title']
			polls.append({'pollId':rec['ID'],
						'pollName': rec['Title']})
			# print polls

## Web URL for Polls/Quizes
## Poll URL = https://ivle.nus.edu.sg/poll/poll.aspx?pollID=aa4c19f3-5bd5-43b1-b0a9-cb5d090b9f46&ClickFrom=outline
webPollURL = "https://ivle.nus.edu.sg/poll/poll.aspx?ClickFrom=outline&pollID="

# for poll in polls:
# 	print poll['pollName']
# 	print webPollURL+poll['pollId']
# 	print "----------------------------------------------------------------------------------------------------"


## Getting workbin details of a Module
## Workbin = https://ivle.nus.edu.sg/API/Lapi.svc/Class_Roster?APIKey={System.String}&AuthToken={System.String}&CourseID={System.String}
classRosterURL = APIUrl + "Class_Roster?APIKey="+ APIKey+"&AuthToken="+authtoken+"&CourseID="
guestRoasterURL= APIUrl + "Guest_Roster?APIKey="+ APIKey+"&AuthToken="+authtoken+"&CourseID="
moduleEnrol =[]

for i in moduleList:
	if i == '391ae11a-46ce-488a-ac22-1c77cdf119b2':		
		rosterResponse = requests.get(classRosterURL+i)
		rosterData = rosterResponse.json()
		for rec in rosterData['Results']:
			print rec['UserID'] + '@nus.edu.sg - '+ rec['Name']
			if (rec['UserID']):
				moduleEnrol.append(rec['UserID'])
	
for i in moduleList:
	rosterResponse = requests.get(guestRoasterURL+i)
	rosterData = rosterResponse.json()
	for rec in rosterData['Results']:
		if (rec['UserID']):
			moduleEnrol.append(rec['UserID'])
# for row in moduleEnrol:
# 	print row


## Getting workbin details of a Module
## Workbin = https://ivle.nus.edu.sg/api/Lapi.svc/Workbins?APIKey={System.String}&AuthToken={System.String}&CourseID={System.String}&Duration={System.Int32}&WorkbinID={System.String}&TitleOnly={System.Boolean}
workbinURL = APIUrl + "Workbins?APIKey="+ APIKey+"&AuthToken="+authtoken+"&Duration=0&WorkbinID=&TitleOnly=false&CourseID="
downloadableFiles = []
nonDownloadableFiles = []

for i in moduleList:
	# print workbinURL+i
	workbinResponse = requests.get(workbinURL+i)
	workbinData = workbinResponse.json()
	# for i in (i for i in (row['Files'] for row in (rec['Folders'][0] for rec in workbinData['Results'])) if i)

	# Parsing the records obtained for each web
	# for rec in workbinData['Results']:
	# 	for row in rec['Folders']:
	# 		for length in xrange(len(row['Files'])):
	# 			for i in [row['Files'][length]]:
	# 				if i['isDownloaded']:
	# 					# downloadableFiles.append(i['ID'])
	# 					print "Downloadable : " + i['ID'] + ', '+ i['FileName'] + ', '+ i['FileDescription']
	# 				else:
	# 					nonDownloadableFiles.append(i['ID'])
	# 					# print "Non - Downloadable : " + i['ID'] + ' '+ i['FileName']
	# print "######################################################################"


## Download file = https://ivle.nus.edu.sg/api/downloadfile.ashx?APIKey={System.String}&AuthToken={System.String}&ID={System.Guid}&target=workbin
downloadURL = APIDomain + "api/downloadfile.ashx?APIKey="+ APIKey+"&AuthToken="+authtoken+"&target=workbin&ID="

# for filename in downloadableFiles:
	# print downloadURL+filename
	# urllib.urlretrieve (downloadURL+filename, "file.gz")


			