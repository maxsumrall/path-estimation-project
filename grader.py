import subprocess
import os

# choose which example to use
test_project_location = ["python_example", "java_example"][1]


# A script to execute the setup and run scripts supplied by the students.
# All input and output to the students programs are expected to be newline terminated.
def main():
    file = "biblio.data.txt"
    maximum_path_length = "10"
    budget = "1000000"

    abs_path = os.path.abspath(file)

    project_directory = "python_example/"

    # Students programs are first setup with this script.
    # For Python or other interrupted programs, nothing needs to be done inside the script.
    # For compiled programs, this is where you invoke the compiler.
    subprocess.call("cd " + test_project_location + " && ./setup.sh && cd ..", shell=True)

    # Students programs are invoked with this script.
    # This script may be called many times. That is why you should do setup
    # tasks in the setup script and not in this script.
    cmd = "cd " + test_project_location + " && ./run.sh " + abs_path + " " + maximum_path_length + " " + budget
    print(cmd)
    child = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

    # The process must first send the size of the data structure
    size = getResponse(child)

    # The first path, with edge label "0"
    send("0", child)
    # The process must respond with it's estimate
    estimateA = getResponse(child)

    # The second path with edge labels "10, 10"
    send("2 1", child)
    # The process must respond with it's estimate
    estimateB = getResponse(child)

    # A signal to the process that there are no more estimates.
    send("", child)

    print("Size: " + size + ", estimate #1: " + estimateA + ", estimate #2: " + estimateB)


def send(message, child):
    child.stdin.write((message + "\n").encode())
    child.stdin.flush()


def getResponse(child):
    response = child.stdout.readline().decode().strip()
    return response


main()
