def solution(message, spoiler_ranges):
    answer = 0
    words=message.split()
    words_len=[]
    
    start=0
    if message[0]==" ":
        start=1
    for i in range(len(words)):
        tmp=[]
        tmp.append(start)
        start+=len(words[i])-1
        tmp.append(start)
        words_len.append(tmp)
        start+=2
    
    not_hide_word=[]
    hide_word=[]
    
    for i in range(len(words)):
        for j in range(len(spoiler_ranges)):
            flag=True
            if words_len[i][0]<=spoiler_ranges[j][0]<=words_len[i][1] or words_len[i][0]<=spoiler_ranges[j][1]<=words_len[i][1] or spoiler_ranges[j][0]<=words_len[i][0]<=spoiler_ranges[j][1] or spoiler_ranges[j][0]<=words_len[i][1]<=spoiler_ranges[j][1]:
                flag=False
                hide_word.append(words[i])
                break
        if flag:
            not_hide_word.append(words[i])
    print(not_hide_word)
    print(hide_word)
            
    for i in range(len(hide_word)):
        if hide_word[i] not in not_hide_word:
            answer+=1
            not_hide_word.append(hide_word[i])
        
    return answer