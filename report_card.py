print("Student Progress Report Card")
print("================================================")
stud_name = input("Enter your name: ")                #name is in str format
stud_roll_no = int(input("Enter your roll number: ")) #roll no in int format
#all marks are in integer format
eng_marks = int(input("Enter your English Marks: "))  
maths_marks = int(input("Enter your Maths Marks: "))
science_marks = int(input("Enter your Science Marks: "))
history_marks = int(input("Enter your History Marks: "))
geography_marks = int(input("Enter your Geography Marks: "))
social_marks = int(input("Enter your Social Science Marks: "))
#to calculate total marks we need to add all marks
total_marks = (eng_marks + maths_marks + science_marks + history_marks + geography_marks + social_marks)
#percentage is obtained by using mathematical formula
stud_percentage = round((total_marks/600) * 100,2)
print("**********************************************")
print(f'English       : {eng_marks}') #f is used for formatting a string
print(f'Maths         : {maths_marks}')
print(f'Science       : {science_marks}')
print(f'History       : {history_marks}')
print(f'Geography     : {geography_marks}')
print(f'Social Science: {social_marks}')
print(f'Total         : {total_marks}')
print(f'Percentage    : {stud_percentage}%')

##f is used for formatting a string, it is a way to format your string that is more readable and fast.
#The f or F in front of strings tell Python to look at the values inside {} and 
#substitute them with the variables values if exists.
print("**********************************************")

if stud_percentage < 40:
    print('You are Promoted')
elif stud_percentage >= 40 and stud_percentage < 49:
    print('Grade D')
elif stud_percentage >= 50 and stud_percentage < 59:
    print('Grade C')
elif stud_percentage >= 60 and stud_percentage < 79:
    print('Grade B')
elif stud_percentage >= 80 and stud_percentage < 100:
    print('Grade A')
else:
    print('You Fail')
print('===============================================')