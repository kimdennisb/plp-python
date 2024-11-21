with open("example.txt", "r") as file:
    data = file.read()
    print(data)
with open("output.txt", "w") as file: 
    file.write(f"{data} with concatenation of this text!")
    
# Ask user for a filename
filename = input("Provide name of the file: ")
try:
    with open(filename, "r") as file:
        data = file.read()
except FileNotFoundError:
    print("File not found. Please check the filename.")