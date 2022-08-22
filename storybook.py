from tabulate import tabulate

#story Data

data = [["Naruto Shippuden", "TV Show", 2007],
        ["Attack on Titan", "TV Show", 2013],
        ["House of Cards", "TV Show", 2013]]

#define the header names

head_names = ["Story", "Type", "Date"]

#display table

print(tabulate(data, headers=head_names, tablefmt="fancy_grid"))

