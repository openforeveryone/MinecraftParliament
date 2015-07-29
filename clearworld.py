from mcpi import minecraft
import time
mc = minecraft.Minecraft.create()
tp = mc.player.setPos
floorLevel = 15
mc.postToChat("Starting Clear!")
mc.setBlocks(-1, 0, -1, 65, 30, 15, 5)
mc.setBlocks(-5, floorLevel-30, -5, 69, floorLevel+30, 19, 0)
mc.setBlocks(-1, floorLevel, -1, 65, floorLevel, 15, 5)
mc.postToChat("Finished!")
tp(32.5,16,7.5)
mc.postToChat("Building MPs")
#mc.setBlocks(0, floorLevel+5, 0, 64, floorLevel+5, 0, 35, 11)
#mc.setBlocks(0, floorLevel+4, 1, 64, floorLevel+4, 1, 35, 11)
#mc.setBlocks(0, floorLevel+3, 2, 64, floorLevel+3, 2, 35, 11)
#mc.setBlocks(0, floorLevel+2, 3, 64, floorLevel+2, 3, 35, 11)
#mc.setBlocks(0, floorLevel+1, 4, 64, floorLevel+1, 4, 35, 11)

#for x in range(0, 6):
    
