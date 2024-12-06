
with open('grades.txt', 'w') as file:
    while True:
     
        grade = input("Enter a grade (or type 'done' to finish): ")
              
        if grade.lower() == 'done':
            break
       
        try:
            grade = float(grade) 
            file.write(f"{grade}\n") 
        except ValueError:
            print("Invalid input! Please enter a valid number for the grade.")
        
print("Grades have been saved to grades.txt.")
