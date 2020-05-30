def squares(*args):
    for x in args:
        yield x ** 2
#
# print("Test")
# numbers = [1, 2, 3, 4, 5]
# squares(numbers)
# print()

from collections import Counter

def get_number_with_highest_count(counts):
    return max(counts, key=lambda number: counts[number])

def most_frequent(numbers):
    counts = Counter(numbers)
    print(counts)
    return get_number_with_highest_count(counts)

numbers = [1, 1, 2, 2, 2, 3]
print(most_frequent(numbers))