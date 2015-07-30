from mcpi import minecraft
mc = minecraft.Minecraft.create()
consYes = 300
consNo = 30
consA = 1
labYes = 30
labNo = 200
labA = 2
snpYes = 10 
snpNo = 40
snpA = 6
ldYes = 3
ldNo = 5
ldA = 0
dupYes = 2
dupNo = 6
dupA = 0
othYes = 5
othNo = 5
othA = 5

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
