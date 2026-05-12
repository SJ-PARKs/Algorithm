def solution(message, spoiler_ranges):
    answer = 0

    
    # words: 단어 배열, words_locate:처음과 끝만
    words=[]
    words_locate=[]
    words_set=set()
    
    w=""
    flag=True
    s=0
    for i in range(len(message)):
        if message[i]==" ":
            if w!="":
                words.append(w)
                words_locate.append([s,i-1])
                flag=True
            w=""
        else:
            if flag:
                s=i
                flag=False
            w+=message[i]
            
    if w != "":
        words.append(w)
        words_locate.append([s, len(message)-1])

    # 스포 방지 된 단어인지 체크하는 배열    
    chk=[0 for _ in range(len(words))]
    
    for i in range(len(spoiler_ranges)):
        start,end=spoiler_ranges[i][0],spoiler_ranges[i][1]
        for j in range(len(words_locate)):
            if start<=words_locate[j][0]<=end or start<=words_locate[j][1]<=end:
                chk[j]=1
            if words_locate[j][0]<=start<=words_locate[j][1] or words_locate[j][0]<=end<=words_locate[j][1]:
                chk[j]=1
    
    for i in range(len(words)):
        if chk[i]==0:
            words_set.add(words[i])
    
    for i in range(len(words)):
        if chk[i]==1:
            if words[i] not in words_set:
                answer+=1
                words_set.add(words[i])
            
    return answer