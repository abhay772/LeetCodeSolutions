def longestPalindrome(s: str) -> str:
    Max=s[0]
    if len(s)==1 or s==s[::-1]:
        return s

    for left in range(len(s)):
        right=left+len(Max)

        while(right<len(s)):
            
            if s[left:right+1]==s[left:right+1][::-1]:
                if len(Max)<len(s[left:right+1]):
                    Max=s[left:right+1]
            right+=1
        #print(s[left:right+1])
    return Max
