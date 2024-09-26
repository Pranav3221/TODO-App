#from functions import show,get_todos,writes_todos
import functions as func
import time
now=time.strftime("%b %d,%Y,%H:%M:%S")
print(now)
#main
while True:
    user_action=(input('\nType add, show, edit, complete or exit: '))
    user_action=user_action.strip()

    if user_action.startswith('add'):
            todo=user_action[4:]
            todo+='\n'

            todos=func.get_todos()

            todos.append(todo)

            func.writes_todos(todos)    

    elif user_action.startswith('show'):
            print('\n')
    
            todos=func.get_todos()
            for index, item in enumerate(todos):
                item=item.strip('\n')
                print(index+1, item)   

    elif user_action.startswith('edit'):
            try:
                number=int(user_action[5:])
                print(number, 'Got it\n')
                number-=1

                todos=func.get_todos()

                new_todo=input("Enter a new todo: ")
                todos[number]=new_todo + '\n'

                func.writes_todos(todos)
                
                print("Todo updated !!!!" )
                func.show()
            except ValueError:
                print('Command is not Valid.')
                continue

    elif user_action.startswith('complete'):
            try:    
                number=int(user_action[9:])
                print(number, 'Got it\n')
                index=number-1

                todos=func.get_todos()

                todo_removed=todos[index].strip('\n')
                todos.pop(index)

                func.writes_todos(todos)
                message=f'Todo Removed is: {todo_removed}'
                print(message)
                print('\nNew Todo list below:')
                func.show()
            except ValueError:
                print('Command is not Valid.')
                continue 
            except IndexError:
                print('Command is not Valid.')
                continue 

    elif user_action.startswith('exit'):
        break

    else:
        print('Command is not Valid')

print('Bye !!')                