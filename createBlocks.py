from mcpi import minecraft
import time
import json


mc = minecraft.Minecraft.create()
x, y, z = mc.player.getPos()
chat = mc.postToChat
blockSet = mc.setBlocks
vote = input('What vote ID? ')
aye = 44, 1
no = 44
noVote = 0
conservative = 35, 3
labour = 35, 14
snp = 35, 4
libDem = 35, 1
other = 35, 7
blockSet(x+1, y, z+1, x+66, y, z+1, conservative)
