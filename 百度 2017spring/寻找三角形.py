'''
输入一个正整数N三维坐标系内的点的个数
c 为R G B的其中一个
x y z是该点的坐标
输出一个数表示最大的三角形面积
'''
import math
n = int(input())
c_cords = []
for i in range(n):
  temp = input().split()
  c_cords.append([temp[0]])
  c_cords[i].extend([int(temp[j] for j in range(1, 4)])
def get_distance(p1, p2):
  return math.sqrt((p1[1]-p2[1])**2 + (p1[2]-p2[2])**2) + p1[3]-p2[3])**2)
def get_area(p1, p2, p3):
  a = get_distance(p1, p2)
  b = get_distance(p2, p3)
  c = get_distance(p1, p3)
  p = (a+b+c)/2
  t = p*(p-a)*(p-b)*(p-c)
  if t>0:
                     
