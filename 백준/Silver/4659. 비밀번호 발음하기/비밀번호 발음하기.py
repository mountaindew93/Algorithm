import sys
input = sys.stdin.readline
arr = ['a', 'e', 'i', 'o', 'u']

while True:
    st = input().strip()
    
    if st == 'end': break
    
    chk = False
    a = True

    for char in st:
        if char in arr:
            chk = True
            break
            
    if not chk:
        a = False
        
    if a:
        for i in range(len(st)):
            if i < len(st) - 2:
                is_v1 = st[i] in arr
                is_v2 = st[i+1] in arr
                is_v3 = st[i+2] in arr
                if (is_v1 and is_v2 and is_v3) or (not is_v1 and not is_v2 and not is_v3):
                    a = False
                    break

            if i < len(st) - 1:
                if st[i] == st[i+1]:
                    if st[i] not in ['e', 'o']:
                        a = False
                        break

    if a:
        print(f'<{st}> is acceptable.')
    else:
        print(f'<{st}> is not acceptable.')