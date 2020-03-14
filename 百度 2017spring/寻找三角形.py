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
    c_cords[i].extend([int(temp[j] for j in range(1, 4))])
def get_distance(p1, p2):
    return math.sqrt((p1[1]-p2[1])**2 + (p1[2]-p2[2])**2 + (p1[3]-p2[3])**2)
def get_area(p1, p2, p3):
    a = get_distance(p1, p2)
    b = get_distance(p2, p3)
    c = get_distance(p1, p3)
    p = (a+b+c)/2
    t = p*(p-a)*(p-b)*(p-c)
    if t>0:
        return math.sqrt(p*(p-a)*(p-b)*(p-c))
    else:
        return 0
    
R=[]
G=[]
B=[]
for each in c_cords:
    if each[0] == 'R':
        R.append(each)
    elif each[0] == 'G':
        G.append(each)
    else:
        B.append(each)

def get_same_color_triangle(color):
    temp_area = []
    length_c = len(color)
    for each1 in c1:
        for each2 in c2:
            for each3 in c3:
                temp_area.append(get_area(color[x], color[y], color[z]))
    return temp_area

def get_different_color_triangle(c1, c2, c3):
    temp_area = []
    for each1 in c1:
        for each2 in c2:
            for each3 in c3:
                temp_area.append(get_area(color[x], color[y], color[z]))
    return temp_area

area = [0]
if len(R)>2:
    area.extend(get_same_color_triangle(R))
if len(G)>2:
    area.extend(get_same_color_triangle(R))
if len(B)>2:
    area.extend(get_same_color_triangle(R))
if R and G and B:
    area.extend(get_different_color_triangle(R, G, B))
print('%.5f' % max(area))
