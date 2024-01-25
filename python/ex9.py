# write all contents of a given file into new file by skipping line 5

with open("first.txt","r")as fp:
   lines=fp.readlines()

   
with open("second.txt","w") as fp:
   count=0;
   for i in lines:
     if count ==4:
       count+=1
       continue
     else:
        fp.write(i)
     count+=1
