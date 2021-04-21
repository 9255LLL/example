#!/c/Users/CSJY/AppData/Local/Programs/Python/Python37/python.exe
Data_List = []
Raw_Data_List = []

Power_Vol = 0

Abs_Min = 500
Abs_Min_Vol = None

f = open("data.csv",'r')

for Line in f:
	Item_List = Line[:-1].split(",")
	Raw_Data_List.append ((float(Item_List[0])*1000,float(Item_List[1])*10000, float(Item_List[2])*1000, float(Item_List[3])*1000, float(Item_List[4])*1000))
	
for Power in range(201):
	Abs_Min = 500
	for i in Raw_Data_List:
		if abs(Power-i[1]) < Abs_Min:
			Abs_Min = abs(Power-i[1])
			Abs_Min_Item = i
	Data_List.append (Abs_Min_Item)

Power = 0
Data_String = ""

for i in Data_List:
	#print(Power,i)
	Data_String += "{0},\t{1},\t{2},\t{3},\t{4},\n".format(Power,int(i[0]),int(i[2]),int(i[3]),int(i[4]))
	Power += 1
	
ff = open("power_vol_map.csv", 'w')
ff.write(Data_String)
ff.close()

input()
f.close()