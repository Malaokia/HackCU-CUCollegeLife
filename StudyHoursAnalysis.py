import numpy as np 
import matplotlib.pyplot as pyplot


def basic_linear_regression(x, y):
    # Basic computations to save a little time.
    #slope(b) (NΣXY - (ΣX)(ΣY)) / (NΣX2 - (ΣX)2)
	slope = (len(x)*sum([a*b for a,b in zip(x,y)]) - sum(x)*sum(y)) / (len(x)*sum([i**2 for i in x]) - (sum(x))**2)
	#Intercept(a) = (ΣY - b(ΣX)) / N 
	intercept = (sum(y) - slope*(sum(x)))/ len(x)
	return (slope,intercept)
def main():
	x = []
	y = []
	with open("StudyHoursDB.csv","r") as f:
		reader = csv.reader(f,delimiter = " ")
		for row in reader:
			minutes = row[0]*60 + row[1]
			y.append(row[2])
			x.append(minutes)
	(slope,intp) = basic_linear_regression(x,y)
	fit = np.polyfit(x,y,1)
	fit_fn = np.poly1d(fit)
	plt.plot(x,y,'yo',x,fit_fn(x),'--k')
	plt.xlim(0,1000)
	plt.ylim(0,100)
	show()