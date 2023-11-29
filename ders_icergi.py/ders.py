"""
def main():
    outfile= open("philisophers.txt","w")
    outfile.write("john locke\n")
    outfile.write("david hume\n")
    outfile.write("edmund burke\n")
    outfile.close()
main()
"""
"""
def main():
    infile= open("philisophers.txt","r")
    line1=infile.readline()
    line2=infile.readline()
    line3=infile.readline()
    infile.close()
    print(line1)
    print(line2)
    print(line3)
main()
"""
def main():
    num_days= int(input("for how many days do:"+"you have sales?"))
    sales_file= open("sales.txt","w")
