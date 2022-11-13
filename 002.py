class DirectedGraphNode:
    def __init__(self, x=None):
        self.label = x
        self.neighbors = []


def topSort(graph_):
    nodeInfo = dict()
    for g in graph_:
        for ng in g.neighbors:
            nodeInfo[ng] = nodeInfo.get(ng, 0) + 1
    zeroQueue = []
    for g in graph_:
        if nodeInfo.get(g, 0) == 0:
            zeroQueue.append(g)
    r = []
    while len(zeroQueue):
        tg = zeroQueue.pop(0)
        r.append(tg.label)
        for g in tg.neighbors:
            nodeInfo[g] -= 1
            if nodeInfo[g] == 0:
                zeroQueue.append(g)
    if not r:
        return -1
    return " ".join(r)


def get_input():
    input_data = input().split(' ')
    f = int(input_data[0])
    s = int(input_data[1])
    return f, s


if __name__ == '__main__':
    m, n = get_input()
    graph = DirectedGraphNode().neighbors
    for i in range(1, m + 1):
        temp = DirectedGraphNode(str(i))
        graph.append(temp)

    for j in range(n):
        l, f = get_input()
        graph[l - 1].neighbors.append(graph[f - 1])

    print(topSort(graph))
