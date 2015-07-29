for x in range(0, 65):
    print("X: %d, Y: %d, Z: %d" % (-x, -z+5+15, z))
    for z in range(0, 5):
        mc.setBlock(-x, -z+5+15, z, 0)
        #mc.postToChat("LOL")

mc.postToChat("Finished")
