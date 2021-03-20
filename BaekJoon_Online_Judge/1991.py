import sys

input = sys.stdin.readline

tree = {}
result = []

def preorder_traversal(a):
    if a == '.':
        return
    
    result.append(a)
    preorder_traversal(tree[a][0])
    preorder_traversal(tree[a][1])


def inorder_traversal(a):
    if a == '.':
        return
    
    inorder_traversal(tree[a][0])
    result.append(a)
    inorder_traversal(tree[a][1])

def postorder_traversal(a):
    if a == '.':
        return

    postorder_traversal(tree[a][0])
    postorder_traversal(tree[a][1])
    result.append(a)

def print_result():
    for x in result:
        print(x, end='')
    print()
    result.clear()

N = int(input())
for _ in range(N):
    n, l, r = input().split()
    tree[n] = (l, r)
    
preorder_traversal("A")
print_result()
inorder_traversal("A")
print_result()
postorder_traversal("A")
print_result()
