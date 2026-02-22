# grade Calculating program
#  Grading Logic: 
#   - A: 90-100, B:80-89, C:70-79,D:60-69,F:0-59

## Function to get message and calculate grade
def calculate_grade(marks):
    if 90<=marks<=100:
        return "A", "Excellent, you have done a great job.🎉"
    elif 80<=marks<=89:
        return "B", "Very Good, Keep it up! 👍"
    elif 70<=marks<=79:
        return "C", "Nice Work, But you can aim heigher 🙂"
    elif 60<=marks<=69:
        return "D", "You passed, keep working hard. 📚"
    else:
        return "F","Don't give up! Try Again and improve🔁"
    

# Fuction to get valid marks
def get_valid_marks():
    while True:
        try:
            marks = int(input("Enter marks (0-100): "))

            if 0<=marks<=100:
                return marks
            else:
                print("❌, Invalid Marks range, Marks should be between 0 and 100.")
        
        except ValueError:
            print("❌,Invalid Input, Only numeric values are allowed")


## Main Program
def main():
    name = input("Enter student name : ").strip()
    marks = get_valid_marks()

    grade,message = calculate_grade(marks)

    print("\n 📊 Result For",name.upper()+ ":")
    print("Marks:",marks,"/100")
    print("Grade:",grade)
    print("Message:",message)

# Run Program
main()