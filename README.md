# Path Estimation Project

This repository contains a script to interact with a program that estimates the cost of a path query. It gives the program input in the form of a file name which contains the information to create the graph, the maximum length of paths that will be asked to estimate, and a budget of how many bytes the program may use to construct a data structure which is used to provide the estimations. This script then feeds the program path (in the form of sets of edge labels) and expects estimations from the program in return. 

## Example interaction

Here is an example interaction between this script and your program. 


```
$ graph.data.txt 4 10000 //The first input.
$ 98745            //The size of the data structure.
$ + 0              //Three edge labels of a path to estimate.
$ 482              //The estimated number of paths with those labels.
$ + 5 + 0          //Three more labels of a path to estimate.
$ 216              //The program estimated no paths in the graph.
$                  //An empty string, notifying your program to terminate.
```

## Getting Started

To help you get started with input and output to this script, an example project in Python, Java, and C++ have been provided.

To test your program locally, or to test the different example projects, you can edit the file `grader.py` to point to the folder of the project you want to test. If you want to test the Python project, set the variable `test_project_location` to 

```
test_project_location = ["python_example", "java_example", "c_example”][0]
```

To test the Java project, set this line to

```
test_project_location = ["python_example", "java_example", "c_example”][1]
```

To test the C++ project, set this line to 

```
test_project_location = ["python_example", "java_example", "c_example"][2]
```