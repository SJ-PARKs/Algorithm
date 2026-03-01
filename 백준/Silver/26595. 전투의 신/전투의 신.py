n=int(input())
a,pa,b,pb=map(int,input().split())

maximum=0
answer_x,answer_y=0,0
if pa<pb:
    for i in range(n//pb+1):
        y=i
        x=(n-pb*y)//pa
        if maximum<a*x+b*y:
            maximum=a*x+b*y
            answer_x,answer_y=x,y
else:
    for i in range(n//pa+1):
        x=i
        y=(n-pa*x)//pb
        if maximum<a*x+b*y:
            maximum=a*x+b*y
            answer_x,answer_y=x,y

print(answer_x,answer_y)