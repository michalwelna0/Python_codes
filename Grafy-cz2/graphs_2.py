# Michal Welna 302935
from typing import List, Set, Dict, NamedTuple
from enum import Enum, auto
import networkx as nx

VertexID = int
EdgeID = int
WageEdge = float

AdjMatrix = List[List[int]]

AdjList = Dict[VertexID, List[VertexID]]

Distance = int

class TrailSegmentEntry(NamedTuple):
    start_vertex : VertexID
    end_vertex : VertexID
    edge_id : EdgeID
    wage_g : WageEdge

Trail = List[TrailSegmentEntry]

class Vertexet(NamedTuple):
    vertex_id : int
    distance: int

class Colour(Enum):
    white = auto()
    grey = auto()
    black = auto()

def neighbors(adjlist: AdjList, start_vertex_id: VertexID, max_distance: Distance) -> Set[VertexID]:
    expected_set,colours,stack = set(), {}, []
    tuple_vertex = Vertexet(start_vertex_id, 0)
    for u in adjlist:
       colours[u] = Colour.white
    colours[tuple_vertex.vertex_id] = Colour.grey
    stack.append(tuple_vertex)

    while stack:
        u = stack.pop()
        if u.distance <= max_distance and u.vertex_id != start_vertex_id:
            expected_set.add(u.vertex_id)
        if u.vertex_id in adjlist:
            for v in adjlist[u.vertex_id]:
                if v not in colours:
                    buff = Vertexet(v, u.distance + 1)
                    stack.append(buff)
                    continue
                elif colours[v] == Colour.white:
                    colours[v] = Colour.grey
                    buff = Vertexet(v,u.distance + 1)
                    stack.append(buff)
            colours[u] = Colour.black
    return expected_set



def load_multigraph_from_file(filename: str) -> nx.MultiDiGraph:

    G = nx.MultiDiGraph()
    with open(filename) as f:
        lines = (line.rstrip() for line in f)
        lines = list(line for line in lines if line)

    for elem in lines:
        a,b,c = elem.split()
        a = int(a)
        b = int(b)
        c = float(c)

        G.add_weighted_edges_from([(a,b,c)])
    return G

def find_min_trail(g: nx.MultiDiGraph, v_start: VertexID, v_end: VertexID) -> Trail:
    path_list = []
    atlas_list = []
    weight_lst = []
    trl_lst = []

    for elem in nx.dijkstra_path(g, v_start, v_end):
        path_list.append(elem)

    for elem in range(len(path_list) - 1):
        atlas_list.append(g[path_list[elem]][path_list[elem + 1]])

    for idx, elem in enumerate(atlas_list):
        if len(atlas_list[idx]) != 1:
            help_lst = []
            for el in range(len(atlas_list[idx])):
                help_lst.append(atlas_list[idx][el]['weight'])
            weight_lst.append(min(help_lst))
        else:
            weight_lst.append(atlas_list[idx][0]['weight'])

    for elem in range(len(path_list) - 1):
        if len(atlas_list[elem]) == 1:
            trl = TrailSegmentEntry(path_list[elem], path_list[elem + 1], 0, weight_lst[elem])
            trl_lst.append(trl)
        else:
            buff = []
            for idx, el in enumerate(atlas_list[elem]):
                tup = el, atlas_list[elem][idx]['weight']
                buff.append(tup)
            buff.sort(key=lambda x: x[1])
            a, b = buff[0]

            trl = TrailSegmentEntry(path_list[elem], path_list[elem + 1], a, weight_lst[elem])
            trl_lst.append(trl)
    return trl_lst


def trail_to_str(trail: Trail) -> str:

    strg = ''
    sumw = 0
    for i in trail:
        sumw += i.wage_g
    for i in trail:
        strg+='{} -[{}: {}]-> '.format(i.start_vertex,i.edge_id,i.wage_g)
    strl= strg + '{}  (total = {})'.format(trail[-1].end_vertex, sumw)
    return strl

