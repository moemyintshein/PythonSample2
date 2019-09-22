import student
import mary

x = student.a["student"]
y = student.b["student"]
z = student.a["age"]
w = student.b["age"]
print(x, z)
print(y, w)

for i in range(len(student.f)):
	print(i, student.f[i])


for i in range(len(mary.a)):
	print(i, mary.a[i])