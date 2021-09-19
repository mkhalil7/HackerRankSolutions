if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    
    #getting some grades
    total_grade = 0
    for grade in student_marks[query_name]:
        total_grade = total_grade+ grade
    
        
    #calcualte average  
    average = total_grade/len(student_marks[query_name])
    
    #print formatting
    print("%.2f" % average)