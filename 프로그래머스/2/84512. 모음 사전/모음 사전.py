import copy

vowel=["A","E","I","O","U"]
dictionary=[]
def DFS(n,word):
    global vowel,dictionary
    if n==5:
        return 
    for i in range(len(vowel)):
        temp_word=copy.deepcopy(word)
        temp_word[n]=vowel[i]
        dictionary.append("".join(temp_word))
        DFS(n+1,temp_word)
def solution(word):
    global dictionary
    answer = 0
    DFS(0,["","","","",""])
    temp_dict=[]
    for i in range(len(dictionary)):
        temp_dict.append("".join(dictionary[i]))
    answer=temp_dict.index(word)
    return answer+1