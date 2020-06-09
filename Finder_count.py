def finder_c(dict):
	c_dict={}
	for i in dict:
		if i in c_dict:
			c_dict[i]+=1    #увеличить значение элемента словаря с ключом i
		else:
			c_dict[i]=1     #присвоить значение 1 элементу словаря с ключом i
	print("В слове ", dict, " встречаются буквы: ")
	print(c_dict)
finder_c("параллелограмм")
