# Yuan-Chih Hsieh     ID: yvh5398
# Jarod Beaumariage   ID: jfb5691
# Kelvin Ngure        ID: knn5090

# convert input lines into list of integers
def convert_input(l):
    line = l.split()
    line = [int(i) for i in line]
    return line


class graph:
    def __init__(self, v, e, s):
        self.v = v
        self.e = e
        self.s = s
        # dist[s]=0, dist[v]=infinity, if v!=s
        self.dist = {}

    def update(self, i, j):
        if self.dist[i] + j[1] < self.dist[j[0]]:
            self.dist[j[0]] = self.dist[i] + j[1]


    def Bellman_Ford(self):

        for i in self.v:
            if i == self.s:
                self.dist[i] = 0
            else:
                self.dist[i] = 1001

        for k in range(1, len(self.v)):
            for i in self.v:
                if i in self.e:
                    for j in self.e[i]:
                        self.update(i, j)


    def NC(self):
        v_1 = {}
        for i in self.dist:
            v_1[i] = self.dist[i]
        for i in self.v:
            if i in self.e:
                for j in self.e[i]:
                    self.update(i, j)

        if v_1 == self.dist:
            return False
        else:
            return True


# read inputs
line1 = input()
nms = convert_input(line1)
n = nms[0]   # vertices
m = nms[1]   # num of edges
s = nms[2]   # source vertex

v = []
for i in range(n):
    v.append(i+1)

e = {}
for i in range(m):
    read = input()
    edge = convert_input(read)
    if edge[0] not in e:
        e[edge[0]] = [[edge[1], edge[2]]]
    else:
        e[edge[0]].append([edge[1], edge[2]])

test = graph(v, e, s)
test.Bellman_Ford()
print(test.NC())