# https://www.codechef.com/problems/EZSPEAK?tab=statement

tc = int(input())
while tc != 0:
	N = int(input())
	a = input()
	consonant = 0
	l = []
	for i in range(0, len(a)):
		if (a[i] != "a" and a[i] != "e" and a[i] != "i" and a[i] != "o" and a[i] != "u"):
			consonant = consonant + 1
			l.append(consonant)
		else:
			consonant = 0
			l.append(consonant)
	if 4 in l:
		print("NO")
	else:
		print("YES")
	tc = tc - 1