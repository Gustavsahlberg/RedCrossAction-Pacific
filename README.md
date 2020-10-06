# RedCrossAction-Pacific

**Table of contents**

[Installation](#installation)

[Server](#Server)

## Installation
We are using Django framework for Python.

To install Django you will need to run this following command in your commandline:
```
$ pip3 install Django==3.1.2
```
To check if Django is installed run this command:
```
$ python3 -m django --version
```

### Windows

To setup the workspace in Windows you will need to do the following:
1) Install Python 3.8.5.
2) Run `setup.bat` in the projects root directory

### Linux

To setup the workspace in Linux you will need to run the following command in your terminal:
```bash
$ ./setup.sh
```


## Server

### Windows

Run the following command in the root directory to start the server:
```
./run.bat
```


### Linux

Run the following command to start our server:
```
$ ./run.sh
```

Both files can take an optional argument for the port number to run the server on. The port `8000` will be used if no port number is specified.

### These files are mainly for development purposes and shouldn't be used in production.