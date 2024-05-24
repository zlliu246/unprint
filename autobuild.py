import os

commands = [
    'rm -rf ./dist',
    'python3 -m build',
    'python3 -m twine upload dist/*'
]

for command in commands:
    print(command)
    os.system(command)