input = open("BP.nastruct.dat","r")
output = open("nastruct_frame.dat","w")

line = input.readlines()
count = 0
for line in input:
	output.write(line)
	count+=13
	print(line)

#desired_lines = line[2:6489:13]

#output.write (desired_lines)
input.close()
output.close()
