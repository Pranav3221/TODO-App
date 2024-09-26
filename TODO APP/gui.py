import functions
import FreeSimpleGUI as sg

label=sg.Text('Type a TO-DO below:')
add_button=sg.Button('Add')
user_input=sg.InputText(tooltip='Type Here')


window=sg.Window('My To-Do App', layout=[[label],[user_input,add_button]])
window.read()
window.close()

new