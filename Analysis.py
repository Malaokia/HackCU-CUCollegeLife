import numpy as np 
import matplotlib.pyplot as plt
import csv
import rw_csv
mpl.use("Agg")

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
    info_old = rw_csv.readInfo()
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
    rw_csv.writeInfo(info_new)
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

'''
#if one isn't complete give estimation
#else store in the database
def ptsAssess():
    ctr = 0
    with open("StudyHoursDB.csv","r") as f:
        reader = csv.reader(f,delimiter = " ")
        for row in reader:
            ctr += 1
            pass
        f.close()
    return ctr
def regression(x,y):
    rnd_down = int(len(x) * 0.8)
    fit = np.polyfit(x[:rnd_down],y[:rnd_down],1)
    fit_fn = np.poly1d(fit)
    plt.plot(x,y,'yo',x,fit_fn(x),'--k'),plt.xlim(0,1000),plt.ylim(0,100)
    plt.ylabel('scores received'),plt.xlabel('minutes spent studying')
    plt.title('Regression of Hours Studying and Scores Received')
    plt.savefig('Regression_Graph',bbox_inches='tight',dpi=100)


    #hr score
def hrsCalc(txt):
    txt_arr = txt.split(" ")
    if len(txt_arr) < 2 and ptsAssess() > 4:
        if int(txt_arr[0]) <= 100:
            data_dict = rw_csv.readStudyHrs()
            regression(data_dict.values(),data_dict.keys())
        else:
            return "Please enter the Score within 100"
    elif len(txt_arr) < 2 and ptsAssess() <= 4:
        return "Not Enough Data Points for Regression Prediction. Please Enter More Points"
    else:
        rw_csv.writeStudyHrs({txt_arr[0]: txt_arr[1]})
        data_dict = rw_csv.readStudyHrs()
        regression(data_dict.values(),data_dict.keys())
    return 0
