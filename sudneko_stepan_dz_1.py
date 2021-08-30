import os

dir_sample = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
for r, f in dir_sample.items():
    if os.path.exists(r):
        print(r, 'уже существует')

    else:
        for folder in f:
            current_dir = os.path.join(r, folder)
            os.makedirs(current_dir)