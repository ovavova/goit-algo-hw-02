from collections import deque


def is_polindrom (s: str) -> bool:
    s_formated = s.strip().lower()
    len_half= len(s_formated) // 2
    de = deque()

    for i in range(len_half):
        de.append(s_formated[i])
    for i in range(len(s_formated)-len_half, len(s_formated)):
        if s_formated[i] != de.pop():
            return False
    return True
    
a ="Able was I ere I saw Elba" # True
b ="rotator"                   # True
c = "left right"               # False
d = "      level "                    # True 
 
print(is_polindrom(a))
print(is_polindrom(b))
print(is_polindrom(c))
print(is_polindrom(d))







