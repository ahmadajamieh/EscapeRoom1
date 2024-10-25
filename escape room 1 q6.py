import numpy as np

#Room 6: Classification - Student Performance Prediction

def classify_student(homework_score, exam_score):
    
    if homework_score >= 85 and exam_score >= 85:
        return "High Achiever"
    elif homework_score >= 60 and exam_score >= 60:
        return "Pass"
    else:
        return "Fail"


print(classify_student(90, 92))  
print(classify_student(65, 70))  
print(classify_student(55, 58))  
