import csv
import json
import os
import subprocess
import sys

import time


def main():
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

    os.chdir(test_project_location)

    subprocess.Popen("./setup.sh", stdout=subprocess.DEVNULL).wait()

    start_time = time.time()
    child = subprocess.Popen(["./run.sh", graph_file, maximum_path_length, budget],
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             bufsize=1, universal_newlines=True)
    dataset_time = time.time() - start_time
    size = child.stdout.readline().strip()

    start_time = time.time()
    with open(queries_file, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        result = {"path_results": []}
        sum_difference = 0
        query_count = 0
        for row in reader:
            path, actual = row
            child.stdin.write(path + "\n")
            estimate = child.stdout.readline().strip()
            difference = abs(int(estimate) - int(actual))
            sum_difference += difference
            query_count += 1
            result["path_results"].append(
                {"path": path.strip(), "estimate": estimate.strip(), "actual": actual.strip(),
                 "difference": difference})

    query_time = time.time() - start_time

    average_quality = sum_difference / float(query_count)

    result["score"] = compute_score(dataset_time, int(size), int(budget), query_time, average_quality)
    result["size"] = size
    result["dataset_time"] = dataset_time
    result["query_time"] = query_time
    print(json.dumps(result))

    child.stdin.write(("\n"))


def compute_score(dataset_time, bytes_used, budget, query_time, average_query_quality):
    a = 1 / 6
    b = 1 / 6
    c = 1 / 3
    d = 1 / 3

    score = a * (dataset_time) + \
            b * (budget / bytes_used) + \
            c * (query_time) + \
            d * (average_query_quality)

    return score


main()
