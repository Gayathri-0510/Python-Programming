def notes(a):
    cnt=0
    if a>=2000:
        cnt+=a//2000
        a=a%2000
    if a>=500:
        cnt += a//500
        a=a%500
    if a>=200:
        cnt+= a//200
        a=a%200
    if a>=100:
        cnt+= a//100
        a=a%100
    if a>=50:
        cnt+=a//50
        a=a%50
    if a>=20:
        cnt+=a//20
        a=a%20
    if a>=10:
        cnt+=a//10
        a=a%10
    print(cnt)
notes(700)
notes(1500)
 
