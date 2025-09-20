# You are given a list of the first ten prime numbers:
# - prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# Perform the following operations using list slicing and indexing techniques:
# a) Extract the middle five primes: Create a new list containing the five primes in the middle of the original list.
# b) Get every second prime: Create a new list containing every second number from the original list, starting from the beginning.
# c) Use negative indexing: Create a new list containing the last three primes of the list. d) Reverse the list: Create a new list that contains all the elements of the original list in
# reverse order.
# e) Descending Order: Sort the list in descending order and store it in a new list.

prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


five_mid = prime_numbers[2:7]
print(f"Five middle numbers: ", five_mid)
second_ones = prime_numbers[::2]
print(f"Every second number: ", second_ones)
last_three = prime_numbers[-3:]
print(f"Last three numbers: ", last_three)
rev_list = prime_numbers[::-1]
print(f"Reversed List: ", rev_list)
desc_list = sorted(prime_numbers, reverse=True)
print(f"List in Descending order: ", desc_list)