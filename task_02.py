tuples = (2, 8, 10, 25, 1, 2, 771, 125, 256, 100, 8, 10, 81, 96, 8, 1, 144, 5)
len_one_digit = len([i for i in tuples if len(str(i)) == 1])
len_two_digit = len([i for i in tuples if len(str(i)) == 2])
len_three_digit = len([i for i in tuples if len(str(i)) == 3])

print(f"""max number : {max(tuples)}
min number : {min(tuples)}
sum tuple : {sum(tuples)}
arithmetic mean : {round(sum(tuples) / len(tuples), 2)}
One number - {len_one_digit} element
Two numbers - {len_two_digit} element
Three numbers - {len_three_digit} elements""")
