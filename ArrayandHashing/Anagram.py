def problem(s, t):
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    if sorted_s == sorted_t:
        return True
    return False

def bestSolution(s, t):
    if len(s) != len(t):
            return False
        
    countS, countT = {}, {}
        
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
    return True

def main():
    s = "anagram"
    t = "nagaram"
    print(problem(s, t))

if __name__ == "__main__":
    main()