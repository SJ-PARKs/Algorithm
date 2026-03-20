n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]

# Please write your code here.
students.sort(key=lambda x:x[1], reverse=True)
students.sort(key=lambda x:x[0])

for i in range(len(students)):
    print(str(students[i][0])+" "+str(students[i][1])+" "+str(students[i][2]))

