#write the python program to copy the contents source.txt file into destination.txt
source_file = "sourcee.txt"
destination_file = "destination.txt"
try :
    file=open("source.txt","r")
    data=file.read()
    file.close()

    file=open("destination.txt","w")
    file.write(data)
    file.close()
except  FileNotFoundError:
    print("source.txt file not found")  



else:
    print("data transfered successfully")

finally:    
    print("program execution completed")