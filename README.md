# Task Tracker CLI

This is a challenge from Roadmap.sh to create a simple CLI for Task Tracker where people can track and manage their tasks. The project was written in Python while JSON is used to store the tasks.

## Usage

### Add tasks 
```sh
python task_cli.py add "Buy groceries"
# Output: Task added successfully (ID: 1)
```

### Update tasks 
```sh
python task_cli.py update 1 "Buy groceries and cook dinner"
# Output: Task updated successfully
```

### List All tasks 
```sh
python task_cli.py list
```

### List tasks by Status
```sh
python task_cli.py list todo
python task_cli.py list in-progress
python task_cli.py list done
```

### Delete task 
```sh
python task_cli.py delete 1
# Output: Task deleted successfully
```