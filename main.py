import rwcsv

def main():
	myob = rwcsv.readinfo()
	i = rwcsv.writeinfo(["1 B","2 A","3 C","4 D","5 A","6 A"])
	j = rwcsv.readscore()
	k = rwcsv.writescore(["family N","travel N","Social Y","Study N","Picture profileA.jpg"])
	l = rwcsv.readgoal()
	m = rwcsv.writegoal(['bigbrother sister mother father','paris singapore brussel vietnam',
		'homework project club volunteer','james jamie jessie jackie'])
	print i,k,l
	#m = rwcsv.writegoal([])
	return 0

if __name__ == '__main__':
	main()

