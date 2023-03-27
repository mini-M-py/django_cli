import subprocess
import time

commmand_dict ={
                "rs":"runserver",
                'sa': "startapp",
                 'mk': 'makemigrations',
                 'mg': 'migrate',
                 'cls': 'collectstatic',
                 "check": "check",
                 "cpm": "compilemesseges",
                 "cct": "createcachetable",
                 "csu": "createsuperuser",
                 "shell": 'shell',
                 'fst':'findstatic',
                 'clrs':'clearsession',
                 'ts': 'testserver',
                 'test':'test',
                 'smg':'squashmigrations',
                 'ssr':'sqlsequencerest',
                 'sm':'sqlmigrate',
                 'sf': 'sqlflush',
                 'shm':'showmigrations',
                 'ste':'sendtestemail',
                 'omg':'optimizemigration',
                 'ld':'loaddata',
                 'idb':'inspectdb',
                 'flush':'flush',
                 'dd':'dumpdata',
                 'ds':'diffsetting',
                 'dbs':'dbshell',
}

command = 'python manage.py'

while True:
    line = input("django_cli-> ")

    
    
    if " " in line:
        parts = line.split(' ')
        if parts[0] not in commmand_dict:
            print(f'invalid command {parts[0]}')
        else:
            command_args = command + ' ' + commmand_dict[parts[0]] + ' ' + parts[1]
            subprocess.call(command_args, shell = True)

    if line == 'help':
        print('available commands:')
        for key, value in commmand_dict.items():
            print(f'{key}: {value}')
    
    elif line not in commmand_dict:
        print(f'invalid command {line}')
    
    else:
        command_line = command + " " + commmand_dict[line]

        subprocess.call(command_line, shell = True)

        time.sleep(1)