import copy
from random import gammavariate

mypuzzle =[[5, 1, 2],[0, 4, 8],[3, 6, 7]]
goalstate = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
 
def print_func( s):
    for i in range(0,3):
        print(s[i])
print('this is a matrix like example ')
print_func(mypuzzle)
print('==========')
print('this is the goal state :')
print_func(goalstate)
print('==========')
def find_index(game):
    for i in range(3):
        for j in range(3):
            if game[i][j] is 0:
                return i, j

def go_left(game):
    x,y = find_index(game)
    if y > 0:
        p = copy.deepcopy(game)
        p[x][y] = p[x][y-1]
        p[x][y-1] = 0
        return p
    else:
        return game
def go_right(game):
    z = find_index(game)
    if z[1] < 2:
        g = copy.deepcopy(game)
        g[z[0]][z[1]] = g[z[0]][z[1]+1]
        g[z[0]][z[1]+1] = 0
        return g
    else:
        return game
def go_up(game):
    x,y= find_index(game)
    if x > 0:
        p = copy.deepcopy(game)
        p[x][y] = p[x-1][y]
        p[x-1][y] = 0
        return p
    else:
        return game
def go_down(game):
    x,y= find_index(game)
    if x < 2:
        p = copy.deepcopy(game)
        p[x][y] = p[x+1][y]
        p[x+1][y] = 0
        return p
    else:
        return game

def actions(game):
    x,y= find_index(game)
    if x == 0 and y== 0:
        return [go_right, go_down]
    elif x== 0 and y ==2:
        return [go_left, go_down]
    elif x== 2 and y== 0:
        return [go_right, go_up]
    elif x== 2 and y==2:
        return [go_left, go_up]
    elif x==0  and y> 0 and y< 2:
        return [go_left, go_right, go_down]
    elif x==2 and y > 0 and y < 2:
        return [go_left, go_right, go_up]
    elif y == 0 and x > 0 and x < 2:
        return [go_right, go_up, go_down]
    elif y == 2 and x > 0 and x < 2:
        return [go_left, go_up, go_down]
    else:
        return [go_right, go_left, go_up, go_down]

def solve(game):
    openlist = [[mypuzzle]]
    closedlist = []
    while openlist:
        path_way = openlist.pop(0)
        node = path_way[-1]
        closedlist.append(node)
        if node == goalstate:
            return path_way
        for action in actions(node):
            child = action(node)
            if child not in closedlist:
                newpath = copy.deepcopy(path_way)
                newpath.append(child)
                openlist.append(newpath)
    return "Failure"

l1=(solve(mypuzzle))
for i  in range(len(l1)):
    for j in range(3):
        for k in range(3):
            if l1[i][j][k]==0:
                m=j
                p=k+m

    print ( l1[i] )  
    print("the heuristic value h is  " +str(p) ) 
    print("------")         



