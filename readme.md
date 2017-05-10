Assumes `doit` is installed. 

This can be installed via pip, make sure you choose the right version appropriate Python

```sh
pip install doit==0.29.0
```

Running this repository is done in a few ways, we can use:

```sh
doit build
```

```sh
doit run
```

```sh
doit test
```

Tasks can be selected via [`DOIT_CONFIG`](http://pydoit.org/tasks.html#doit-config-default-tasks)

```py
DOIT_CONFIG = {'default_tasks': ['t3']}

def task_t1():
    return {'actions': ["touch task1"],
            'targets': ['task1']}

def task_t2():
    return {'actions': ["echo task2"]}

def task_t3():
    return {'actions': ["echo task3"],
            'file_dep': ['task1']}

```

Based on how we have set up our repository, we can run the following:

```sh
# run nosetests
doit tests

# run python sample.py
doit "run sample"
```



