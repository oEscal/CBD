file = open("female-names.txt", "r")
data = file.readlines()
file.close()

data_dict = {}
for name in data:
   letter = name[0]
   if letter not in data_dict:
      data_dict[letter] = 0
   data_dict[letter] += 1

file_save = open("initials4redis.txt", "w")
for letter in data_dict:
   file_save.write(f"set {letter.upper()} {data_dict[letter]}\n")
file_save.close()

print("Done")
