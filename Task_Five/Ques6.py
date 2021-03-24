fh=open("doc.txt",'w')
fh.write("Hello I am A file \n")
fh.write("Where you need to return the data string \n")
fh.write("Which is of even length \n")
fh.write("Make sure you return the content in the same link as it is present.")
fh.close()
fr=open("doc.txt",'r')
lines=fr.read()
for word in lines.split():
    if len(word)%2==0:
        print(word)
fr.close()