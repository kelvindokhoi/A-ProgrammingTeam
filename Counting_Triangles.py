# Counting Triangles
# https://open.kattis.com/contests/uba923/problems/countingtriangles
class Secment:
    def __init__(self,slope,offset,x1,x2) -> None:
        self.slope = slope
        self.offset = offset
        self.x1 = x1
        self.x2 = x2
while True:
    num_lines = int(input())
    if num_lines==0:
        break
    total_points = 0
    slopes = [0]*num_lines
    for i in range(num_lines):
        x1,y1,x2,y2 = map(float,input().split())
        slope = (y2-y1)/(x2-x1)
        offset = y1-x1*slope
        if x1>x2:
            x1,x2 = x2,x1
        slopes[i] = Secment(slope,offset,x1,x2)
    for i in range(num_lines):
        for j in range(i+1,num_lines):
            if slopes[i].slope!=slopes[j].slope:
                intersect_x = (slopes[i].offset-slopes[j].offset)/(slopes[j].slope-slopes[i].slope)
                if slopes[i].x1<=intersect_x<=slopes[i].x2 and slopes[j].x1<=intersect_x<=slopes[j].x2:
                    for k in range(j+1,num_lines):
                        if slopes[i]!=slopes[k] and slopes[j]!=slopes[k]:
                            intersect_x_ik = (slopes[i].offset-slopes[k].offset)/(slopes[k].slope-slopes[i].slope)
                            intersect_x_jk = (slopes[j].offset-slopes[k].offset)/(slopes[k].slope-slopes[j].slope)
                            if slopes[i].x1<=intersect_x_ik<=slopes[i].x2 and slopes[k].x1<=intersect_x_ik<=slopes[k].x2 and slopes[j].x1<=intersect_x_jk<=slopes[j].x2 and slopes[k].x1<=intersect_x_jk<=slopes[k].x2:
                                total_points += 1
    print(total_points)