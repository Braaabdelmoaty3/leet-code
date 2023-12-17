def sumNums(nums,target):
    for x in range (len(nums)):
        for y in range (x + 1 , len(nums)):
            mysum = nums[x] + nums[y]
            if mysum == target:
                return x,y


nums = [3,2,4]
target = 6
print(sumNums(nums,target))
