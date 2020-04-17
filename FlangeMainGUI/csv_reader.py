import os
import csv

#cwd = os.getcwd()

HOME = os.environ.get("HOMEDRIVE")
USER = os.environ.get("USERNAME")

def mapper(flangeClass, NPS):
	if (flangeClass == 2500):
		if (NPS > 12):
			raise Exception('Size {} does not exist for class #{} flanges.'.format(str(NPS), str(flangeClass)))
	if (flangeClass == 900) or (flangeClass == 1500) or (flangeClass == 2500):
		if (NPS == 3.5) or (NPS == 22):
			raise Exception('Size {} does not exist for class #{} flanges.'.format(str(NPS), str(flangeClass)))
	filename = HOME+"\\Users\\"+USER+"\\abaqus_plugins\\FlangeMainGUI\\Flanges_B16.5_" + str(flangeClass) + '.csv'
	with open(filename, 'rb') as file:
		lines = csv.reader(file, delimiter=',')
		for line in lines:
			if(line[0] == str(NPS)):
				ans = line[2:12]
	file.close()
	flangeDimensions = map(float, ans)
	flangeDimensions[4] = int(flangeDimensions[4])
	
	bolt=[]
	boltFile = HOME+"\\Users\\"+USER+"\\abaqus_plugins\\FlangeMainGUI\\Bolts_B16.5.csv"
	with open(boltFile, 'rb') as filename:
		lines = csv.reader(filename, delimiter=',')
		for line in lines:
			if (line[0] == str(flangeDimensions[5])):
				print('a')
				bolt.append(line[4])
				bolt.append(line[10])
				bolt.append(line[12])
	filename.close()

	boltDimensions = map(float, bolt)

	keys = ["flangeDimensions","boltDimensions"]
	vals = [flangeDimensions, boltDimensions]

	d = dict(zip(keys,vals))

	return d