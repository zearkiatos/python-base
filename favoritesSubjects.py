
def subjectsCount(subjectName1:str, subjectName2:str, subjectName3:str)->int:
    countSubject = 0
    if (subjectName1.lower().find('programacion')!=-1 or subjectName1.lower().find('matematica')!=-1 or subjectName1.lower().find('filosofia')!=-1 or subjectName1.lower().find('literatura')!=-1):
        countSubject+=1
    if (subjectName2.lower().find('programacion')!=-1 or subjectName2.lower().find('matematica')!=-1 or subjectName2.lower().find('filosofia')!=-1 or subjectName2.lower().find('literatura')!=-1):
        countSubject+=1
    if (subjectName3.lower().find('programacion')!=-1 or subjectName3.lower().find('matematica')!=-1 or subjectName3.lower().find('filosofia')!=-1 or subjectName3.lower().find('literatura')!=-1):
        countSubject+=1

    return countSubject
    