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
