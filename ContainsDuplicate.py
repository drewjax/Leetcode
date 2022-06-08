def problem(nums) -> bool:
    hashset = set()
    
    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)
    return False

def main():
    nums = [1, 2, 3, 1]
    print(problem(nums))

if __name__ == "__main__":
    main()
    