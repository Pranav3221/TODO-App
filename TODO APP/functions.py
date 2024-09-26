FILEPATH='todos.txt'

#Functions
def show(): 
    print('\n')
    
    todos=get_todos()
    for index, item in enumerate(todos):
        item=item.strip('\n')
        print(index+1, item)
    


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r')as file_local:
        todos_local=file_local.readlines()
    return todos_local 

def writes_todos( todos_arg, filepath=FILEPATH):
     with open(filepath, 'w') as file:
          file.writelines(todos_arg)