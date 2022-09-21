import sys  # 导入sys模块

sys.setrecursionlimit(100010)  # 将默认的递归深度修改为3000


def dfs(child, father):
    global maxDist
    for i in range(len(neighbor[child])):
        cnt = neighbor[child][i]  # child节点相连的节点
        if cnt != father:  # 无需向父节点方向找,否则会陷入死循环
            dfs(cnt, child)  # 深度优先遍历
            if colorStr[cnt - 1] != colorStr[child - 1]:  # 相邻节点颜色不同
                # distLeaf[child]代表以child为根节点到叶子节点当前已找到的最大距离
                # distLeaf[cnt] + 1代表以child为根节经过cnt节点再到叶子节点的最大距离
                maxDist = max(maxDist, distLeaf[child] + distLeaf[cnt] + 1)
                distLeaf[child] = max(distLeaf[child], distLeaf[cnt] + 1)


n = int(input())  # 节点数
colorStr = input()  # 各节点颜色
maxDist = 0
distLeaf = [0 for i in range(n + 1)]  # distLeaf[i]代表以i为根节点到叶子节点的最大距离
neighbor = [[] for i in range(n + 1)]  # neighbor[i]代表与i节点相连的节点
for i in range(n - 1):
    a, b = map(int, input().split())
    neighbor[a].append(b)
    neighbor[b].append(a)
dfs(1, 0)
print(maxDist)
