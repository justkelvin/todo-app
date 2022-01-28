#!/usr/bin/env python3

# Title: Todo-App
# Description: Lets you add and manage stuffs you do directly on the terminal
# Author: 
# Date: 2022-01-28
# Version: 2022.v1.3

import typer
from rich.console import Console
from rich.table import Table
from model import Todo
from database import get_all_todos, delete_todo, insert_todo, complete_todo, update_todo

console = Console()
app = typer.Typer()

@app.command(short_help="Add a task to the list.")
def add(task: str, category: str):
	typer.echo(f"Adding {task}, {category}")
	todo = Todo(task, category)
	insert_todo(todo)
	show()

@app.command(short_help="Delete a task from the list.")
def delete(position: int):
	typer.echo(f"Deleting {position}")
	# Indices in UI begin at 1 while in database at 0
	delete_todo(position-1)
	show()

@app.command(short_help="Update the database.")
def update(position: int, task: str = None, category: str = None):
	typer.echo(f"Updating {position}")
	update_todo(position-1, task, category)
	show()

@app.command(short_help="Complete a task and mark it.")
def complete(position: int):
	typer.echo(f"Complete {position}")
	complete_todo(position-1)
	show()

@app.command(short_help="Print all tasks.")
def show():
	tasks = get_all_todos()
	console.print("[bold magenta]Todos[/bold magenta]!", "💻")

	table = Table(show_header=True, header_style="bold blue")
	table.add_column("#", style="dim", width=6)
	table.add_column("Task", min_width=20)
	table.add_column("Category", min_width=12, justify="right")
	table.add_column("Done", min_width=12, justify="right")

	def get_category_color(category):
		COLORS = {'Learn': 'Cyan', 'YouTube': 'red', 'Sports': 'cyan', 'Study': 'green'}
		if category in COLORS:
			return COLORS[category]
		return 'white'

	for idx, task in enumerate(tasks, start=1):
		c = get_category_color(task.category)
		is_done_str = '✅' if task.status == 2 else '❌'
		table.add_row(str(idx), task.task, f'[{c}]{task.category}[/{c}]', is_done_str)
	console.print(table)

if __name__ == "__main__":
	app()