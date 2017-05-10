DOIT_CONFIG = {'default_tasks': ['test']}

def task_tests():
    return {'actions': ["nosetests --exe"]}

def gen_pipeline():
    yield {'basename': 'run pipeline',
           'actions': ['echo runpipeline'], 
           'verbosity': 2}
    yield {'basename': 'run test', 
           'actions': ['echo runtest'], 
           'verbosity': 2}
    
    yield {'basename': 'run sample', 
           'actions': ['python sample.py'], 
           'verbosity': 2}

def task_all():
    yield gen_pipeline()

