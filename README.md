This is the CLI for Task Tracker by Ridwan Amirul Maulana (Me)

# How to use

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