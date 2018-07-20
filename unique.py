import argparse
import string 


# print unique char/word/line from text
def counter(text):
    for x in text:
        if text.count(x) < 2:
            print(x)

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required=True, help="Name of input file with extension.")
ap.add_argument("-c", "--char", action="store_true", help="Search unique characters.")
ap.add_argument("-w", "--word", action="store_true", help="Search unique words.")                
ap.add_argument("-l", "--line", action="store_true", help="Search unique lines.")
ap.add_argument("-s", "--small", action="store_true", help="Convert text to lowercase.")

args = vars(ap.parse_args())

if args["char"] is False and args["word"] is False and args["line"] is False:
    print("at least one of -c, -w, -l required.")


lines = "" # list for read data from file
translaton = str.maketrans('', '', string.punctuation)


# load the input file and copy data to data (string) and then to lines (list)
with open(args["file"]) as f:
    for data in f:
        if args["small"]:
            data = data.lower()  
        data = data.translate(translaton) # remove all punctuation
        lines += data

# lines2 is list from lines(string)
lines2 = lines.split('\n')
lines2 = [x.strip(' ') for x in lines2]

words = lines.split()

char = []
for ch in words:
    char += ch

# find unique word
if args["word"]:
    print("Unique word(s):")
    counter(words)
    
# find unique line    
if args["line"]:
    print("Unique line(s):")
    counter(lines2)

# find unique char
if args["char"]:
    print("Unique character(s):")
    counter(char)
    

