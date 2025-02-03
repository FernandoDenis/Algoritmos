# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
# You are given  scores. Store them in a list and find the score of the runner-up.

# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

arr = [57,57,-57,57]

# si declaras winner = int() este tendra el valor de 0, por lo que no funciona para este problema

winner = -101 # En el problema el numero mas pequeño a agregar es -100
runnerUp = -101
for score in arr:
    if score > winner:
        runnerUp = winner
        winner = score
    elif runnerUp < score and score != winner:
        runnerUp = score

nuevaVar = float()
print(nuevaVar)