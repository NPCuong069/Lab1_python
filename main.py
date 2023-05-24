# Name: Nguyen Phuoc Cuong
# Class: GCS1003A

# Exercise 1:


from datetime import date
# Enter student information
name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
entrance_year_check = input("Enter your entrane year: ")
# While loop to check for input
while entrance_year_check.isdigit()==False:
    entrance_year_check = input("Entrance year must be a number: ")
entrance_year= int(entrance_year_check)
current_year= date.today().year
# Show information
def get_information():
    study_year =current_year- entrance_year
    print("My name is "+name+", I am",age,"years old, \nI am",study_year,"year student a Greenwich")
get_information()

# Exercise 2:
# Input text
text = input("Enter a text: ")
order = int(input("Enter an order: "))
words_to_replace = input("Enter a word: ")
# Convert text to list
text_list = text.split()
#Replace text
text_list[order-1]= words_to_replace
# Create new text
new_text = ""
for item in text_list:
    new_text+=" "+item
# Convert new text to list 
new_text_list = new_text.split()
# Show result
print("Length of original text is: ",len(text_list))
print("Modified text: ", new_text)
print("Length of modified text is: ",len(new_text_list))