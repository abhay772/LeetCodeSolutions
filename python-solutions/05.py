def longestPalindrome(s: str) -> str:

    start = 0
    end = 0

    for i in range(len(s)):
        len1 = expandFromMiddle(s, i, i)
        len2 = expandFromMiddle(s, i, i+1)
        length = max(len1, len2)

        if length > end - start:
            start = i - ((length - 1) // 2)
            end = i + (length // 2) + 1

    return s[start:end]


def expandFromMiddle(s: str, lower: int, higher: int) -> int:

    while lower > -1 and higher < len(s) and s[lower] == s[higher]:
        higher += 1
        lower -= 1

    return higher - lower - 1


print(longestPalindrome("ababad"))
