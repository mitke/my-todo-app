FILEPATH = "todos.txt"

def get_todos(fpath=FILEPATH):
    """
    Read a text file and return the list of to-do items.
    Text fajl pretvara u niz.
    """
    with open(fpath, 'r', encoding='utf-8') as f:
        todos_local = f.readlines()
    return todos_local

def write_todos(todos_local, fpath=FILEPATH):
    """
    Write the to-do items list in the text file.
    Čita to-do listu i upisuje u fajl.
    """
    with open(fpath, 'w', encoding='utf-8') as f:
        f.writelines(todos_local)

if __name__ == "__main__":
    print(get_todos())
    print('Hello from functions!')
