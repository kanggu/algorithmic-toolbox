# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

max_index1 = 0
max_index2 = 1

if n >= 3:
	for i in range(2,n):
		if a[i] > a[max_index1]:
			if a[max_index1] > a[max_index2]:
				max_index2 = max_index1
			max_index1 = i
		elif a[i] > a[max_index2]:
			max_index2 = i




print(a[max_index1] * a[max_index2])
