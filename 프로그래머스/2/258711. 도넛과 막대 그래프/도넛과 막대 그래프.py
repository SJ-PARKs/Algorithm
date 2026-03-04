def solution(edges):
    answer = []
    node=[]
    for i in range(len(edges)):
        node.append(edges[i][0])
        node.append(edges[i][1])
    node=list(set(node))
    
    graph=dict()
    for i in range(len(node)):
        graph[node[i]]=[0,0]
        
    for i in range(len(edges)):
        graph[edges[i][0]][0]+=1
        graph[edges[i][1]][1]+=1

    total,one,two,three=0,0,0,0
    for key,value in graph.items():
        if value[0]>=2 and value[1]==0:
            total=value[0]
            answer.append(key)
        if value[0]>=2 and value[1]>=2:
            one+=1
        if value[1]>=1 and value[0]==0:
            two+=1

    three=total-one-two
    
    answer.append(three)
    answer.append(two)
    answer.append(one)
    
    return answer