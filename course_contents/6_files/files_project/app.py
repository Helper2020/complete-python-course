# file pointer
my_file = open('data.txt', 'r')
# reads entire content as single string
file_content = my_file.read()

my_file.close()

print(file_content)

user_name = input('Enter your name: ')
# 'w' erases the content of the file
# We want to open the file for the smallest amount of time
my_file_writing = open('data.txt', 'w')
my_file_writing.write(user_name)

my_file_writing.close()
