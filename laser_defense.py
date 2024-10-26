L = 0 # The length of each  side of the square
N = 0 # The number of lines that start from the origin
M = 0 # The  number of lines that start from the point(0, L)


def intersection_points(lines):
    points = []
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            x1, y1, x2, y2 = lines[i]
            x3, y3, x4, y4 = lines[j]
            denom = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
            if denom != 0:
                t = ((x1-x3)*(y3-y4) - (y1-y3)*(x3-x4)) / denom
                u = -((x1-x2)*(y1-y3) - (y1-y2)*(x1-x3)) / denom
                if 0 <= t <= L and 0 <= u <= L:
                    x = x1 + t * (x2-x1)
                    y = y1 + t * (y2-y1)
                    # Check if intersection point lies on the edge of the square
                    if 0 < x < L and 0 < y < L:
                        points.append((x, y))
            # Check for coincident lines
            elif (x1, y1) == (x3, y3) and (x2, y2) == (x4, y4):
                continue
            # Check for lines with zero length
            elif (x1, y1) == (x2, y2) or (x3, y3) == (x4, y4):
                continue
            # Check for lines that lie outside the square
            elif (x1 < 0 and x2 < 0) or (x1 > L and x2 > L) or (y1 < 0 and y2 < 0) or (y1 > L and y2 > L):
                continue
    return points

def count_areas(lines):
    points = intersection_points(lines)
    areas = 1
    for _ in range(len(points)):
        areas += 1
    return areas


def main():
    L_M_N = (input().split(" ")) # Get the  length of each side of the square, the number of lines that start from the origin, and the  number of lines that start from the point(0, L)
    L = int(L_M_N[0]) # get the length of each line of the square
    num_A_lines = int(L_M_N[1])
    num_B_lines = int(L_M_N[2])
    # num_all_lines = num_A_lines + num_B_lines
    lines = [] # store for all the line x1, y1 & x2, y2
    for i in range(num_A_lines): # get the lines that start from the origin
        j = input().split(" ")
        if j[0] == "U":
            x1 = 0
            y1 = 0
            x2 = int(j[1])
            y2 = L
        else:
            x1 = 0
            y1 = 0
            x2 = L
            y2 = int(j[1])
        lines.append((x1, y1, x2, y2))
        
    for i in range(num_B_lines): # get the lines that start from the B point (0, L)
        j = input().split(" ")
        if j[0] == "U":
            x1 = L
            y1 = 0
            x2 = int(j[1])
            y2 = L
        else:
            x1 = L
            y1 = 0
            x2 = 0
            y2 = int(j[1])
        lines.append((x1, y1, x2, y2))
        
    areas = count_areas(lines)
    
    print(areas)

if __name__ == "__main__":
    main()