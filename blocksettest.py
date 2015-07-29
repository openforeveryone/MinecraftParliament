from mcpi import minecraft
import time

mc = minecraft.Minecraft.create()
chat = mc.postToChat
x, y, z = mc.player.getPos()
tp = mc.player.setPos
blockSet = mc.setBlock

blockSet(x+1, y, z, 1)
