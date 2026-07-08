def ft_count_harvest_iterative():
	days_until = int(input("Days until harvest: "))
	days = range(days_until)
	for cur in days:
		print("Day", cur + 1)
	print("Harvest time!")