from mcpi import minecraft
mc = minecraft.Minecraft.create()
floorLevel = 15
blockCount = 0
aye = 44, 1
no = 44
noVote = 0
conservative = 35, 11
labour = 35, 14
snp = 35, 4
libDem = 35, 1
dup = 87
other = 35, 7
currentParty = conservative

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
    print(blockCount)
    for z in range(0, 5):
        mc.setBlock(x, -z+5+floorLevel, z, currentParty)
        blockCount+=1
        
        
mc.postToChat("Drawing set2")

for x in range(0, 65):
    #print("X: %d, Y: %d, Z: %d" % (-x+65, -z+5+floorLevel, z))
    print(blockCount)
    for z in range(9, 14):
        mc.setBlock(x, z-8+floorLevel, z+1, currentParty)
        blockCount+=1
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
        

        #mc.postToChat("LOL")
print(blockCount)

mc.postToChat("Finished")
