# **Todo-App**

A todo app that helps you set tasks and show them in a nice table all in the terminal. It is easily manageble by passing arguments to the main script.

## **Features**

- Terminal based
- Fast
- Uses sqlite3 database.
- Easily customizable


## **Installation**

### On Linux and MacOS
```
python3 -m pip3 install -r requirements.txt
```

### On Windows

1. Install `Windows Terminal` app from the app store
2. Install `python 3.x` also from the app store (if you just type `python` in the Windows Terminal app it will offer you to install)
3. If you have git installed, clone this repo 
```git
git clone https://github.com/n07f0und/todo-app
```
4. Install the program and libraries by typing in the Windows Terminal `pip3 install -r requirements.txt` inside the cloned repository.
5. Now you can finally run it by typing in the Windows Terminal `python3 todo.py --help`


## **Dependencies**

To run, it only requires python 3. On Linux and MacOS, you should have it by default, but if you don't, install `python3` package from your standard repository.


## **Usage**

Run `todo.py` in your terminal.
```bash
python3 todo.py [commands]
```

### Required user commands


```bash
add      -   Add a task to the list.
complete -   Complete a task and mark it.
delete   -   Delete a task from the list.
show     -   Print all tasks.
update   -   Update the database.
```


## **Contact me**

**For Queries: [Find me on Twitter](https://twitter.com/@_K3voh)**