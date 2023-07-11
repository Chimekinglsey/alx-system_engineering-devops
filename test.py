def my_string():
	First, Second_name = input("Enter Name:").split()
	print("{} {}".format(First, Second_name))
	my_list=[]
	my_list.append((First, Second_name))
	print(my_list)
my_string()
