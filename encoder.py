input_string =input("Enter a string to be changed to its Base64 equivalent:	")

combined_string=''

#Changes each character to corresponding ASCII character then to binary string
for i in input_string:
	bin_string=bin(ord(i))
	#(bin_string)
	
#create binary string to 8 bit and concatenate to make binary string
	combined_string+=(8-(len(bin_string)-2))*'0'+str(bin_string)[2:]
#print(len(combined_string))


#add 0 padding to create 6 bit binary string
if len(combined_string)%6!=0:
	combined_string+=(6-(len(combined_string)%6))*'0'

if len(input_string)%3==0:
	padding=0
elif len(input_string)%3==1:
	padding=2
else:
	padding=1


#print(padding)
padding=int(padding)*'='


result=''
for i in range(0,len(combined_string),6):
	separated_string=2*'0'+combined_string[i:i+6]
	x=int(separated_string,2)
	
	if x>=0 and x<=25:
		result+=chr(x+65)
	if x>=26 and x<=51:
		result+=chr(x+97-26)
	if x>=52 and x<=61:
		result+=chr(x-4)
	if x==62:
		result+='+'
	if x==63:
		result+='/'
	
if len(padding)>0:
	result+=str(padding)
print(result)

	
	


	
