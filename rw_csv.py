#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test.py
#  
#  Copyright 2016 user <user@cu-cs-vm>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import csv

def readInfo():
	infodict = {}
	with open("infodb.csv","r") as f:
		reader = csv.reader(f, delimiter=" ")
		for row in reader:
			infodict.update({row[0]:row[1]})
		f.close()
	return infodict
def writeInfo(dic):
	fo = open("infodb.csv","rw+")
	fo.seek(0,0)
	for index in range(1,7):
		fo.write("%s %s"%(str(index),dic[str(index)]) )
		fo.write("\n")
	fo.close()
	return 0
def readScore():
	infodict = {}
	with open("scoredb.csv","r") as f:
		reader = csv.reader(f, delimiter=" ")
		for row in reader:
			infodict.update({row[0]:row[1]})
		f.close()
	return infodict
def writeScore(list):
	fo = open("scoredb.csv","rw+")
	fo.seek(0,0)
	for index in range(0,5):
		fo.write("%s"%list[index])
		fo.write("\n")
	fo.close()
	return 0
def readGoal():
	infodict = {}
	with open("goaldb.csv","r") as f:
		reader = csv.reader(f, delimiter="-")
		for row in reader:
			infodict.update({row[0]: row[1]})
		f.close()
	print infodict
	return infodict
def writeGoal(list):
	lst_arr = list.split(" ")
	with open("goaldb.csv", 'r') as f:
		file_lines = [''.join([x.strip("\n"), " %s\n"%lst_arr[1]]) if x.find(lst_arr[0]) == 0 else x for x in f.readlines()]
	with open("goaldb.csv", 'w') as f:
		f.writelines(file_lines) 
	return 0
def readStudyHrs():
	infodict = []
	with open("studyhoursdb.csv","r") as f:
		for line in csv.reader(f):
			if ''.join(line).strip():
				row = line[0].split(" ")
				infodict.append((row[0],row[1]))
	return infodict
def writeStudyHrs(dic):
	fo = open("studyhoursdb.csv","rw+")
	fo.next()
	fo.write("\n%s %s"%(dic.keys()[0],dic.values()[0]))
	fo.close()
	return 0



