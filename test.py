c = [2,1,1,3,1,3,4,1,1,3,4,1,1,1,3,4]
hit=0
for index,element in enumerate(c):
	if element == 1:
		try:
			if c[index+1]==3 and c[index+2]==4:
				hit = hit+1
		except IndexError:
			break
print "Sequence Found", hit ,"times"