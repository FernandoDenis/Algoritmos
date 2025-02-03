def compareTriplets(a, b):
    score = [0,0]
    for i in range(len(a)):
        if a[i] > b[i]:
            score[0] += 1
        elif a[i] < b[i]:
            score[1] += 1
            
    return score         
   
a = [5,6,7]
b = [3,6,10]

print(compareTriplets(a,b)) # 1 - 1