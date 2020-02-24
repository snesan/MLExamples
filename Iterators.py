# Program to Demonstrate iterators and iterables
# Programmer : vidyasagar
# Batch -
# Updated Date :

### Iterators and Iterables

list(map(lambda *a: a, range(3)))
list(map(lambda *a: a, (1, 2, 3, 4), 'abc'))
p = map(lambda *a: a, (1, 2, 3, 4), 'abc')
dir(map)

students = [
dict(id=0, credits=dict(math=9, physics=6, history=7)),
dict(id=1, credits=dict(math=6, physics=7, latin=10)),
dict(id=2, credits=dict(history=8, physics=9, chemistry=10)),
dict(id=3, credits=dict(math=5, physics=5, geography=7)),
]

students = [
dict(id=0, credits=dict(math=9, physics=6, history=7)),
dict(id=1, credits=dict(math=6, physics=7, latin=10)),
dict(id=2, credits=dict(history=8, physics=9, chemistry=10)),
dict(id=3, credits=dict(math=5, physics=5, geography=7)),
]

students[2].["math"]

def decorate(student):
# create a 2-tuple (sum of credits, student) from student dict
    return (sum(student['credits'].values()), student)
def undecorate(decorated_student):
# discard sum of credits, return original student dict
    return decorated_student[1]

decorate(students)

students1 = sorted(map(decorate, students), reverse=True)
students1 = list(map(undecorate, students))


