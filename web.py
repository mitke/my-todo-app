import streamlit as st
from modules import functions

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


todos = functions.get_todos()

st.title("My Todo App")
#st.subheader("This is my todo app")
st.write("")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="unos nove stavke", label_visibility='collapsed',
              placeholder="Add new TODO...", on_change=add_todo, key='new_todo')

print("Zdravo!")

st.session_state
