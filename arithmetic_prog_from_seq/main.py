
def canMakeArithmeticProgression(arr):
    arr.sort()
    diff = arr[1] - arr[0]
    return all(x == arr[0] + i*diff for i,x in enumerate(arr))

        

canMakeArithmeticProgression([-13,-17,-8,-10,-20,2,3,-19,2,-18,-5,7,-12,18,-17,12,-1])