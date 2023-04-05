# 백준 1991 - 실버1
# https://www.acmicpc.net/problem/1991

def preorder(node):
    print(chr(ord('A')+node), end='')
    if graph[node][0] != -1:
        preorder(graph[node][0])
    if graph[node][1] != -1:
        preorder(graph[node][1])

def inorder(node):
    if graph[node][0] != -1:
        inorder(graph[node][0])
    print(chr(ord('A')+node), end='')
    if graph[node][1] != -1:
        inorder(graph[node][1])

def postorder(node):
    if graph[node][0] != -1:
        postorder(graph[node][0])
    if graph[node][1] != -1:
        postorder(graph[node][1])
    print(chr(ord('A')+node), end='')


n = int(input())

graph = [[] for _ in range(26)]

for i in range(n):
    a, b, c = input().split()
    if b == '.':
        graph[ord(a)-ord('A')].append(-1)
    else:
        graph[ord(a)-ord('A')].append(ord(b)-ord('A'))
    if c == '.':
        graph[ord(a)-ord('A')].append(-1)
    else:
        graph[ord(a)-ord('A')].append(ord(c)-ord('A'))
    
# print(graph)
preorder(0) # A부터 순회
print()
inorder(0)
print()
postorder(0)