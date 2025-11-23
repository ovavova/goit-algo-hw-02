


def symmetry(s: str) -> bool:
    open = "({[" 
    close = ")}]"
    match = {")": "(",
            "}": "{",
            "]": "["
            }
    stack = []
    for sym in s:
        if sym in open:
            stack.append(sym)
        elif sym in close:
            if not stack:
                return f"Не симетрично" 
            top = stack.pop()
            if match[sym] != top:
                return f"Не симетрично"
    if stack:
        return f"Не симетрично"
    else:
        return f"Симетрично"

            


s = "( ){[ 1 ]( 1 + 3 )( ){ }}"
d = "( 23 ( 2 - 3)"
l = "( 11 }"

print(symmetry(s))
print(symmetry(d))
print(symmetry(l))

