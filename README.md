0x00. AirBnB clone - The console

Description:
The console serves as the initial component in the development of the AirBnB project, aiming to deploy a simplified version of the AirBnB website (HBnB). In this phase, a command interpreter has been designed to handle object management for the AirBnB website. This is the first step towards building our first full-fledged web application, the AirBnB clone.

Key functionalities of the command interpreter for managing AirBnB clone objects include:

Creating a new object.
Retrieving an object from either a file or a database.
Performing operations on objects.
Updating attributes of an object.
Destroying or removing an object

Example:

Your shell should work like this in interactive mode:
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit

But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 

