import sys
# Строка, на основании которой берётся индекс всех элементов "1".
search_line = '010101010'
# Входной массив, из которого будут выбраны все позиции элементов на основании индексов элементов "1" из строки search_line.
in_array = ['test','service2','dev','service4','test5','test6','test7','service8','prod'] 
# Выходной массив.
out_array = []

def items_line(search_line = search_line):
	"""
		Проверка строки на наличие только символов '0' или '1'.
		Параметр search_line - строка, состоящая только из 9 элементов,
		которая проходит валидацию на наличие только '0' или '1'.
		Наличие в строке других элементов, отличных '0' или '1',
		приведёт к выходу программы с выводом неверных элементов.
		Пример search_line:
				для положительной валидации:
										'010101010'
				для отрицательной валидации:
										'010901003'
										'01090100A'								
	"""
	buffers = ''
	for i in search_line:
		if (i != "0" and i != '1'): 
			buffers = buffers + f',{i}'
	buffers = buffers[1:]
	if len(buffers) == 1:
		sys.exit(f"Вы ввели недопустимый элемент {buffers} в строку.")
	elif len(buffers) > 1:
		sys.exit(f"Вы ввели недопустимые элементы {buffers} в строку.")

def length_line(search_line = search_line):
	"""
		Проверка длины строки. 
		Параметр search_line - строка, которая должна состоять из 9 элементов. 
		Если длина строки не равна 9 элементам, то это приведёт к выходу из программы
		с выводом сообщения о неверном количестве элементов в строке.
		Пример search_line:
				для прохождения положительной валидации по длине строки:
										'010101010'
										'010901003'
										'01090100A'
				для отрицательной валидации по длине строки:
										'010101'
										'010109'
										'01A'	
																		
	"""
	if len(search_line) != 9:
		print("Вы ввели неверное количество элементов в строку.")
		items_line(search_line = search_line)
		sys.exit()
	else:
		items_line(search_line = search_line)
		return(search_line)

def valid_array(in_array = in_array):
	"""
		Генерация входного массива и его валидация по кол-ву элементов.
		На вход функции подаётся строка, которая должна состоять из 9-ти элементов, укзанных через ",".
		Пример:
			На входе 'sasasa,sasa,sasa,2222222222sss,sas,asas,asas,sasa'
			При успешной валидации функция вернёт:
					 ['sasasa','sasa','sasa','2222222222sss','sas','asas','asas','sasa']
		Отрицательный  результат (если кол-во элементов не равно 9) приведёт к выходу из программы. 
	"""
	# Генерация входного массива
	in_array = in_array.split(',')
	# Валидация входного массива
	if len(in_array) != 9:
		print("Вы ввели неверное количество элементов в строку.")
		sys.exit()
	else:
		return(in_array)

def mode_line(search_line = search_line):
	"""
		Параметр search_line  в ручном режиме нужно заполнить самостоятельно.
		Параметр search_line  в авто режиме принимает значение:
					'010101010',
		из-за ранее определённой константой search_line. 			
	"""
	print("\nСтрока в авто режиме заполнится значением '010101010'.")
	print("Требование - строка, состоящая из 0 и/или 1, должна состоять из 9 символов.")
	print("Для ручного режима введите 'Y/y'. Для авто режима -'N/n': ")

	# Взаимодействие с пользователем. 
	# Ожидает 'Y/y' - для ручного режима. 
	# Ожидает 'N/n'  - для авто режима. 
	while 1:
		mode = input()
		if not mode:
			print("Выберете режим заполнения строки ( 'Y/y' - ручной  или 'N/n - авто' ).")
			continue
		elif 'Y' == mode or 'y' == mode: 
			print("\nЗаполните строку: ")	
			search_line = input()
			search_line = length_line(search_line = search_line)
			return(search_line)
		elif 'N' == mode or 'n' == mode:
			print("Строка приняла значение по умолчанию '010101010'.")
			return(search_line)
		else:
			print("Для ручного режима введите 'Y/y'. Для авто режима - 'N/n'. Требуется повторный ввод: ")

def mode_array(in_array = in_array):
	"""
		Параметр in_array в ручном режиме нужно заполнить самостоятельно.
		Пример ввода элементов для получения входного массива:
		'test,service2,dev,service4,test5,test6,test7,service8,prod'
		Параметр in_array будет в авто режиме принимать значение:
		['test','service2','dev','service4','test5','test6','test7','service8','prod'].
		Из-за ранее определённой константой in_array. 			
	"""
	print("\nВходной массив в авто режиме заполнится значениями:"\
		+ "test,service2,dev,service4,test5,test6,test7,service8,prod.")
	print("Требование - массив должен состоять из 9-и элементов, указанных через ','.")
	print("Для ручного режима введите 'Y/y'. Для авто режима - 'N/n': ")

	# Взаимодействие с пользователем. 
	# Ожидает 'Y/y'  - для ручного режима. 
	# Ожидает 'N/n' - для авто режима. 
	while 1:
		mode = input()
		if not mode:
			print("Выберите режим заполнения входного массива ( 'Y/y' или 'N/n' ).")
			continue
		elif 'Y' == mode or 'y' == mode: 
			print("\nЗаполните входной массив: ")	
			in_array = input()
			in_array = valid_array(in_array = in_array)
			return(in_array)
		elif 'N' == mode or 'n' == mode:
			print("Массив принял значение по умолчанию:\ntest,service2,dev,service4,test5,test6,test7,service8,prod")
			return(in_array)
		else:
			print("Для ручного режима введите 'Y/y'. Для авто режима - 'N/n'. Требуется повторный ввод: ")

def finall_array(search_line = search_line, in_array = in_array):
	"""
		На основании прошедших валидацию  параметров search_line и in_array 
		генерируется выходной массив out_array.
		От каждого элемента "1" строки search_line будет взят его индекс.
		Далее - на основании взятых индексов - 
		будет прозводиться выборка из входного массива,
	"""	
	for index, item in enumerate(search_line):
		if item != '0':
			out_array.append(in_array[index])
	return(out_array)

def main (search_line = search_line, in_array = in_array,out_array = out_array):
	"""
		Основная функция.
		
		Параметр search_line (строка) определён как константа.
		Далее может быть изменен.

		Параметр in_array (входной массив) определен как константа.
		Далее может быть изменен.

		Параметр out_array (выходной массив)
	"""
	try:
		print("Программа написана на Python 3.7.3, Debian 10.1 'buster'.")
		print("Выход из программы Ctrl+'C'")
		
		search_line = mode_line(search_line = search_line)
		in_array = mode_array(in_array = in_array)
		out_array = finall_array(search_line = search_line, in_array = in_array)

		print("\nРезультат выполения программы: ")
		print("Строка: ",search_line)
		print("Входной массив: ", in_array)
		print('Выходной массив:', out_array)	

	except KeyboardInterrupt:
		print("\nВы вышли из программы.")
	return(0)	
			
main(search_line = search_line ,in_array = in_array, out_array = out_array)

