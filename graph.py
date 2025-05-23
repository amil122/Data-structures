
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^---GRAPH--^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
def add_node_matrix(v):
    global node_count
    if v in nodes_matrix:
        print('the given node is in the graph')
    else:
        node_count = node_count + 1
        nodes_matrix.append(v)
        for n in graph_matrix:
            n.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph_matrix.append(temp)
        print(graph_matrix,"after appending temp")


def add_edge_matrix(v1,v2):
    if v1 not in nodes_matrix:
        print('it is not there')
    elif v2 not in nodes_matrix:
        print('it is not here')
    else :
        index1= nodes_matrix.index(v1)
        index2 = nodes_matrix.index(v2)
        print('this is index1',index1,v1)
        print('this is index2',index2,v2)
        graph_matrix[index1][index2]= 1
        graph_matrix[index2][index1] = 1

def delete_matrix(v):
    global node_count
    if v not in nodes_matrix:
        print('it is not in the list')
    else :
        index1 = nodes_matrix.index(v)
        node_count = node_count-1
        nodes_matrix.remove(v)
        for i in graph_matrix:
            i.pop(index1)

def delete_edge_matrix(v1,v2):
    if v1 and v2 not in nodes_matrix:
        print('the given vertices are not present in the graph')
    else :
        index1 = nodes_matrix.index(v1)
        index2 = nodes_matrix.index(v2)
        graph_matrix[index1][index2] = 0
        graph_matrix[index2][index1] = 0

from collections import deque

def BFS(start_node, graph):
    visited = set()
    queue = deque([(start_node, 0)])  # Tuple: (node, cost)
    while queue:
        current_node, cost = queue.popleft()
        print(current_node,'current node')
        if current_node not in visited:
            print(f"Node: {current_node}, Cost: {cost}")
            visited.add(current_node)
            for neighbor, edge_weight in graph[current_node]:
                if neighbor not in visited:
                    queue.append((neighbor, edge_weight))
                
def DFS(node,visited,graph):
    if node not in graph:
        print('it is not there')
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i[0],visited,graph)
            
def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph_matrix[i][j],'<4' ),end=' ')  
        print()  
        
nodes_matrix = []
graph_matrix = []
node_count = 0
add_node_matrix('A')
add_node_matrix('B')
add_node_matrix('C')
add_node_matrix('D')
add_node_matrix('E')

add_edge_matrix('A','B')
add_edge_matrix('A','D')
add_edge_matrix('B','E')

print(nodes_matrix)




print_graph()


        
def add_node_list(v):
    if v in graph_list:
        print('the given node i spresent in the list')
        return
    graph_list[v]= []

def add_edge_list(v1,v2,cost):
    if v1 not in graph_list:
        print('the given node is not present in the tree')
    elif v2 not in graph_list:
        print('the given node os not present in the tree')
    else :
        list1 = [v2,cost]
        list2 = [v1,cost]
        graph_list[v1].append(list1)
        graph_list[v2].append(list2)
        
def delete_node_list(v):
    if v not in graph_list:
        print('it is not there in the graph')
    else:
        graph_list.pop(v)
        for adj_list in graph_list.values():
            for pair in adj_list:
                if pair[0] == v:
                    adj_list.remove(pair)


def delete_edge_list(v1,v2,cost):
    if v1 and v2 not in graph_list:
        print('the given vertex is not present in the graph ')
    else :
        temp = [v2,cost]
        temp1= [v1,cost]
        if temp in graph_list[v1]:
            graph_list[v1].remove(temp)
            graph_list[v2].remove(temp1)
            
def dfs(node,visited,graph):    
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            dfs(i[0],visited,graph)

from collections import deque
def bfs(start_node,graph):
    visited = set()
    queue = deque([(start_node,0)])
    while queue :
        current_node,cost = queue.popleft()
        if current_node not in visited:
            print(current_node)
            visited.add(current_node)
            for i in graph[current_node]:
                if i[0] not in visited:
                    queue.append(i)
    
    
    
    
    
visited = set()   
graph_list = {}
add_node_list("A")
add_node_list("B")
add_node_list("C")
add_node_list("D")
add_edge_list('A','B',10)
add_edge_list('A','C',20)
add_edge_list('C','D',30)
delete_edge_list('A','B',10)
# dfs("A",visited,graph_list)
bfs("A",graph_list)
