gas = [5,1,2,3,4]
cost = [4,4,1,5,1]
tank  = 0
thecostlist = []
a = 0
n = len(gas)
j = 0
for i in range(n):
    thecostlist.append(gas[i] - cost[i])
k = 0
if sum(thecostlist) < 0 :
    print(-1)
while j < n:
    print(a,j,k,tank)
    if (thecostlist[a] + tank) < 0:
        a = a + 1
        k = a
        tank = 0
    else:
        tank = tank + thecostlist[a]
        j = j + 1
        a = a + 1
        if a >= n:
            a = a - n
        if tank < 0:
            j = 0
            a = k + 1
print(k)
###官方题解虽然想法一样，但还是优雅的多。。。。。。