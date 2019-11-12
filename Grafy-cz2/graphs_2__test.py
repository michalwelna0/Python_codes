# Michal Welna 302935

import unittest
from BFS import graphs_2 as gr
import networkx as nx

class TestGraphs2(unittest.TestCase):

    def test_load_multigraph_from_file(self):
        G = gr.load_multigraph_from_file('directed_graphe_blank_lines.txt')
        graph = nx.MultiDiGraph()
        graph.add_weighted_edges_from([(1, 2, 0.5), (2, 3, 0.4), (2, 3, 0.3), (1, 3, 1.0)])
        self.assertEqual(nx.info(G), nx.info(graph))

    def test_find_min_trail(self):
        graph = nx.MultiDiGraph()
        graph.add_weighted_edges_from([(1, 2, 0.5), (2, 3, 0.4), (2, 3, 0.3), (1, 3, 1.0)])
        buff = [gr.TrailSegmentEntry(start_vertex=1, end_vertex=2, edge_id=0, wage_g=0.5), gr.TrailSegmentEntry(start_vertex=2, end_vertex=3, edge_id=1, wage_g=0.3)]
        self.assertEqual(gr.find_min_trail(graph,1,3), buff)
        self.assertEqual(0.8, nx.dijkstra_path_length(graph,1,3))

    def test_trail_to_string(self):
        graph = nx.MultiDiGraph()
        graph.add_weighted_edges_from([(1, 2, 0.5), (2, 3, 0.4), (2, 3, 0.3), (1, 3, 1.0)])
        buff = gr.find_min_trail(graph,1,3)
        stry = gr.trail_to_str(buff)
        self.assertEqual(stry,'1 -[0: 0.5]-> 2 -[1: 0.3]-> 3  (total = 0.8)')


if __name__ == '__main__':
    unittest.main()
