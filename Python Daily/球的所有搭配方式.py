'''
红球3个，黄球3个，绿球6个，把所有球放进一个盒子里面，从其中抽取8个球，求球的所有搭配方式
'''
for red in range(4):
  for yellow in range(4):
    for green in range(7):
      if red + yellow + green == 8:
        print("red = {},".format(red), end = "")
        print("yellow = {},".format(yellow), end = "")
        print("green = {},".format(green), end = "")
        print()
