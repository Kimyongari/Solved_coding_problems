d = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}
days =['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
month, day = map(int,input().split())
dd = sum([d[i] for i in range(1,month)])+day
print(days[dd % 7-1])