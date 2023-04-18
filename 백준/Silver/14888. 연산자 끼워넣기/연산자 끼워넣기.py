n = int(input())
nums = list(map(int, input().split()))
plus, minus, multy, divide = map(int, input().split())

ls = []
maxVal = -1000000000
minVal = 1000000000

def getSequence(n1, n2, n3, n4):
    global maxVal, minVal
    
    if n1 == 0 and n2 == 0 and n3 == 0 and n4 == 0:
        val = nums[0]
        for i in range(n-1):
            if ls[i] == 1:
                val += nums[i+1]
            elif ls[i] == 2:
                val -= nums[i+1]
            elif ls[i] == 3:
                val *= nums[i+1]
            else:
                if val < 0 and nums[i+1] > 0:
                    val *= -1
                    val //= nums[i+1]
                    val *= -1
                else:
                    val //= nums[i+1]
        if maxVal < val:
            maxVal = val
        if minVal > val: minVal = val
        
    else:
        if n1 > 0:
            ls.append(1)
            getSequence(n1-1, n2, n3, n4)
            ls.pop()

        if n2 > 0:
            ls.append(2)
            getSequence(n1, n2-1, n3, n4)
            ls.pop()

        if n3 > 0:
            ls.append(3)
            getSequence(n1, n2, n3-1, n4)
            ls.pop()

        if n4 > 0:
            ls.append(4)
            getSequence(n1, n2, n3, n4-1)
            ls.pop()

getSequence(plus, minus, multy, divide)
print(maxVal)
print(minVal)
