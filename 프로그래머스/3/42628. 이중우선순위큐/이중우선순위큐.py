import heapq as h
def solution(operations):
    heap = []
    for i in operations:
        if i[0] == "I":
            h.heappush(heap, int(i[2:]))
        if i == "D -1":
            if len(heap) != 0:
                heap.pop(0)
        if i == "D 1":
            if len(heap) != 0:
                heap.pop(-1)
    if len(heap) != 0:
        return (max(heap), min(heap))
    else:
        return([0,0])