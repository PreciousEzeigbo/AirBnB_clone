## DESCRIPTION

A complete web application composed by:

* A command interpreter to manipulate data without a visual interface
* A website that shows the final product to everybody: static and dynamic
* A database or files that store data
* An API that provides a communication interface between the website and the data


## Command Interpreter

A versatile tool designed to provide efficient and direct interaction through a text-based interface.

### Getting Started

You can initiate the Command Interpreter by running the command ./console.py.

### Usage

* Within the console, you have the capability to create, destroy, and update objects.
* To access a comprehensive list of available commands along with their functions, simply type help.

### Examples

```bash
abdel-moaty@ubuntu:~/AirBnB$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb) help quit
Quit command to exit the program

(hbnb)
(hbnb)
(hbnb) quit
abdel-moaty@ubuntu:~/AirBnB$
abdel-moaty@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.count()
2
(hbnb) User.destroy("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
(hbnb) User.count()
1
(hbnb) User.destroy("Bar")
** no instance found **
(hbnb)
```
