def helper(cur, days_until):
	print("Day", helper(cur + 1, days_until))
def ft_count_harvest_recursive():
	days_until = int(input("Days until harvest: "))
	helper(1, days_until)
	print("Harvest time!")
