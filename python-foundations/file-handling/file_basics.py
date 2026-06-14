# Count number of lines in file

f = open("sample_files/sample.txt", 'r')

count_line = 0

for line in f:

    count_line += 1

print("Number of lines:", count_line)

f.close()

print("------------------")


# Count number of words in file

f = open("sample_files/sample.txt", 'r')

s = f.read()

count_word = 0

for word in s.split():

    count_word += 1

print("Number of words:", count_word)

f.close()

print("------------------")


# Count number of characters in file

f = open("sample_files/sample.txt", 'r')

content = f.read()

count_ch = 0

for ch in content:

    count_ch += 1

print("Number of characters:", count_ch)

f.close()

print("------------------")


# Count number of vowels in file

f = open("sample_files/sample.txt", 'r')

content = f.read()

count_vowel = 0

for ch in content:

    if ch.lower() in 'aeiou':

        count_vowel += 1

print("Number of vowels:", count_vowel)

f.close()

print("------------------")


# Count uppercase and lowercase letters in file

f = open("sample_files/sample.txt", 'r')

content = f.read()

upper = 0
lower = 0

for ch in content:

    if ch.islower():

        lower += 1

    elif ch.isupper():

        upper += 1

print("Uppercase Letters:", upper)
print("Lowercase Letters:", lower)

f.close()

print("------------------")


# Count digits and spaces in file

f = open("sample_files/sample.txt", 'r')

count_space = 0
count_digits = 0

content = f.read()

for ch in content:

    if ch.isdigit():

        count_digits += 1

    elif ch.isspace():

        count_space += 1

print("Digits:", count_digits)
print("Spaces:", count_space)

f.close()

print("------------------")


# Count vowels and consonants in file

f = open("sample_files/sample.txt", 'r')

content = f.read()

vowels = 0
consonants = 0

for ch in content:

    if ch.lower() in 'aeiou':

        vowels += 1

    elif ch.isalpha() and ch.lower() not in 'aeiou':

        consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)

f.close()

print("------------------")


# Count special characters in file

f = open("sample_files/text.txt", 'r')

content = f.read()

special_ch = 0

for ch in content:

    if not ch.isalpha() and not ch.isspace() and not ch.isdigit():

        special_ch += 1

print("Special Characters:", special_ch)

f.close()

print("------------------")


# Count frequency of characters in file

freq = {}

f = open("sample_files/sample.txt", 'r')

content = f.read()

for ch in content:

    if ch in freq:

        freq[ch] += 1

    else:

        freq[ch] = 1

print(freq)

f.close()

print("------------------")


# Count frequency of words in file

f = open("sample_files/data.txt", 'r')

words = f.read().split()

freq = {}

for word in words:

    if word in freq:

        freq[word] += 1

    else:

        freq[word] = 1

print(freq)

f.close()

print("------------------")


# Find most frequent word in file

f = open("sample_files/data.txt", 'r')

words = f.read().split()

freq = {}

max_count = 0
most_word = ''

for word in words:

    if word in freq:

        freq[word] += 1

    else:

        freq[word] = 1

for word, count in freq.items():

    if count > max_count:

        max_count = count
        most_word = word

print("Most Frequent Word:", most_word)
print("Frequency:", max_count)

f.close()

print("------------------")


# Find least frequent word in file

f = open("sample_files/data.txt", 'r')

words = f.read().split()

freq = {}

min_count = float('inf')
least_word = ''

for word in words:

    if word in freq:

        freq[word] += 1

    else:

        freq[word] = 1

for word, count in freq.items():

    if count < min_count:

        min_count = count
        least_word = word

print("Least Frequent Word:", least_word)
print("Frequency:", min_count)

f.close()

print("------------------")


# Find all repeated words in file

f = open("sample_files/sample.txt", 'r')

freq = {}
repeated = set()

words = f.read().split()

for word in words:

    if word in freq:

        freq[word] += 1

    else:

        freq[word] = 1

for word, count in freq.items():

    if count > 1:

        repeated.add(word)

print(repeated)

f.close()

print("------------------")


# Find all unique words in file

f = open("sample_files/sample.txt", 'r')

freq = {}
unique = set()

words = f.read().split()

for word in words:

    if word in freq:

        freq[word] += 1

    else:

        freq[word] = 1

for word, count in freq.items():

    if count == 1:

        unique.add(word)

print(unique)

f.close()

print("------------------")


# Find longest word in file

f = open("sample_files/sample.txt", 'r')

words = f.read().split()

longest = ''

for word in words:

    if len(word) > len(longest):

        longest = word

print(longest)

f.close()

print("------------------")


# Find shortest word in file

f = open("sample_files/sample.txt", 'r')

words = f.read().split()

shortest = words[0]

for word in words:

    if len(word) < len(shortest):

        shortest = word

print(shortest)

f.close()