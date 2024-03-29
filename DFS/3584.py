# boj, 3584: 가장 가까운 공통 조상,python3
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N=int(sys.stdin.readline())
    p_list=[0 for _ in range(N+1)]      
    for _ in range(N-1):
        p,c=map(int,sys.stdin.readline().split())
        p_list[c]=p
    print(p_list)

    a, b = map(int, sys.stdin.readline().split())
    a_parent = [a]
    b_parent = [b]

    # 각 노드의 부모노드가 루트일때까지 모두 저장
    while p_list[a]:
        a_parent.append(p_list[a])
        a = p_list[a]
    
    while p_list[b]:
        b_parent.append(p_list[b])
        b = p_list[b]
    a_level = len(a_parent)-1
    b_level = len(b_parent)-1

    # 부모노드가 같지 않을 때까지
    while a_parent[a_level] == b_parent[b_level]:
        a_level -= 1
        b_level -= 1
    print(a_parent[a_level + 1])


