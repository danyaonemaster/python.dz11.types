tuples = (2, 8, 10, 25, 1, 2, 771, 125, 256, 100, 8, 10, 81, 96, 8, 1, 144, 5)
lists = []
list_str = ["One", "Two", "Three"]

print(f"""max number : {max(tuples)}
min number : {min(tuples)}
sum tuple : {sum(tuples)}
arithmetic mean : {round(sum(tuples) / len(tuples), 2)}""")

for index, number in zip(range(1, 4), list_str):
    lists.append([i for i in tuples if len(str(i)) == index])

    print(f"{number} number - {len(lists[index - 1])} elements")

