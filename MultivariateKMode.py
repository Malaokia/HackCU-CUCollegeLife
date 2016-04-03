import numpy as np
from kmodes import kmodes
import csv

alpha_dic = {'A':[1,0,0,0],'B':[0,1,0,0],'C':[0,0,1,0],'D':[0,0,0,1]}
ansdata = []
emldata = []
with open('MultiPInfodb.csv','r') as f:
	reader = csv.reader(f, delimiter=':')
	for row in reader:
		tem = []
		emldata.append(row[0])
		for x in row[1].split(' '):
			tem +=alpha_dic[x]
		ansdata.append(tem)
f.close()

km = kmodes.KModes(n_clusters=4,init="Huang",n_init=5,verbose=1)
clusters = km.fit_predict(ansdata)

grp = {0:[],1:[],2:[],3:[]}
ctr = 0
for index in clusters:
	grp[index].append(emldata[ctr])

	ctr += 1
file_lines = []
print grp
for x in grp.values():
	if x is None:
		file_lines.append("")
	else:
		txt = ""
		for i in x:
			txt += ",%s"%i
		file_lines.append(txt)
file_lines = [i.replace(',','',1) for i in file_lines]
print file_lines
with open('htmlinfodb.csv','w') as f:
	for i in file_lines:
		f.writelines(i+'\n')
f.close()


		
