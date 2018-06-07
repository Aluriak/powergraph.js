"""Convert bubble files into JS file for cytoscape.js.

usage:
    python make_from_bubble.py <bblfile> <output file>

"""

import sys
from bubbletools import BubbleTree, utils
from bubbletools.utils import reversed_graph
from data import JS_HEADER, JS_MIDDLE, JS_FOOTER, JS_NODE_LINE, JS_EDGE_LINE


def bbl_to_cys(bblfile:str, width_as_cover:bool=True, show_cover:str='cover: {}'):
    """Yield lines of js to write in output file"""
    tree = BubbleTree.from_bubble_file(bblfile, symmetric_edges=False)
    yield from JS_HEADER
    def isclique(node):  return node in tree.edges.get(node, ())
    for node in tree.roots:
        yield JS_NODE_LINE(node, clique=isclique(node))
    parents = reversed_graph(tree.inclusions)  # (power)node -> direct parent
    for node, parents in parents.items():
        assert len(parents) == 1, {node: parents}
        yield JS_NODE_LINE(node, next(iter(parents)), clique=isclique(node))

    yield from JS_MIDDLE

    use_cover = width_as_cover or show_cover
    if use_cover:
        def coverof(source, target) -> int:
            source_cover = sum(1 for _ in tree.nodes_in(source))
            target_cover = sum(1 for _ in tree.nodes_in(target))
            return (source_cover or 1) * (target_cover or 1)
        def labelof(cover:int) -> str or None:
            if cover > 1:  # it's a power edge
                return show_cover.format(cover)
    # Now, (power) edges
    powernodes = frozenset(tree.powernodes())
    for source, targets in tree.edges.items():
        for target in targets:
            if target == source:  continue  # cliques are not handled this way
            label, attrs, isreflexive = None, {}, False
            ispower = source in powernodes or target in powernodes
            if use_cover:
                cover = coverof(source, target)
                label, attrs = labelof(cover), {'width': 2+cover}
            yield ' '*8 + JS_EDGE_LINE(source, target, ispower, label=label, attrs=attrs)

    yield from JS_FOOTER



if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(__doc__)
        exit()
    with open(sys.argv[2], 'w') as outfd:
        for line in bbl_to_cys(sys.argv[1]):
            outfd.write(line + '\n')
