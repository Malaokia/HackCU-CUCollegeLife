import numpy as np 
import matplotlib.pyplot as plt
import csv
import rw_csv

#at one side we give them last result
#give calculation and store it
def quizASSESS(mx):
    if mx == "A":
        return 'HUMANITIES'
    elif mx == "B":
        return 'SOCIAL SCIENCES'
    elif mx == "C":
        return'SCIENCES' 
    else:
        return'QUANTITATIVE REASONING'
def infoOLD():
    info_old = rw_csv.readinfo()
    trait_old = quizASSESS(max(info_old.values()))
    return trait_old
def infoNEW(txt):
    expln = {}
    with open("traitdb.csv","r") as f:
        reader = csv.reader(f, delimiter="-")
        for row in reader:
            expln.update({row[0]:row[1]})
        f.close()
    info_new,txt_arr = {},txt.split(",")
    for i in txt_arr:
        info_new.update({i[0]:i[-1]})
    trait_new = quizASSESS(max(info_new.values()))
    rw_csv.writeinfo(info_new)
    return trait_new,expln[trait_new]
'''
def scoreRW():
    j = rwcsv.readscore()
    k = rwcsv.writescore(["family N","travel N","Social Y","Study N","Picture profileA.jpg"])
def goalRW():
    l = rwcsv.readgoal()
    m = rwcsv.writegoal(['bigbrother sister mother father','paris singapore brussel vietnam',
        'homework project club volunteer','james jamie jessie jackie'])
    return las_r


#if one isn't complete give estimation
#else store in the database
def regression():
    x = []
    y = []
    with open("StudyHoursDB.csv","r") as f:
        reader = csv.reader(f,delimiter = " ")
        for row in reader:
            print row
            y.append(int(row[2]))
            x.append(int(row[0])*60 + int(row[1]))
    fit = np.polyfit(x,y,1)
    fit_fn = np.poly1d(fit)
    plt.plot(x,y,'yo',x,fit_fn(x),'--k'),plt.xlim(0,1000),plt.ylim(0,100)
    plt.ylabel('scores received'),plt.xlabel('minutes spent studying')
    plt.title('Regression of Hours Studying and Scores Received')
    plt.show()
'''
if __name__ == "__main__":
    main()
