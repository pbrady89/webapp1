import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state['new_todo'] = ''


st.title('My Todo App')
st.subheader('This is my todo app')
st.write('This app is to increase your productivity')


for index, todo in enumerate(todos):
    check_box = st.checkbox(todo, key=index)
    if check_box:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[index]
        st.rerun()

st.text_input(label='New Todos', placeholder='Write New Todo Here...', on_change=add_todo, key='new_todo')
