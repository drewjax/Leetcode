import collections


def mySolution(strs):
    strsCopy = []
    sortedStrings = []
    for str in strs:
        strsCopy.append(str)
        str = sorted(str)
        sortedStrings.append(str)
    groupedStrs = []
    i = 0
    j = 0
    blackMark = []
    for i in range(len(strs)):
        tempStr = []
        for j in range(len(strs)):
            if (sortedStrings[i] == sortedStrings[j]):
                if (j not in blackMark):
                    tempStr.append(strs[j])
                    blackMark.append(j)
        if (tempStr):
            groupedStrs.append(tempStr)
    return groupedStrs



def bestSolution(strs):
    ans = collections.defaultdict(list)
        
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        ans[tuple(count)].append(s)
    return ans.values()

def main():
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(mySolution(strs))

if __name__ == "__main__":
    main()