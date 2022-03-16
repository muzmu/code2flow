import ast

with open('data.txt') as f:
    data = ast.literal_eval(f.read())
    print(data[0])
