if __name__ == '__main__':
    StudentList = []
    ScoreList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        #get nested list of students and scores
        StudentList.append([name,score])
        #get score lsit
        ScoreList.append(score)
    
    #Clean the duplicate grades, sort and get scond lowest
    SecondLowestScore  = sorted( list(dict.fromkeys(ScoreList)))[1]
    
    #Sort the student list based on grades first then names 
    StudentList = sorted(StudentList, key=lambda x: (- x[1], x[0]))
    
    
    #Print students with equal grade as the second lowest
    for std in StudentList:
        if(std[1]==SecondLowestScore):
            print(std[0])
        
    