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

def readinfo():
	infodict = {}
	with open("infodb.csv","r") as f:
		reader = csv.reader(f, delimiter=" ")
		for row in reader:
			infodict.update({row[0]:row[1]})
		f.close()
	return infodict
def writeinfo(list):
	fo = open("infodb.csv","rw+")
	fo.seek(0,0)
	for index in range(0,6):
		fo.write("%s"%list[index])
		fo.write("\n")
	fo.close()
	return 0
def readscore():
	infodict = {}
	with open("scoredb.csv","r") as f:
		reader = csv.reader(f, delimiter=" ")
		for row in reader:
			infodict.update({row[0]:row[1]})
		f.close()
	return infodict
def writescore(list):
	fo = open("scoredb.csv","rw+")
	fo.seek(0,0)
	for index in range(0,5):
		fo.write("%s"%list[index])
		fo.write("\n")
	fo.close()
	return 0
def readgoal():
	infodict = {}
	with open("goaldb.csv","r") as f:
		reader = csv.reader(f, delimiter=" ")
		title = ["family","travel","study","social"]
		ctr = 0
		for row in reader:
			infodict.update({title[ctr]: row})
			ctr += 1
		f.close()
	return infodict
def writegoal(list):
	fo = open("goaldb.csv","rw+")
	fo.seek(0,0)
	for index in range(0,4):
		fo.write("%s"%list[index])
		fo.write("\n")
	fo.close()
	return 0


