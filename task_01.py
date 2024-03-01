tuples = (
    2, 0, 3, 4, 0, "G", "A", "F", "L", "Q", "a", "a", "h", "o", "p", "w", "w", "x", "x", 5, 6, 10, 11, 7, 7, 8, 0, 15,
    2, 3, 4, "r", "r", "r", "e", "e", "a")
user_input = input(f"{tuples} \n enter any tuple value : ")

print(f"""\nint len list: {len([i for i in tuples if isinstance(i, int)])}
str len list: {len([i for i in tuples if isinstance(i, str)])}
upper len list: {len([i for i in tuples if isinstance(i, str) and i.isupper()])}
lower len list: {len([i for i in tuples if isinstance(i, str) and i.islower()])}
all {user_input} in a tuple : {len([i for i in tuples if str(i) == user_input])}""")
