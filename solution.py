# convert input lines into list of integers
def convert_input(l):
    line = l.split()
    line = [int(i) for i in line]
    return line



# priority queue
class PQ:
    def __init__(self):
        self.bh = []    # first store value, second store number

    def bubble_up(self, k):
        if k == 0:
            pass
        else:
            p = (k-1) // 2
            if self.bh[p][0] > self.bh[k][0]:
                temp = self.bh[p]
                self.bh[p] = self.bh[k]
                self.bh[k] = temp
                self.bubble_up(p)

    def siftdown(self, k):
        if 2*k+1 >= len(self.bh):
            return
        elif 2*k+2 >= len(self.bh):
            c = 2*k+1
        else:
            if self.bh[2*k+1][0] <= self.bh[2*k+2][0]:
                c = 2*k+1
            else:
                c = 2*k+2
        if self.bh[k][0] > self.bh[c][0]:
            temp = self.bh[k]
            self.bh[k] = self.bh[c]
            self.bh[c] = temp
            self.siftdown(c)
        
    def insert(self, val, num):
        self.bh.append([val, num])
        self.bubble_up(len(self.bh)-1)

    def empty(self):
        if len(self.bh) == 0:
            return True
        else:
            return False

    def find_min(self):
        return self.bh[0]

    def del_min(self):
        n = self.bh.pop()
        if len(self.bh) != 0:
            self.bh[0] = n
            self.siftdown(0)
        else:
            pass
    
    def decrease_key(self, k, val):
        n = 0
        while n < len(self.bh):
            if self.bh[n][1] == k:
                self.bh[n][0] = val
                break
            else:
                n += 1
        self.bubble_up(n)



# find shortest path
def Dijkstra(v, e, s):
    dist = []
    pq = PQ()
    for i in range(1, v+1):
        dist.append(1001)
        pq.insert(1001, i)
    dist[s-1] = 0
    pq.decrease_key(s, 0)
    while pq.empty() == False:
        cur = pq.find_min()
        pq.del_min()
        if cur[1] not in e:
            pass
        else:
            for v in e[cur[1]]:
                if dist[v[0]-1] > dist[cur[1]-1] + v[1]:
                    dist[v[0]-1] = dist[cur[1]-1] + v[1]
                    pq.decrease_key(v[0], dist[v[0]-1])

    return dist



# read inputs
line1 = input()
nms = convert_input(line1)
v = nms[0]   # vertices
e = nms[1]   # num of edges
s = nms[2]   # source vertex
adj_e = {}   # first index is to which vertex, second is edge-length
for i in range(e):
    read = input()
    edge = convert_input(read)
    if edge[0] not in adj_e:
        adj_e[edge[0]] = [[edge[1], edge[2]]]
    else:
        adj_e[edge[0]].append([edge[1], edge[2]])

short_path = Dijkstra(v, adj_e, s)

for i in range(len(short_path)):
    if short_path[i] >= 1001:
        short_path[i] = -1
        print(short_path[i])
    else:
        print(short_path[i])