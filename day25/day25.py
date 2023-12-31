#using networkx, hyperneutrino solution too, to revisit later
import networkx as nx

graph = nx.Graph()

with open('day25/input.txt') as f:
    for line in f.readlines():
        left, right = line.split(":")
        for node in right.strip().split():
            graph.add_edge(left, node)
            graph.add_edge(node, left) # graph is not directional

edges_to_cut = nx.minimum_edge_cut(graph)# get the minimum edge needed to cut the graph in two
graph.remove_edges_from(edges_to_cut) # proceed to cut those edges
comp1, comp2 = nx.connected_components(graph) # get two components of the resulting graph

print(len(comp1) * len(comp2))