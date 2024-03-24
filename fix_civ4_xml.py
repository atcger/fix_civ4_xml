"""
Copy to folder containing the bad XMLs and execute.

It works by adding a ' ' before any NON-ASCII char previous to a '<'.
"""

import os

def fix_file(path):
    new_lines = []
    with open(path, "r") as f:
        lines = f.readlines()
        for l in lines:
            new_l = ""
            prev_c = 0
            for c in l:
                if c == '<' and prev_c > 128:
                    new_l += ' '
                new_l += c
                prev_c = ord(c)
            if new_l != l:
                print("Modified line", new_l)
            new_lines.append(new_l)
    with open(path, "w") as f:
        f.writelines(new_lines)

def list_files(dir):
    files = os.listdir(dir)

    print("files in current path: ", dir)
    for f in files:
        print(f)
        fix_file(os.path.join(dir, f))

def fix_civ4_xml():
    path = os.path.abspath(__file__)
    dir = os.path.dirname(path)
    print("fix folder: ", dir)
    list_files(dir)
    input("SUCCESS! Press any key to exit")
    return

if __name__ == "__main__":
    fix_civ4_xml()
