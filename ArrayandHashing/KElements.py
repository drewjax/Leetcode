
def mySolution(nums, k):
    # This code exceded the time limit, but works the same
    #nums.sort()
    #j = 1
    #i = 0
    #uniqueNum = []
    #cntNum = []
    #for i in range(len(nums)):
    #    cnt = 0
    #    for j in range(len(nums)):
    #        if (nums[i] == nums[j]):
    #            cnt += 1
    #   if nums[i] not in uniqueNum:
    #        uniqueNum.append(nums[i])
    #        cntNum.append(cnt)

    count = {}
    freq = [[] for i in range(len(nums) + 1)]
    
    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)
    finalAns = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            finalAns.append(n)
            if len(finalAns) == k:
                return finalAns
        

def bestSolution(nums, k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]
    
    for n in nums:
        count[n] = 1 + count.get(n, 0)
    print(count)
    for n, c in count.items():
        freq[c].append(n)
    
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

def main():
    nums = [1, 2, 3, 1, 1, 3, 2, 2, 2, 2]
    print(mySolution(nums, 2))

if __name__ == "__main__":
    main()