import numpy as np 
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import csv
import rw_csv
import numpy as np
from sklearn import linear_model
import pandas as pd

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

def __correlationCalculation(x,y):
		correl = np.corrcoef(x,y)[0][1]
		if (correl == 0):
			return "Two variable sets are uncorrelated.\n"
		elif (correl > 0):
			return "There is a positive correlation.\n"
		else:
			return "There is a negative correlation.\n"  
 
def __graphData(data,slope,x,y,intercept,training):
		data.plot(kind='scatter',x="Score",y="Hours of Studying")
		x_eval = x[training:]
		y_eval = y[training:]
		b = plt.scatter(x_eval,y_eval,c='yellow')
		x_list = []
		y_list = []
		for k in x:
			x_list.append(k)
			y_value = slope * k + intercept
			y_list.append(y_value)
		line, = plt.plot(x_list,y_list,c='red',linewidth=2)
		plt.savefig("LinearRegressionGraph",bbox_inches='tight',dpi=100)

def regression(x_data,y_data,predict_value):
    text_output = "LINEAR REGRESSION ANALYSIS\n"
    text_output = text_output + __correlationCalculation(x_data,y_data)
    if text_output != "Two variable sets are uncorrelated.\n":
			training = int(len(x_data)*80/100)
			regr = linear_model.LinearRegression()
			dic = {"Score":x_data[:training-1],"Hours of Studying":y_data[:training-1]}
			data = pd.DataFrame(dic)
			data.index += 1
			X = data[["Score"]]
			y = data["Hours of Studying"]
			text_output = text_output + "x value is scores\n"
			text_output = text_output + "y value is hours of studying\n"
			regr.fit(X,y)
			slope = regr.coef_[0]
			intercept = regr.intercept_
			text_output = text_output + "Coefficient computes from linear regression model:\n" + str(slope) + "\n"
			text_output = text_output + "Interception computes from linear regression model:\n" + str(intercept) + "\n"
			text_output = text_output + "Linear approximation line has form: y = " + str(slope) + " x + " + str(intercept) + "\n"
			dic_eval = {"Score":x_data[training:],"Hours of Studying":y_data[training:]}
			data_eval = pd.DataFrame(dic_eval)
			data_eval.index += 1
			X_eval = data_eval[["Score"]]
			y_eval = data_eval["Hours of Studying"]
			mean_sqr_err = np.mean((regr.predict(X_eval)-y_eval)**2)
			score = regr.score(X_eval,y_eval)
			text_output = text_output + "Mean square error is " + str(mean_sqr_err) + "\n"
			text_output = text_output + "Score of this prediction " + str(score) + "\n"
			text_output = text_output + "(Note: if score number equals 1, there is a perfect prediction and a strong linear relationship between two variables)\n"
			__graphData(data,slope,x_data,y_data,intercept,training)
			if (predict_value <= 100):
				predict_result = slope*predict_value + intercept
			else:
				predict_result = "Invalid output for score (Need to be some number from 0 to 100)."
    return (text_output,predict_result)


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
        print data_dict
        regression(data_dict.values(),data_dict.keys())
    return 0

