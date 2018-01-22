import numpy as np
array = np.zeros((50,40))
res=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
i=0
j=0
p=0
np.set_printoptions(threshold='nan')
with open('data.txt') as f:
	lines = f.readlines()
	for line in lines:
		print(line)
		i=0
		for num in line.split(", "):
			if num!="\n":
				print("|"+num+"|"+" TO : "+str(j)+","+str(i))
				if num:
					array[j,i]=float(num)
					i=i+1
			if i>0:
				p=i
		j=j+1

#print(array)
#print(j)
for l in range(j):
	#print(array[l])
	for k in range(p):
		if l!=0:
			res[k] = (res[k] + array[l,k]) / 2 
		else:
			res[k] = array[l,k]

file = open("avg.txt","w")
file.write(str(0.0)+", ")
for elem in res:
	if elem != 0:
		file.write(str(elem)+", ")
