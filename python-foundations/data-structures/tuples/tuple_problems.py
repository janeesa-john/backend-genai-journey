# Find largest element in tuple

numbers = (4, 8, 2, 10, 1)

large = numbers[0]

for num in numbers:

    if num > large:

        large = num

print("Largest Element:", large)

print("------------------")


# Find smallest element in tuple

numbers = (4, 8, 2, 10, 1)

small = numbers[0]

for num in numbers:

    if num < small:

        small = num

print("Smallest Element:", small)

print("------------------")


# Sum of tuple elements

numbers = (4, 8, 2, 10, 1)

total = 0

for num in numbers:

    total += num

print("Sum of Tuple Elements:", total)

print("------------------")


# Search element in tuple using loop

numbers = (1, 2, 3, 4, 5)

search = 3

for num in numbers:

    if num == search:

        print("Element Found")
        break

else:

    print("Element Not Found")

print("------------------")


# Search element in tuple using 'in'

numbers = (1, 2, 3, 4, 5)

search = 3

if search in numbers:

    print("Element Found")

else:

    print("Element Not Found")

print("------------------")


# Count occurrences in tuple

numbers = (1, 2, 2, 3, 2, 4)

search = 2

count_num = 0

for num in numbers:

    if num == search:

        count_num += 1

print(f"{search} appears {count_num} times")

print("------------------")


# Find common elements between tuples

tuple1 = (1, 2, 3, 4, 5)

tuple2 = (4, 5, 6, 7, 8)

common = []

for num in tuple1:

    if num in tuple2:

        common.append(num)

print("Common Elements:", common)

print("------------------")


# Convert tuple to list and list to tuple

numbers = (1, 2, 3, 4)

list_new = list(numbers)

print("Tuple to List:", list_new)

tuple_new = tuple(list_new)

print("List to Tuple:", tuple_new)

print("------------------")


# Reverse a tuple

numbers = (1, 2, 3, 4, 5)

print("Reversed Tuple:", numbers[::-1])


# Find largest element in tuple

numbers = (4, 8, 2, 10, 1)

large = numbers[0]

for num in numbers:

    if num > large:

        large = num

print("Largest Element:", large)

print("------------------")


# Find smallest element in tuple

numbers = (4, 8, 2, 10, 1)

small = numbers[0]

for num in numbers:

    if num < small:

        small = num

print("Smallest Element:", small)

print("------------------")


# Sum of tuple elements

numbers = (4, 8, 2, 10, 1)

total = 0

for num in numbers:

    total += num

print("Sum of Tuple Elements:", total)

print("------------------")


# Search element in tuple using loop

numbers = (1, 2, 3, 4, 5)

search = 3

for num in numbers:

    if num == search:

        print("Element Found")
        break

else:

    print("Element Not Found")

print("------------------")


# Search element in tuple using 'in'

numbers = (1, 2, 3, 4, 5)

search = 3

if search in numbers:

    print("Element Found")

else:

    print("Element Not Found")

print("------------------")


# Count occurrences in tuple

numbers = (1, 2, 2, 3, 2, 4)

search = 2

count_num = 0

for num in numbers:

    if num == search:

        count_num += 1

print(f"{search} appears {count_num} times")

print("------------------")


# Find common elements between tuples

tuple1 = (1, 2, 3, 4, 5)

tuple2 = (4, 5, 6, 7, 8)

common = []

for num in tuple1:

    if num in tuple2:

        common.append(num)

print("Common Elements:", common)

print("------------------")


# Convert tuple to list and list to tuple

numbers = (1, 2, 3, 4)

list_new = list(numbers)

print("Tuple to List:", list_new)

tuple_new = tuple(list_new)

print("List to Tuple:", tuple_new)

print("------------------")


# Reverse a tuple

numbers = (1, 2, 3, 4, 5)

print("Reversed Tuple:", numbers[::-1])

print("------------------")


# Find second largest element in tuple

numbers = (2, 4, 5, 1, 9)

large = numbers[0]

sec_large = numbers[0]

for num in numbers:

    if num > large:

        sec_large = large
        large = num

    elif num > sec_large and num != large:

        sec_large = num

print("Largest:", large)
print("Second Largest:", sec_large)

print("------------------")


# Remove duplicates from tuple

numbers = (1, 2, 2, 3, 4, 4, 5)

unique = []

for num in numbers:

    if num not in unique:

        unique.append(num)

new = tuple(unique)

print("Tuple Without Duplicates:", new)

print("------------------")


# Find frequency of elements in tuple

numbers = (1, 2, 2, 3, 2, 4)

frequency = {}

for num in numbers:

    if num in frequency:

        frequency[num] += 1

    else:

        frequency[num] = 1

print("Frequency:", frequency)

print("------------------")


# Find even and odd numbers from tuple

numbers = (1, 2, 3, 4, 5, 6)

num_even = []

num_odd = []

for num in numbers:

    if num % 2 == 0:

        num_even.append(num)

    else:

        num_odd.append(num)

print("Even Numbers:", num_even)
print("Odd Numbers:", num_odd)

print("------------------")


# Find maximum and minimum element in one loop

numbers = (4, 8, 2, 10, 1)

large = numbers[0]

small = numbers[0]

for num in numbers:

    if num > large:

        large = num

    if num < small:

        small = num

print("Maximum:", large)
print("Minimum:", small)

print("------------------")


# Sort tuple without using sort()

