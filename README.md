## Django command line interface(CLI)
This CLI (Command Line Interface) is designed for Django developers to quickly and easily execute common Django management commands without typing out the full command each time. Users can simply enter a shorthand command into the CLI and the corresponding Django command will be executed.

The custom CLI, the user can simply enter `rs` instead of typing out the full `python manage.py runserver` command. This can save time and effort, especially for commands with longer names or that are frequently used. The CLI also includes error handling and support for passing arguments to certain commands.
> `rs 8080` 

>`sa app_naame`

## Installetion
* Create a New python file in the root directory of your django project.
* Copy and paste this code inside the file and save it.
* Open terminal and run `python file_name.py` the it will display ` django_cli->` now our django cli is running.
* You can also use `help` command to see supported command.
* You can enter any of the supported commands followed by any necessary arguments `rs 8080`

## License
This project is licensed under the MIT License - see the [LICENSE](/LICENSE.md) file for details.

## Acknowledgments
This script was inspired by the Django CLI script in the [Django Girls tutorial](https://tutorial.djangogirls.org/en/intro_to_command_line/).