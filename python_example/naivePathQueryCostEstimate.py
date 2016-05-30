import sys


def main():
    graph_file_name = sys.argv[1]
    maximum_path_length = sys.argv[2]
    budget = sys.argv[3]
    # From the file, create Node and Edge objects which are all linked up , which makes the graph.
    nodes, edges = build_graph(graph_file_name)
    # According to the assignement, we must write the size of the datastructure to standard out and wait for input.
    sys.stdout.write(str(sys.getsizeof(nodes) + sys.getsizeof(edges)) + "\n")

    message = sys.stdin.readline()
    while message != "\n":
        message = message.replace("+", "")
        message = message.replace("-", "")
        message.strip()
        edge_labels = message.split()
        estimated_hits = 0
        for edge in edge_labels:
            estimated_hits += len(edges[edge])
        sys.stdout.write(str(estimated_hits) + "\n")
        message = sys.stdin.readline()

    sys.stdout.write("")


def build_graph(graph_file_name):
    nodes = {}
    edges = {}
    graph_file = open(graph_file_name, "r")
    for line in graph_file.readlines():
        line = line.split(" ")
        edge_type = line[1].strip()
        startNode = getOrCreateNode(nodes, line[0].strip())
        endNode = getOrCreateNode(nodes, line[2].strip())
        edge = Edge(startNode, endNode, edge_type)
        startNode.outgoing.append(edge)
        endNode.incoming.append(edge)
        registerEdge(edges, edge)
    return nodes, edges


def getOrCreateNode(nodes, node_id):
    if node_id in nodes:
        return nodes[node_id]
    else:
        node = Node(node_id, [], [])
        nodes[node_id] = node
        return node


def registerEdge(edges, edge):
    if edge.type in edges:
        edges[edge.type].append(edge)
    else:
        edges[edge.type] = [edge]


class Edge(object):
    """A Directed Edge in the graph.

    Attributes:
        start node: the node at the start of this edge
        end node: The node at the end of this edge
        type: the type of this edge.
    """

    def __init__(self, start, end, type_id):
        """Return an edge """
        self.start = start
        self.end = end
        self.type = type_id


class Node(object):
    """A Node in the graph.

    Attributes:
        outgoing edges: a list of edges with this node as the start node
        incoming edges: a list of endges with this node as the end node
    """

    def __init__(self, node_id, outgoing, incoming):
        """Return a node """
        self.node_id = node_id
        self.outgoing = outgoing
        self.incoming = incoming


main()
