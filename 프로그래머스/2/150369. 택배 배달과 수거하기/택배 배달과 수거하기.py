from collections import deque
def solution(cap, n, deliveries, pickups):
    answer = 0
    while len(deliveries) or len(pickups):
        while len(deliveries) and deliveries[-1] == 0:
            deliveries.pop()
        while len(pickups) and pickups[-1] == 0:
            pickups.pop()
        answer += 2 * (max(len(deliveries), len(pickups)))
        update(deliveries,cap)
        update(pickups,cap)
        
    return answer
def update(graph, cap):
    while len(graph):
        if graph[-1] > cap:
            graph[-1] -= cap
            break
        else:
            cap -= graph[-1]
            graph.pop()
            
            
    
    
        
            
            
        