import sys
def modul(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 1
    if a>20 or b>20 or c>20:
        return modul(20,20,20)
    if w[a][b][c]==0:
        if a<b<c:
            w[a][b][c]=modul(a,b,c-1)+modul(a,b-1,c-1)-modul(a,b-1,c)
        else:
            w[a][b][c]=modul(a-1, b, c) + modul(a-1, b-1, c) + modul(a-1, b, c-1) - modul(a-1, b-1, c-1)
    return w[a][b][c]

#조건이 -50<=a,b,c<=50이지만 셋 중 하나라도 음수가 되면 1을 return하므로 양수일때만 생각해주면 된다.
w=[[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
while True:
    a,b,c=map(int,sys.stdin.readline().split())
    if a==b==c==-1:
        break
    print('w({}, {}, {}) = {}'.format(a,b,c,modul(a,b,c)))
