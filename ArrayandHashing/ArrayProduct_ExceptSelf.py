#must run in O(n) time and no division operator
import math

def mySolution(nums):
    productArr = [1] * (len(nums))
    prefix = 1
    for i in range(len(nums)):
        productArr[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        productArr[i] *= postfix
        postfix *= nums[i]
        print(postfix)
    return productArr


def bestSolution():
     #best solution here
     print()

def main():
    nums = [1, 2, 3, 4]
    print(mySolution(nums))

if __name__ == "__main__":
    main()