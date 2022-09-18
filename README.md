# A todo list

## Description
The backend uses Flask, SQLite with SQLAlchemy, and Python. 
The front end uses HTML and the SemanticUI Componenet Framework. 

### Features
This is a CRUD app.
    - You can create one or many task to add to your list.
    - Pressing update change the status label from incomplete to complete with a green label background
    - You can undo the status by pressing update again
    - You can delete the task regardless if you have completed it or not.
 

## Installing project using Poetry:
1. You should have Poetry and Python(3.10) installed  
2. Clone the repo
3. Open the terminal and cd into the project directory
4. Run the command: poetry install 
5. Activate the virtual enviorment: .venv\Scripts\activate
6. This will run it in the development enviorment: python app.py

### Addition information
This Todo list was created following a tutorial from Python Engineer on YouTube.
One of the modifications I did was not allowing a user to add an empty todo task.
I hope to coninue adding more to make it my own.


<img src="img\todo-list.png" width="100" height="100">