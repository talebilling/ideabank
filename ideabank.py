import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = "open_and_write.txt"

def action_by_argv():
    if len(sys.argv) == 1:
        idea_line = promt_input()
        export_idea_line_to_file(filename, idea_line)
        read_lines = read_from_file(filename)
        print_output(read_lines)
    else:
        print("Invalid command")

def promt_input():
    return input("What is your new idea: ")

def export_idea_line_to_file(filename, idea_line):
    export_file = open(dir_path + "/" + filename, "a+")
    export_file.writelines(idea_line + "\n")
    export_file.close()

def read_from_file(filename):
    read_file = open(dir_path + "/" + filename, "a+")
    read_file.seek(0, 0)
    read_lines = read_file.readlines()
    read_file.close()
    return read_lines
    
def print_output(read_line):
    print("\nYour ideabank:")
    for i in range(len(read_line)): 
        print(str(i + 1) + ". " + read_line[i], end="")

action_by_argv()