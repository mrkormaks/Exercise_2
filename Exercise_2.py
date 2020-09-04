def odometer(N):
	distance = 0
	list_1 = []
	list_2 = []
	list_3 = []
	for i in range(len(N)):
		if i % 2 == 0:
			list_1.append(N[i])
		if i % 2 != 0:
			list_2.append(N[i])
	for i in range(len(list_2)):
		if i == 0:
			list_3.append(list_2[i])
		else:
			list_3.append(list_2[i] - list_2[i-1])
	for i in range(len(list_1)):
		distance += list_1[i] * list_3[i]
	return(distance)
