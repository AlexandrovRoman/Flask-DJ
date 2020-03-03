def create_file(path, name, template):
    with open(f'{path}\\{name}.py', 'w') as f:
        f.write(template)
