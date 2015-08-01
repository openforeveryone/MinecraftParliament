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
othYes = 15
othNo = 0
othA = 0

Yes= {'Liberal Democrat': 0, 'Conservative': 0, 'UK Independence Party': 0, 'Scottish National': 0, 'Labour': 0, 'First Deputy Chairman of Ways and Means': 0, 'Independent': 0, 'Plaid Cymru': 0, 'Alliance': 0, 'Democratic Unionist': 0, 'Social Democratic & Labour Party': 0, 'Sinn Féin': 0, 'Respect': 0, 'Green': 0, 'Second Deputy Chairman of Ways and Means': 0, 'Speaker of the House of Commons': 0, 'Chairman of Ways and Means': 0}
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











from mcpi import minecraft
mc = minecraft.Minecraft.create()

floorLevel = 15

#Minecraft block ids
aye = 44, 1
noe = 44
didntVote = 0

#Party Minecraft block ids
conservative = 35, 11
labour = 35, 14
snp = 35, 4
libDem = 35, 1
dup = 87
other = 35, 7

#Vote and party counters
currentParty = conservative
blockCount = 0
currentVote = aye
voteCount = 0




#for count in range(0, 5):
 #   for x in range(0, 3):
  #      print ("WE're on time %d %d" % (x, count))
    

#for y in range(20, 22):
 #   for x in range(0, 2):    
  #      mc.setBlock(x, y, x, 1)
        #mc.postToChat("x: %d, y: %d, z: 0" % (x, y))
   #     print("x: %d, y: %d, z: 0" % (x, y))

#mc.setBlocks(0, 21, 0, 64, 21, 5, 1)

mc.postToChat("Drawing set1")
for x in range(0, 65):
    for z in range(0, 5):
        mc.setBlock(x, -z+5+floorLevel, z, currentParty)
        mc.setBlock(x, -z+5+floorLevel+1, z, currentVote)
        blockCount+=1
        voteCount+=1
        if voteCount == consYes:
            currentVote = noe
        if voteCount == consNo+consYes:
            currentVote = didntVote
        if voteCount == consNo+consYes+consA:
            currentVote = aye
        if voteCount == consNo+consYes+consA+labYes:
            currentVote = noe
        if voteCount == consNo+consYes+consA+labYes+labNo:
            currentVote = didntVote
        if voteCount == consNo+consYes+consA+labYes+labNo+labA:
            currentVote = aye
        if voteCount == consNo+consYes+consA+labYes+labNo+labA+snpYes:
            currentVote = noe
        if voteCount == consNo+consYes+consA+labYes+labNo+labA+snpYes+snpNo:
            currentVote = didntVote
        if voteCount == consNo+consYes+consA+labYes+labNo+labA+snpYes+snpNo+snpA:
            currentVote = aye
        if voteCount == consNo+consYes+consA+labYes+labNo+labA+snpYes+snpNo+snpA+ldYes:
            currentVote = noe
        if voteCount == consNo+consYes+consA+labYes+labNo+labA+snpYes+snpNo+snpA+ldYes+ldNo:
            currentVote = didntVote
        if voteCount == consNo+consYes+consA+labYes+labNo+labA+snpYes+snpNo+snpA+ldYes+ldNo+ldA:
            currentVote = aye
        if voteCount == consNo+consYes+consA+labYes+labNo+labA+snpYes+snpNo+snpA+ldYes+ldNo+ldA+dupYes:
            currentVote = noe
        if voteCount == consNo+consYes+consA+labYes+labNo+labA+snpYes+snpNo+snpA+ldYes+ldNo+ldA+dupYes+dupNo:
            currentVote = didntVote
        if voteCount == consNo+consYes+consA+labYes+labNo+labA+snpYes+snpNo+snpA+ldYes+ldNo+ldA+dupYes+dupNo+dupA:
            currentVote = aye
        if voteCount == consNo+consYes+consA+labYes+labNo+labA+snpYes+snpNo+snpA+ldYes+ldNo+ldA+dupYes+dupNo+dupA+othYes:
            currentVote = noe
        if voteCount == consNo+consYes+consA+labYes+labNo+labA+snpYes+snpNo+snpA+ldYes+ldNo+ldA+dupYes+dupNo+dupA+othYes+othNo:
            currentVote = didntVote

        
mc.postToChat("Drawing set2")

for x in range(0, 65):
    #print("X: %d, Y: %d, Z: %d" % (-x+65, -z+5+floorLevel, z))
    print(blockCount)
    for z in range(9, 14):
        mc.setBlock(x, z-8+floorLevel, z+1, currentParty)
        mc.setBlock(x, z-8+floorLevel+1, z+1, currentVote)
        blockCount+=1
        voteCount+=1
        if blockCount == 331:
            currentParty = labour
        if blockCount == 563:
            currentParty = snp
        if blockCount == 619:
            currentParty = libDem
        if blockCount == 627:
            currentParty = dup
        if blockCount == 635:
            currentParty = other
        if voteCount == consYes:
            currentVote = noe
        if voteCount == consNo+consYes:
            currentVote = didntVote
        if voteCount == consNo+consYes+consA:
            currentVote = aye
        if voteCount == consNo+consYes+consA+labYes:
            currentVote = noe
        if voteCount == consNo+consYes+consA+labYes+labNo:
            currentVote = didntVote
        if voteCount == consNo+consYes+consA+labYes+labNo+labA:
            currentVote = aye
        if voteCount == consNo+consYes+consA+labYes+labNo+labA+snpYes:
            currentVote = noe
        if voteCount == consNo+consYes+consA+labYes+labNo+labA+snpYes+snpNo:
            currentVote = didntVote
        if voteCount == consNo+consYes+consA+labYes+labNo+labA+snpYes+snpNo+snpA:
            currentVote = aye
        if voteCount == consNo+consYes+consA+labYes+labNo+labA+snpYes+snpNo+snpA+ldYes:
            currentVote = noe
        if voteCount == consNo+consYes+consA+labYes+labNo+labA+snpYes+snpNo+snpA+ldYes+ldNo:
            currentVote = didntVote
        if voteCount == consNo+consYes+consA+labYes+labNo+labA+snpYes+snpNo+snpA+ldYes+ldNo+ldA:
            currentVote = aye
        if voteCount == consNo+consYes+consA+labYes+labNo+labA+snpYes+snpNo+snpA+ldYes+ldNo+ldA+dupYes:
            currentVote = noe
        if voteCount == consNo+consYes+consA+labYes+labNo+labA+snpYes+snpNo+snpA+ldYes+ldNo+ldA+dupYes+dupNo:
            currentVote = didntVote
        if voteCount == consNo+consYes+consA+labYes+labNo+labA+snpYes+snpNo+snpA+ldYes+ldNo+ldA+dupYes+dupNo+dupA:
            currentVote = aye
        if voteCount == consNo+consYes+consA+labYes+labNo+labA+snpYes+snpNo+snpA+ldYes+ldNo+ldA+dupYes+dupNo+dupA+othYes:
            currentVote = noe
        if voteCount == consNo+consYes+consA+labYes+labNo+labA+snpYes+snpNo+snpA+ldYes+ldNo+ldA+dupYes+dupNo+dupA+othYes+othNo:
            currentVote = didntVote

        

        #mc.postToChat("LOL")
print(blockCount)

mc.postToChat("Finished")
