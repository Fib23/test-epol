import sys
search_line = '010101010' #  Строка на основание, которой берётся индекс всех элементов "1".
in_array = ['test','service2','dev','service4','test5','test6','test7','service8','prod'] # Входной массив, из которого будут выбраны все позиции элементов на основании индексов элементов "1" из строки search_line.
out_array = [] # Выходной массив.

def sub_fillter(search_line = search_line):
	# Проверка строки на наличие только символов '0' или '1'.
	buffers = ''
	for i in search_line:
		if i == "0"	or i == "1":
			pass
			#print(f"Элемент {i} равен '0' или '1'")
		else:
			buffers = buffers + f',{i}'
	buffers = buffers[1:]
	if len(buffers) == 1:	
		#print(f"Вы ввели недопустимый элемент {buffers} в строку")	
		sys.exit(f"Вы ввели недопустимый элемент {buffers} в строку.")
	elif len(buffers) > 1:
		#print(f"Вы ввели недопустимые элементы {buffers} в строку")
		sys.exit(f"Вы ввели недопустимые элементы {buffers} в строку.")

def fillter(search_line = search_line):
	# Строгая проверка на длину строки. Требование - строка должна быть из 9 символов.
	if len(search_line) != 9:
		print("Вы ввели неверное количество элементов в строку.")
		sub_fillter(search_line = search_line)
		sys.exit()
	else:
		sub_fillter(search_line = search_line)
		return(search_line)

def fillter_array (in_array = in_array):
	in_array = in_array.split(',')
	if len(in_array) != 9:
		print("Вы ввели неверное количество элементов в строку.")
		sys.exit()
	else:
		return(in_array)	

def main (search_line = search_line, in_array = in_array,out_array = out_array):
	try:
		print("Выход из программы Ctrl+'C'")
		#Выбор между авто и ручным заполнением переменной search_line (строка)
		print("\nСтрока по умолчанию заполнится значением '010101010'.")
		print("Если хотите, её можно заполнить самому. Требование - строка, состоящая из 0 и/или 1,  должна состоять из 9 символов.")
		print("Для ручного режима введите 'Y/y'. Для автоматического режима -'N/n': ")

		while 1>0:
			mode = input()
			if not mode:
				print("Не указан параметр для выбора режима работы со строкой ( 'Y/y' или 'N/n' ). Требуется повторный ввод параметра.")
				continue
				#sys.exit("Не указан параметр для выбора режима работы со строкой")
			elif 'Y' == mode or 'y' == mode: 
				print("\nЗаполните строку: ")	
				search_line = input()
				search_line = fillter(search_line = search_line)
				break
			elif 'N' == mode or 'n' == mode:
				search_line = '010101010'
				print("Строка приняла значение по умолчанию '010101010'.")
				break
			else:
				print("Указан неверный параметр. Требуется повторный ввод: ")
				#sys.exit("Указан неверный параметр. Завершение работы.")
			# print(search_line)	

		#Выбор между авто и ручным заполнением переменной in_array (входного массива)
		print("\nВходной массив  по умолчанию заполнится значениями: test,service2,dev,service4,test5,test6,test7,service8,prod.")
		print("Если хотите, его можно заполнить самому. Требование - массив должен состоять из 9-и элементов, указанных через ','.")
		print("Для ручного режима введите 'Y/y'. Для автоматического режима  - 'N/n': ")
		
		while 1>0:
			mode = input()
			if not mode:
				print("Не указан параметр для выбора режима работы с входным массивом ( 'Y/y' или 'N/n' ). Требуется повторный ввод параметра.")
				continue
				#sys.exit("Не указан параметр для выбора режима работы c входным массивом")
			elif 'Y' == mode or 'y' == mode: 
				print("\nЗаполните входной массив: ")	
				in_array = input()
				in_array = fillter_array (in_array = in_array)
				break
			elif 'N' == mode or 'n' == mode:
				in_array = ['test','service2','dev','service4','test5','test6','test7','service8','prod']
				print("Массив принял значение по умолчанию: test,service2,dev,service4,test5,test6,test7,service8,prod")
				break
			else:
				print("Указан неверный параметр. Требуется повторный ввод: ")
				#sys.exit("Указан неверный параметр. Завершение работы.")
			#print(in_array)	

		#search_line = fillter(search_line = search_line)
		print("\nРезультат выполения программы: ")
		print("Строка: ",search_line)
		print("Входной массив: ", in_array)
		for index, item in enumerate(search_line):
			if item != '0':
				#print(f"Индекс {index} элемента '{item}' соответсвует элементу входного массива {in_array[index]}")
				out_array.append(in_array[index])
		print('Выходной массив', out_array)		
	except KeyboardInterrupt:
		print("\nВы вышли из программы.")
			
main(search_line = search_line ,in_array = in_array, out_array = out_array)
