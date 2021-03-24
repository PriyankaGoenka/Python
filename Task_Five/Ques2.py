from sys import argv
filename, progname = argv

print("Name of file is: ", filename)
print("Enter the name of program: ", progname)
#try:
    #while True:
        #print("Enter the name of the file to be opened",file_name
'''fh=open("da.txt",'w')
fh.write("My name is Priyanka")
fh.close()'''
try:
    while True:
        fh=open(filename)
        content=fh.read()
        print(content)
        fh.close()
        break

except:
    print("Enter the correct name:")
    

