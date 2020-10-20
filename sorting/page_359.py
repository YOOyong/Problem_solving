
n = int(input())
students = []
for _ in range(n):
    students.append(input().split())

#람다 순서대로 조건을 주며 정렬한다. 내림차는 -를 붙이면 된다.
students.sort( key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])