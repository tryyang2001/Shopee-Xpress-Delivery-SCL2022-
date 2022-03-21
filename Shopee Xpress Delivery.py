# Shopee Code League
# Problem description
"""
Shopee Xpress Delivery

The first line contains two numbers

"""
import sys
import copy
from queue import PriorityQueue

black_holes = dict()
connections = dict()

def print_matrix(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            print(map[i][j], end=" | ")
        print()

map = list()
ROW, COL = 0, 0

line_num = 0
first_line = sys.stdin.readline().split()
ROW, COL = int(first_line[0]), int(first_line[1])

for i in range(ROW):
    line = sys.stdin.readline().split()
    map.append([])
    for char in line:
        map[line_num].append(int(char))
    line_num += 1

for row in range(len(map)):
    for col in range(len(map[row])):
        if map[row][col] > 0:
            if (map[row][col] not in black_holes):
                black_holes[map[row][col] ] = []
            black_holes[map[row][col]].append((row, col))

no_cost = dict()
for value in black_holes:
    for pos in black_holes[value]:
        no_cost[pos] = value
        holes = copy.deepcopy(black_holes[value])
        holes.pop(holes.index(pos))
        if pos not in connections:
            connections[pos] = []
        for each in holes:
            connections[pos].append(each)

def is_within_limit(row, col):
    return row < ROW and col < COL and row >= 0 and col >= 0

class DeliveryMan:
    def __init__(self, curr_pos):
        self.pos = curr_pos

    def get_next_positions(self, curr_pos):
        pos = list()
        row, col = curr_pos[0], curr_pos[1]
        if  col + 1 < COL and (row, col + 1) not in reached:
            pos.append((row, col + 1))
        if  row + 1 < ROW and (row + 1, col) not in reached:
            pos.append((row + 1, col))
        if  row - 1 >= 0 and (row - 1, col) not in reached:
            pos.append((row - 1, col))
        if  col - 1 >= 0 and (row, col - 1) not in reached:
            pos.append((row, col - 1))
        if curr_pos in connections:
            for each in connections[curr_pos]:
                if each not in reached:
                    pos.append(each)
        for each in pos:
            assert is_within_limit(each[0], each[1])
        return pos
    def update_pos(self,pos):
        self.pos = pos

parent = dict()
reached = set()
goal = tuple()
"""
at start (0,0) to end (M - 1, N - 1), at most M down and N right required
"""
def search():
    start = (0, 0)
    goal = (ROW - 1, COL - 1)
    deliveryman = DeliveryMan(start)
    frontier = PriorityQueue()
    frontier.put((0, deliveryman.pos))
    action_count = 0
    while not frontier.empty():
        curr = frontier.get()
        curr_cost = curr[0]
        curr_pos = curr[1]
        deliveryman.update_pos(curr_pos)
        if curr_pos in reached:
            continue
        reached.add(curr_pos)
        if is_goal(curr_pos, goal):
            return curr_cost
        expand = deliveryman.get_next_positions(curr_pos)
        for next in expand:
            if is_teleported(curr_pos, next):
                frontier.put((curr_cost, next))
            else:
                frontier.put((curr_cost + 1, next))
    return None

def is_teleported(node, parent):
    return (node in connections and parent in connections and no_cost[node] == no_cost[parent])

def is_goal(curr, goal):
    return curr[0] == goal[0] and curr[1] == goal[1]

print(search())