numbers = (4, 2, 8, 1)

numbers_list = list(numbers)

for i in range(len(numbers_list)):

    for j in range(i + 1, len(numbers_list)):

        if numbers_list[i] > numbers_list[j]:

            numbers_list[i], numbers_list[j] = numbers_list[j], numbers_list[i]

sorted_tuple = tuple(numbers_list)

print(sorted_tuple)

print("------------------")


# Find missing number in tuple

numbers = (1, 2, 3, 5)

for num in range(1, 6):

    if num not in numbers:

        print("Missing Number:", num)

print("------------------")


# Rotate tuple elements

numbers = (1, 2, 3, 4, 5)

rotated = numbers[1:] + numbers[:1]

print("Rotated Tuple:", rotated)

print("------------------")


# Find pair with given sum in tuple

numbers = (1, 2, 3, 4, 5)

target = 7

for i in range(len(numbers)):

    for j in range(i + 1, len(numbers)):

        if numbers[i] + numbers[j] == target:

            print(f"Pair Found: {numbers[i]} {numbers[j]}")

print("------------------")


# Find pairs with equal sum

numbers = (1, 2, 3, 4, 5)

new = {}

for i in range(len(numbers)):

    for j in range(i + 1, len(numbers)):

        total = numbers[i] + numbers[j]

        if total not in new:

            new[total] = [(numbers[i], numbers[j])]

        else:

            new[total].append((numbers[i], numbers[j]))

print("Pairs Grouped By Sum:", new)

print("------------------")


# Check palindrome tuple

numbers = (1, 2, 3, 2, 1)

reverse = numbers[::-1]

if numbers == reverse:

    print("Palindrome Tuple")

else:

    print("Not Palindrome")

print("------------------")


# Check whether two tuples are identical

tuple1 = (1, 2, 3)

tuple2 = (1, 2, 3)

if len(tuple1) == len(tuple2):

    for i in range(len(tuple1)):

        if tuple1[i] != tuple2[i]:

            print("Not identical")
            break

    else:

        print("Identical")

else:

    print("Not identical")

print("------------------")


# Count vowels in tuple of strings

words = ("apple", "banana", "orange")

vowels = 'AEIOUaeiou'

count_vowel = 0

for word in words:

    for ch in word:

        if ch in vowels:

            count_vowel += 1

print("Total Vowels:", count_vowel)

print("------------------")


# Find longest word in tuple

words = ("apple", "banana", "orange", "kiwi")

long = words[0]

for word in words:

    if len(word) > len(long):

        long = word

print("Longest Word:", long)

print("------------------")


# Find shortest word in tuple

words = ("apple", "banana", "orange", "kiwi")

short = words[0]

for word in words:

    if len(word) < len(short):

        short = word

print("Shortest Word:", short)

print("------------------")


# Count words starting with vowel

words = ("apple", "banana", "orange", "umbrella", "grape")

vowels = 'aeiou'

vowel_word = 0

for word in words:

    if word[0].lower() in vowels:

        vowel_word += 1

print("Words Starting With Vowel:", vowel_word)

print("------------------")


# Count ending letters of words

words = ("apple", "table", "grape", "kite")

dict_end = {}

for word in words:

    if word[-1] not in dict_end:

        dict_end[word[-1]] = 1

    else:

        dict_end[word[-1]] += 1

print(dict_end)

print("------------------")


# Find most repeated ending letter

words = ("apple", "table", "grape", "kite", "banana")

dict_end = {}

count_last = 0

top_letter = ""

for word in words:

    if word[-1] in dict_end:

        dict_end[word[-1]] += 1

    else:

        dict_end[word[-1]] = 1

for key, value in dict_end.items():

    if value > count_last:

        count_last = value
        top_letter = key

print("Most Repeated Ending Letter:", top_letter)

print("------------------")


# Group words by length

words = ("apple", "dog", "banana", "cat", "orange")

group = {}

for word in words:

    if len(word) not in group:

        group[len(word)] = []

        group[len(word)].append(word)

    else:

        group[len(word)].append(word)

print(group)

print("------------------")


# Create dictionary from tuple of words

words = ("apple", "banana", "cat")

group = {}

for word in words:

    group[word] = len(word)

print(group)

print("------------------")


# Find word with maximum vowels

words = ("apple", "banana", "education", "cat")

max_vowel_count = 0

max_vowel = ''

for word in words:

    max_count = 0

    for ch in word:

        if ch.lower() in 'aeiou':

            max_count += 1

    if max_count > max_vowel_count:

        max_vowel_count = max_count
        max_vowel = word

print("Word With Maximum Vowels:", max_vowel)

print("------------------")


# Find word with minimum vowels

words = ("apple", "banana", "education", "cat")

min_vowel_count = float('inf')

min_vowel = ''

for word in words:

    count = 0

    for ch in word:

        if ch.lower() in 'aeiou':

            count += 1

    if count < min_vowel_count:

        min_vowel_count = count
        min_vowel = word

print("Word With Minimum Vowels:", min_vowel)

print("------------------")


# Find first repeating character in tuple of words

words = ("apple", "banana", "cat")

for word in words:

    freq = {}

    for ch in word:

        if ch in freq:

            freq[ch] += 1

        else:

            freq[ch] = 1

    for ch in word:

        if freq[ch] > 1:

            print(word, "->", ch)

            break

    else:

        print(word, "-> No repeating character")