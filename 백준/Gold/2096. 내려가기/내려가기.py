n = int(input())
scores = list(map(int, input().split()))
maxscores = scores
minscores = scores

for _ in range(n-1):
    scores = list(map(int, input().split()))
    maxscores = [scores[0]+ max(maxscores[:2]), scores[1]+ max(maxscores), scores[2]+ max(maxscores[1:])]
    minscores = [scores[0]+ min(minscores[:2]), scores[1]+ min(minscores), scores[2]+ min(minscores[1:])]

print(max(maxscores), min(minscores))