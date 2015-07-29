from mcpi import minecraft
import time
import json


mc = minecraft.Minecraft.create()
chat = mc.postToChat
blockSet = mc.setBlocks
mc.player.setPos(0, -2, 0)
aye = 44, 1
no = 44
noVote = 0
conservative = 35, 11
labour = 35, 14
snp = 35, 4
libDem = 35, 1
other = 35, 7

for x in range(0, 65):
    for z in range(0, 5):
        mc.setBlock(x, 21, z, 1)
