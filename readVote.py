import urllib.request
import json
from pprint import pprint

consYes = 0
consNo = 0
consA = 0
labYes = 0
labNo = 0
labA = 0
snpYes = 0 
snpNo = 0
snpA = 0
ldYes = 0
ldNo = 0
ldA = 0
dupYes = 0
dupNo = 0
dupA = 0
othYes = 0
othNo = 0
othA = 0

Yes= {'Liberal Democrat': 0, 'Conservative': 0, 'UK Independence Party': 0, 'Scottish National': 0, 'Labour': 0, 'First Deputy Chairman of Ways and Means': 0, 'Independent': 0, 'Plaid Cymru': 0, 'Alliance': 0, 'Democratic Unionist': 0, 'Social Democratic & Labour Party': 0, 'Sinn Féin': 0, 'Respect': 0, 'Green': 0, 'Second Deputy Chairman of Ways and Means': 0, 'Speaker of the House of Commons': 0, 'Chairman of Ways and Means': 0};
No={'Liberal Democrat': 0, 'Conservative': 0, 'UK Independence Party': 0, 'Scottish National': 0, 'Labour': 0, 'First Deputy Chairman of Ways and Means': 0, 'Independent': 0, 'Plaid Cymru': 0, 'Alliance': 0, 'Democratic Unionist': 0, 'Social Democratic & Labour Party': 0, 'Sinn Féin': 0, 'Respect': 0, 'Green': 0, 'Second Deputy Chairman of Ways and Means': 0, 'Speaker of the House of Commons': 0, 'Chairman of Ways and Means': 0}
Abstain = {'Liberal Democrat': 0, 'Conservative': 0, 'UK Independence Party': 0, 'Scottish National': 0, 'Labour': 0, 'First Deputy Chairman of Ways and Means': 0, 'Independent': 0,'Plaid Cymru': 0, 'Alliance': 0, 'Democratic Unionist': 0, 'Social Democratic & Labour Party': 0, 'Sinn Féin': 0, 'Respect': 0, 'Green': 0, 'Second Deputy Chairman of Ways and Means': 0, 'Speaker of the House of Commons': 0, 'Chairman of Ways and Means': 0}
#Yes["Conservative"]=10
#Yes["UK Independence Party"]=1
#No["Conservative"]=0


print ("making request")
url = 'http://lda.data.parliament.uk/commonsdivisions/id/229689.json'
test = urllib.request.urlopen(url)

#test = open (.\testVote.json)
data = test.read()
jsonData = data.decode('utf-8')
print(len(jsonData))
count = 0
jsonObj = json.loads(jsonData)

#pprint(jsonData)
#pprint (jsonObj["result"]["primaryTopic"]["vote"][0])
votes = jsonObj["result"]["primaryTopic"]["vote"]
voteCount = len(votes)
for count in range(0, voteCount-1):
    party = jsonObj["result"]["primaryTopic"]["vote"][count]["memberParty"]
    vote = jsonObj["result"]["primaryTopic"]["vote"][count]["type"]
    name = jsonObj["result"]["primaryTopic"]["vote"][count]["memberPrinted"]["_value"]
    #print (name)
    #print (vote)
    #print (party)
    if (vote == "http://data.parliament.uk/schema/parl#AyeVote"):
        Yes[party] = Yes[party] + 1;
        #print('Yes')
    elif (vote == "http://data.parliament.uk/schema/parl#NoVote"):
        No[party]+=1
        #print ('No')
    else:
        Abstain[party]+=1
        #print ('Abstain/Other')
    #print ("\n")

consYes = Yes["Conservative"]
consNo = No["Conservative"]
consA = 331-(consYes+consNo)
print ("Con Yes " + str(consYes))
print ("Con No " + str(consNo))
print ("Con Abs " + str(consA))

labYes = Yes["Labour"]
labNo = No["Labour"]
consA = 232-(labYes+labNo)

snpYes = Yes["Scottish National"]
snpNo = No["Scottish National"]
snpA = 56-(snpYes+snpNo)

ldYes = Yes["Liberal Democrat"]
ldNo = No["Liberal Democrat"]
ldA = 8-(ldYes+ldNo)

dupYes = Yes["Democratic Unionist"]
dupNo = No["Democratic Unionist"]
dupA = 8-(dupYes+dupNo)

