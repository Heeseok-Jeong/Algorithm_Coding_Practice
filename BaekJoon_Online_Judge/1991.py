import sys

input = sys.stdin.readline

tree = ['.' for _ in range(2*(26+2))]
result = []

def alpha2index(a):
    for i in range(2*(26+2)):
        if tree[i] == a:
            break
    # print(a, i)
    return i

def preorder_traversal(a):
    if a == '.':
        return
    
    if alpha2index(a)*2 >= 2*(26+1):
        result.append(a)
        return

    result.append(a)
    preorder_traversal(tree[alpha2index(a)*2])
    preorder_traversal(tree[alpha2index(a)*2 + 1])


def inorder_traversal(a):
    if a == '.':
        return
    
    if alpha2index(a)*2 >= 2*(26+1):
        result.append(a)
        return

    inorder_traversal(tree[alpha2index(a)*2])
    result.append(a)
    inorder_traversal(tree[alpha2index(a)*2 + 1])

def postorder_traversal(a):
    if a == '.':
        return

    if alpha2index(a)*2 >= 2*(26+1):
        result.append(a)
        return

    postorder_traversal(tree[alpha2index(a)*2])
    postorder_traversal(tree[alpha2index(a)*2 + 1])
    result.append(a)

def print_result():
    for x in result:
        print(x, end='')
    print()
    result.clear()

N = int(input())
tree[1] = "A"
for _ in range(N):
    n, l, r = input().split()
    tree[alpha2index(n)*2] = l
    tree[alpha2index(n)*2 + 1] = r
# print(tree)
    
preorder_traversal("A")
print_result()
inorder_traversal("A")
print_result()
postorder_traversal("A")
print_result()
