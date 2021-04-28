import pytest
import inspect
from graph import Graph, main
import io
import math

def test_vertex_edge_weight():
    g = Graph()
    with pytest.raises(ValueError):
        g.add_vertex(0)
    g.add_vertex("A")
    x = g.add_vertex("B")
    with pytest.raises(ValueError):
        g.add_edge("A", "cat", 10.0)
    with pytest.raises(ValueError):
        g.add_edge("A", "B", "cat")
    assert isinstance(x, Graph)
    x = g.add_edge("A", "B", 10.0)
    assert g.get_weight("A", "B") == 10
    assert g.get_weight("B", "A") == math.inf
    assert isinstance(x, Graph)

def test_bfs():
    g = Graph()
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")
    g.add_vertex("E")
    g.add_vertex("F")

    g.add_edge("A", "B", 1.0)
    g.add_edge("A", "C", 1.0)

    g.add_edge("B", "D", 1.0)

    g.add_edge("C", "E", 1.0)

    g.add_edge("E", "F", 1.0)

    gen = g.bfs("A")
    data = [x for x in gen]
    assert data[0] == "A"
    assert data[-1] == "F"
    assert len(data) == 6
    gen = g.bfs("C")
    data = [x for x in gen]
    assert len(data) == 3

def test_dfs():
    g = Graph()
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")
    g.add_vertex("E")
    g.add_vertex("F")

    g.add_edge("A", "B", 1.0)
    g.add_edge("A", "C", 1.0)

    g.add_edge("B", "D", 1.0)

    g.add_edge("C", "E", 1.0)

    g.add_edge("E", "F", 1.0)

    gen = g.dfs("A")
    data = [x for x in gen]
    assert data[0] == "A"
    assert data[-1] in ("D", "F")
    assert len(data) == 6
    gen = g.dfs("C")
    data = [x for x in gen]
    assert len(data) == 3

def test_print():
    g = Graph()
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")
    g.add_vertex("E")
    g.add_vertex("F")

    g.add_edge("A", "B", 1.0)
    g.add_edge("A", "C", 1.0)

    g.add_edge("B", "D", 1.0)

    g.add_edge("C", "E", 1.0)

    g.add_edge("E", "F", 1.0)
    
    expected ='''digraph G {
   A -> B [label="1.0",weight="1.0"];
   A -> C [label="1.0",weight="1.0"];
   B -> D [label="1.0",weight="1.0"];
   C -> E [label="1.0",weight="1.0"];
   E -> F [label="1.0",weight="1.0"];
}
'''
    output = str(g)
    assert output == expected
    
def test_dsp():
    g = Graph()
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")
    g.add_vertex("E")
    g.add_vertex("F")

    g.add_edge("A", "B", 2)
    g.add_edge("A", "F", 9)

    g.add_edge("B", "F", 6)
    g.add_edge("B", "D", 15)
    g.add_edge("B", "C", 8)

    g.add_edge("C", "D", 1)

    g.add_edge("E", "C", 7)
    g.add_edge("E", "D", 3)
    
    g.add_edge("F", "B", 6)
    g.add_edge("F", "E", 3)

    dist, path = g.dsp("A", "B")
    assert path == ['A', 'B']
    dist, path = g.dsp("A", "C")
    assert path == ['A', 'B', 'C']
    dist, path = g.dsp("A", "D")
    assert path == ['A', 'B', 'C', 'D']
    dist, path = g.dsp("A", "F")
    assert path == ['A', 'B', 'F']
    dist, path = g.dsp("D","A")
    assert path == []

def test_dsp_all():
    g = Graph()
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")
    g.add_vertex("E")
    g.add_vertex("F")

    g.add_edge("A", "B", 2)
    g.add_edge("A", "F", 9)

    g.add_edge("B", "F", 6)
    g.add_edge("B", "D", 15)
    g.add_edge("B", "C", 8)

    g.add_edge("C", "D", 1)

    g.add_edge("E", "C", 7)
    g.add_edge("E", "D", 3)
    
    g.add_edge("F", "B", 6)
    g.add_edge("F", "E", 3)

    paths = g.dsp_all("A")
    assert isinstance(paths, dict)
    assert paths == {'A':['A'], 'B':['A', 'B'], 'C':['A', 'B', 'C'], 'D':['A', 'B', 'C', 'D'], 'E':['A', 'B', 'F', 'E'], 'F':['A', 'B', 'F']}
    
    paths = g.dsp_all("D")
    assert isinstance(paths, dict)
    assert paths == {'A': [], 'B':[], 'C':[], 'D':['D'], 'E':[], 'F':[]}

def test_for_main():
    ''' we just test for existence '''
    assert inspect.isfunction(main)
    
def test_code_quality():
    from pylint import epylint as lint
    import re
    
    (pylint_stdout, pylint_stderr) = lint.py_run('graph.py', return_std=True)
    expected = 8.5
    actual = pylint_stdout.getvalue()
    x = re.findall('[0-9]+', actual)[0]
    x = float(x)
    assert x >= expected




