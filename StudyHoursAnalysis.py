import numpy as np 
import matplotlib.pyplot as plt
import csv

def main():
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
if __name__ == "__main__":
    main()