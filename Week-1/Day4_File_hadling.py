#File i/o
#Text files - .txt, .docx, .log etc
#Binary files - .mp4, .mpv, .png, .jpeg etc

#Open, read & close file
#f = open("file_name", "mode") - mode: r-read mode, w-write mode
#data=f.read()
#f.close()

f=open("demo.txt", "r")
data = f.read()
print(data)
f.close()

#Reading a file
#data = f.read() reads entire file
#data = f.readline() reads data line at a time

#Writing a file 
#f = open("demo.txt", "w")
f.write("this is a new line") # overwrites the entire file

#f = open("demo.txt", "a")
f.write("this is a new line") #adds to the file


