import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def union(num_1, num_2):
    x, y = find(num_1), find(num_2)
    if x > y:
        nodes[x] = y
    else:
        nodes[y] = x


def find(num):
    if nodes[num] != num:
        nodes[num] = find(nodes[num])
    return nodes[num]


n, m = map(int, input().rstrip().split())
nodes = [i for i in range(n + 1)]

for i in range(m):
    command, a, b = map(int, input().rstrip().split())

    if command == 0:
        union(a, b)

    else:
        if find(b) == find(a):
            print('YES')
        else:
            print('NO')