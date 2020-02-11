Python Lab -- To Do List

This repo is a simple to do list built using python, django, andh html/css.

Here you will be able to add, update, and delete various tasks and things you may need to get done.

Our models and forms are Tasks and Groups. Groups group all the various tasks together. These can be any name, but we choose days of the week in our intial seed for consistancy. Tasks are things to do get done. We have an intial seed to get started. There is also some included CSS to get things started.

SETTINGS.py

    Make sure to add todo to INSTALLED_APPS
    
    DATABASE:
        ENGINE: 'leave as is'
        NAME: todo
        USER: todouser
        PASSWORD: todo
        HOST: localhost

    Note that we have some dummy data so all you have to do is 'makemigrations'.

Models.py:

    Group:
        group_name = name of list, CharField

    Task:
        task_name = name of task, CharField
        finished = boolean value(true/false)
        notes = additonal notes, TextField
        group = links to group model, ForiegnKey

Forms.py:

    Group:
        group_name = assign it a name

    Task:
        task_name = name if the task
        finished = auto potulates to false
        notes = addiotnal information
        group = assign it to a group

Views.py:

    group_list:
        lists groups
    
    group_detail:
        show a detailed group

    group_create:
        creates a new group

    group_update:
        updates an existing group

    group_delete:
        deletes and existing group
    
    task_list:
        lists tasks
    
    task_detail:
        show a detailed task

    task_create:
        creates a new task

    task_update:
        updates an existing task

    task_delete:
        deletes and existing task
    

URLs.py:
    path '':
    "It's all teh correct paths"

Future plans to implement:
    --Automagiclaly assign tasks to current group(Fills in group section in form)
    --Finishing a task automatically deletes it
    --Make it look less terrible