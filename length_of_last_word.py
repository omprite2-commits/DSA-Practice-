def lengthOfLastWord(s):
    s = s.strip()
    return len(s.split()[-1])