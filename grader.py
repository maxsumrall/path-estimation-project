import subprocess
import os

# choose which example to use
import time

test_project_location = ["python_example", "java_example", "c_example"][0]


# A script to execute the setup and run scripts supplied by the students.
# All input and output to the students programs are expected to be newline terminated.
def main():
    file = "biblio.txt"
    maximum_path_length = "10"
    budget = "1000000"

    abs_path = os.path.abspath(file)

    # Students programs are first setup with this script.
    # For Python or other interrupted programs, nothing needs to be done inside the script.
    # For compiled programs, this is where you invoke the compiler.
    subprocess.call("cd " + test_project_location + " && ./setup.sh && cd ..", shell=True)

    # Students programs are invoked with this script.
    # This script may be called many times. That is why you should do setup
    # tasks in the setup script and not in this script.
    cmd = "cd " + test_project_location + " && ./run.sh " + abs_path + " " + maximum_path_length + " " + budget
    print(cmd)
    child = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

    # The process must first send the size of the data structure
    size = getResponse(child)

    queries = open("biblio.csv", "r")
    line = queries.readline()
    while line != "":
        line = line.split(",")
        path = line[0]
        actual = line[1]
        send(path, child)
        # The process must respond with it's estimate
        estimate = getResponse(child)
        print("Path: " + path + " Estimate: " + estimate + " Actual: " + actual)
        line = queries.readline()

    # A signal to the process that there are no more estimates.
    send("", child)


def send(message, child):
    child.stdin.write((message + "\n").encode())
    child.stdin.flush()


def getResponse(child):
    response = child.stdout.readline().decode().strip()
    return response


main()
