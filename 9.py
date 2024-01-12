#Write all content of a given file into a new file 
with open("source.txt","r")as fp:
   lines=fp.readlines()
lines

   
with open("destination.txt","w") as fp:
   count=0;
   for i in lines:
     if count ==4:
       count+=1
       continue
     else:
        fp.write(i)
         
