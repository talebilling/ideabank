import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = "open_and_write.txt"
comm_line_arg_lenght = len(sys.argv)
comm_line_arg = sys.argv

def action_by_argv():
    if comm_line_arg_lenght == 1:
        input_read_export_line_to_file()
    elif comm_line_arg_lenght == 2 and comm_line_arg[1] == "--list":
        print_saved_lines_to_output() 
    elif comm_line_arg_lenght == 3 and comm_line_arg[1] == "--delete": 
        index_input_read_delete_export()
    else:
        print("Invalid command")

def input_read_export_line_to_file():
    idea_line = promt_input()
    read_lines = read_from_file(filename)
    read_lines.append(idea_line + "\n")
    export_idea_lines_to_file(filename, read_lines)
    print_output(read_lines)

def print_saved_lines_to_output():
    read_lines = read_from_file(filename)
    print_output(read_lines)

def index_input_read_delete_export():  
    if comm_line_arg[2].isdigit():
        index = int(comm_line_arg[2]) - 1
        mod_lines = read_from_file(filename)
        delete_idea(mod_lines, index)
        export_idea_lines_to_file(filename, mod_lines)
        print_output(mod_lines)
    else:
        print("Invalid digit in command line")

def promt_input():
    return input("What is your new idea: ")

def read_from_file(filename):
    read_file = open(dir_path + "/" + filename, "a+")
    read_file.seek(0, 0)
    read_lines = read_file.readlines()
    read_file.close()
    return read_lines

def export_idea_lines_to_file(filename, lines):
    export_file = open(dir_path + "/" + filename, "w+")
    export_file.writelines(lines)
    export_file.close()
    
def print_output(read_lines):
    print("\nYour ideabank:")
    for i in range(len(read_lines)): 
        print(str(i + 1) + ". " + read_lines[i], end="")

def delete_idea(read_lines, index):
    if index < len(read_lines):
        del read_lines[index] #alt solution: read_lines.pop(index)

action_by_argv()