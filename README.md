# CS4032 Lab2

## Student
Name : David Hegarty <br/>
Student ID: 13332863

## Description
Construct a multithreaded skeleton TCP server, supporting thread pooling.

## Dependencies
Python 2.7.9

## How To Use
To execute the service, first run the _compile.sh_ script via the following command:

```
./compile.sh
```
This will ensure the program is compiled. 

Next, execute the service via the _*start.sh*_ script, by typing the following command into your terminal:

```
./start.sh portnumber
```
 where _portnumber_ should be replaced with the port you wish to use.

 The IP address is hardcoded, however this can be changed via modifying line 7 of the server.py file,
 by replacing the contents of the double quotes with the desire IP address

