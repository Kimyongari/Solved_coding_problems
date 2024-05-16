def solution(n):
    def move(start, target):
        return [[start, target]]

    def hanoi(n, start, target, auxiliary):
        if n == 1:
            return move(start, target)
        else:
            steps = []
            steps += hanoi(n-1, start, auxiliary, target)
            steps += move(start, target)
            steps += hanoi(n-1, auxiliary, target, start)
            return steps

    return hanoi(n, 1, 3, 2)  # 기둥 번호는 1, 2, 3

