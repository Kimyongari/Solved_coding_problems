import heapq as hq
def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)
    while scoville[0] < K:
        answer += 1
        a = hq.heappop(scoville)
        b = hq.heappop(scoville)
        c = a + (2 * b)
        hq.heappush(scoville, c)
        if len(scoville) == 2 and (scoville[0] + (2 * scoville[1])) < K:
            return -1
    return answer

# 스코빌 = 가장안매운거 + (두번째로 안매운거 * 2)