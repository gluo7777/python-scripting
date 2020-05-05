import json

with open(file=r'NoteBook.json',mode='r') as fp:
    notebook = json.load(fp=fp)
    print(notebook['Java']['notes'])
    if 'heading1' not in notebook:
        notebook['heading1'] = {'notes':['a','b']}
        print(notebook)