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
