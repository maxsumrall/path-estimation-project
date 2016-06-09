import csv
import json
import os
import subprocess
import sys

# You must pass in the path to the queries csv file as the third argument
queries_file = os.path.abspath(sys.argv[1])
# You must pass in the path to the project to grade as the first argument
test_project_location = sys.argv[2]
# You must pass in the path to the file of the graph as the second argument
graph_file = os.path.abspath(sys.argv[3])
# You must pass in the maximum path length as the fourth argument
maximum_path_length = sys.argv[4]
# You must pass in the budget as the fifth argument.
budget = sys.argv[5]

# test_project_location = 'python_example'
# graph_file = os.path.abspath('biblio.txt')
# queries_file = os.path.abspath('biblio.csv')
# maximum_path_length = '10'
# budget = '10'

os.chdir(test_project_location)

subprocess.Popen("./setup.sh", stdout=subprocess.DEVNULL).wait()

child = subprocess.Popen(["./run.sh", graph_file, maximum_path_length, budget],
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         bufsize=1, universal_newlines=True)

with open(queries_file, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    result = {"path_results": []}
    for row in reader:
        path, actual = row
        child.stdin.write(path + "\n")
        estimate = child.stdout.readline().strip()
        result["path_results"].append({"path": path.strip(), "estimate": estimate.strip(), "actual": actual.strip()})
    result["score"] = "10"
    print(json.dumps(result))

child.stdin.write(("\n"))
