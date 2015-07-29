from mcpi import minecraft
import time

mc = minecraft.Minecraft.create()
chat = mc.postToChat
chat("Hello World! This is YRS")
x, y, z = mc.player.getPos()
time.sleep(1)
chat("Get ready to drop!")
time.sleep(0.5)
chat("3")
time.sleep(1)
chat("2")
time.sleep(1)
chat("1")
time.sleep(1)
mc.player.setPos(x, y+100, z)
chat("WHEEEEEEE!")



