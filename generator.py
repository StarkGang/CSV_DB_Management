import os
import ast


ascii_art = """
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@((((((((((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@%((((((@@@(@@@(((((#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@#((#((@@((@@@(@@@@@@@(((((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@(&@@((@@((@@@(@@@((@@@@(((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@((@@((@@#(@@@(@@@((((@%(((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@#(@@@(@@@(@@@((@@@@(((((((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@((@@(@@@(@@@((((@@@@#(((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@(@@@@@@#@@@(((((((@@%((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@(%@(%@@@@@(@@@(((@@%(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@((((@@@@@(@@@(@@@(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(((&@@@(@@@@@((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(((@@(@@(((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@((((((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""


def custom_input(txt: str):
    txt_to_return = None
    no_of_tries = 0
    while not txt_to_return:
        if no_of_tries != 0:
            print("\033[31m", "No INPUT Received. Try Again.", "\033[0m")
        txt_to_return = input("\033[36m" + txt + "\033[0m")
        no_of_tries += 1
    return txt_to_return.strip()


def check_folder():
    if not os.path.exists("scripts"):
        os.mkdir("scripts")
    if not os.path.exists("template"):
        os.mkdir("template")
    if not os.path.exists("sessions"):
        os.mkdir("sessions")

def take_custom_input():
    script_name = custom_input("Enter script name: ")
    db_name = custom_input("Enter database name: ")
    colm = custom_input("Enter columns names (separated by a comma) [EX: name, class, roll no]: ")
    colm = ast.literal_eval(colm) if colm.startswith("[") else colm.split(",")
    enter_name = custom_input("Enter names of project members (separated by a comma) [EX: warner, stark, midhun]: ")
    return script_name, db_name, colm, enter_name

def create_script():
    script_name, db_name, colm, name = take_custom_input()
    with open("template/dummy.txt", "r") as f:
        data = f.read()
        data = data.replace("<<<person_name>>>", name)
        data = data.replace("<<<db_name>>>", db_name)
        data = data.replace("<<<db_col>>>", str(colm))
        data = data.replace("<<<script_name>>>", script_name)
    with open(f"scripts/{script_name}_csv_db.py", "w") as f:
        f.write(data)
    print(f"Script created successfully in scripts/{script_name}")

if __name__ == "__main__":
    print("\033[32m", ascii_art, "\033[0m")
    check_folder()
    create_script()
