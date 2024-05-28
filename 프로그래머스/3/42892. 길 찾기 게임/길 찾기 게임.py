class Node:
    def __init__(self, info, num, left=None, right=None):
        self.info = info
        self.num = num
        self.left = left
        self.right = right
        
    def has_left(self):
        return self.left is not None # 왼쪽 자식이 있으면 True, 없으면 False
    
    def has_right(self):
        return self.right is not None # 오른쪽 자식이 있으면 True, 없으면 False

    
def make_BT(nodeinfo):
    node_number = [i for i in range(1, len(nodeinfo) + 1)]
    node_number.sort(key=lambda x:(nodeinfo[x-1][1], -nodeinfo[x-1][0]), reverse=True)
    root = None
    for i in range(len(nodeinfo)): # 0~9
        if root is None:
            root = Node(nodeinfo[node_number[0]-1], node_number[0])
        else:
            parent = root # 4번 노드의 부모는 루트인 7번 노드
            current_node = Node(nodeinfo[node_number[i]-1], node_number[i])
            
            while True:
                if current_node.info[0] < parent.info[0]: # 부모보다 왼쪽에 있으면
                    if parent.has_left(): # 만약 왼쪽 자식이 있으면 그 왼쪽 자식을 현재 노드의 부모로 하고 넘어가야 함
                        parent = parent.left
                        continue
                    else: # 만약 왼쪽 자식이 없으면 현재 노드가 부모의 왼쪽 자식이 됨
                        parent.left = current_node
                        break # 제 위치를 찾았으니 while 문을 빠져나와서 다음 노드를 확인하러 가야됨

                elif current_node.info[0] > parent.info[0]:
                    if parent.has_right():
                        parent = parent.right
                        continue
                    else:
                        parent.right = current_node
                        break
    return root


def pre_order(root, answer):
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        if node is None:
            continue
        answer[0].append(node.num)
        stack.append(node.right)
        stack.append(node.left)
    
    
def post_order(root, answer):
    stack = []
    stack.append((root, False))
    while stack:
        node, visited = stack.pop()
        if node is None:
            continue
        if visited:
            answer[1].append(node.num)
        else:
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))
    
    
def solution(nodeinfo):
    answer = [[],[]]
    root = make_BT(nodeinfo)
    pre_order(root, answer)
    post_order(root, answer)
    
    
    return answer




'''
이진트리 만들기 : 노드를 만드는 걸 계속 반복하면됨. 현재 노드의 정보, 왼쪽 자식 및 오른쪽 자식 여부, parent를 누구로 해주는지. 이렇게 정의하면 끝!

<정의해야 할 것>
- 노드 만들기
- 이진트리 만들기 (노드 만들기를 기반으로 해야겠지?)
'''