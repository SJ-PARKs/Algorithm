def solution(s):
    answer = True
    
    stack=[]
    for x in s:
        if len(stack)==0:
            stack.append(x)
        elif x=="(":
            stack.append(x)
        elif x==")":
            if stack[-1]=="(":
                stack.pop()
            else:
                stack.append(x)
    if len(stack)!=0:
        answer=False

    return answer