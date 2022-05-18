# Reese wrote this on Dav's suggestion!!!

with open("../git.txt", encoding="utf-8") as file:			#Open git.txt to read only
    data_lines = file.readlines()
    
    line_i = 0
    listtable = [] 							#Will contain all characters, each as its own sublist
    while line_i < len(data_lines):
        listtable.append([])
        listtable[line_i//10].append(ord(data_lines[line_i][0])) 	#First entry in the sublist is the character's Unicode value as a number
        for y in range(9):
            listtable[line_i//10].append(data_lines[line_i+y]) 		#Then add the character and its bitmap data lines as subsequent entries.
        line_i+=10 							#Go to next character


listtable.sort(key=lambda x: x[0]) 					#Sort list by Unicode values
    
    
with open("../git.txt", "w", encoding="utf-8") as file:			#And re-open to write only
    for i in listtable:
    	for y in range(9):
    	    print(i[y+1],end='',file=file)				#Add the textlines one by one
    	if listtable.index(i) != len(listtable)-1:
    	    print('\n',end='',file=file)				#And if it isn't the last character in the list, add a newline as well
