
from itertools import count
_next_uid = count(1)
next_uid = lambda: next(_next_uid)


def JS_NODE_LINE(id:str, parent:str=None, clique:bool=False) -> str:
    attrs = {'id': id}
    if parent:
        attrs['parent'] = parent
    if clique:
        attrs['type'] = 'clique'
    return ' '*8 + "{{ data: {{ {} }} }},".format(', '.join(f"'{k}': '{v}'" for k, v in attrs.items()))

def JS_EDGE_LINE(source:str, target:str, ispoweredge:bool, isreflexive:bool=False,
                 id:str or int='', label:str='', attrs:dict={}) -> str:
    """

    >>> JS_EDGE_LINE('a', 'b', True)
    "        { data: { source: 'a', target: 'b', type: 'poweredge' } },"

    >>> JS_EDGE_LINE('a', 'b', False)
    "        { data: { source: 'a', target: 'b' } },"

    >>> JS_EDGE_LINE('PWRN-a-1-1', 'PWRN-a-1-2', True)
    "        { data: { source: 'PWRN-a-1-1', target: 'PWRN-a-1-2', type: 'poweredge' } },"

    """
    classes = []
    end = ''
    if ispoweredge: end += ", type: '{}poweredge'".format('reflexive-' if isreflexive else '')
    if label:
        end += f", label: '{label}'"
        classes.append('autorotate')
    if classes:
        end += " }, classes: '" + ' '.join(classes) + "' },"
    else:
        end += " } },"
    id = str(id if id else next_uid())
    if attrs:
        attrs = ', ' + ', '.join(f"'{k}': '{v}'" for k, v in attrs.items())
    else:
        attrs = ''
    return ' '*8 + f"{{ data: {{ source: '{source}', target: '{target}'" + attrs + end


JS_FOOTER = """
    ]
  },

  layout: {
    name: 'cose-bilkent',
    numIter: 4000,
    initialEnergyOnIncremental: 0.9,
    refresh: 30,  // FPS
    fit: true,  // fit at the end
    padding: 20,  // fit padding
    animate: false,  // 'during' or 'end' or false

    nodeDimensionsIncludeLabels: true, // Avoid label overlap
    randomize: true,
    nodeRepulsion: 8500,
    idealEdgeLength: 60,  // in compounds
    edgeElasticity: 0.40,
    nestingFactor: 0.2001,  // force for edges inter-compounds

    gravity: 0.20,
    gravityRange: 1.8,
    gravityCompound: 0.9,
    gravityRangeCompound: 1.3,

    tile: true,  // tile disconnected nodes
    tilingPaddingVertical: 10,
    tilingPaddingHorizontal: 10,
  }
});
""".strip().splitlines(False)


JS_MIDDLE = """
    ],
    edges: [
""".strip().splitlines(False)


JS_HEADER = """
var cy = window.cy = cytoscape({
  container: document.getElementById('cy'),

  boxSelectionEnabled: false,
  autounselectify: true,

  style: [
    {
        selector: 'node',
        css: {
            'content': 'data(id)',
            'text-valign': 'center',
            'text-halign': 'center'
        }
    },
    {
        selector: 'node[type="clique"]',
        css: {
            'border-color': 'green',
        }
    },
    {
        selector: '$node > node',
        css: {
            'padding': '30px',
            'text-valign': 'top',
            'text-halign': 'center',
            'background-color': '#eee'
        }
    },
    {
        // selector: 'edge[type="edge"]',
        selector: 'edge',
        css: {
            'label': 'data(label)',
            'width': '1',
            'target-arrow-shape': 'none',
            'source-arrow-shape': 'none',
            //'target-arrow-color': 'black',
        }
    },
    {
        selector: '.autorotate',
        css: { 'edge-text-rotation': 'autorotate' }
    },
    {
        selector: 'edge[type="poweredge"]',
        css: {
            // 'width': '8',
            'width': 'data(width)',
            'target-arrow-shape': 'none',
            'source-arrow-shape': 'none',
            'color': 'black',
            'source-endpoint': 'outside-to-line',
            'target-endpoint': 'outside-to-line',
        }
    },
    {
        selector: 'edge[type="reflexive-poweredge"]',
        css: {
            'width': '10',
            //'width': 'data(width)',
            'target-arrow-shape': 'none',
            'source-arrow-shape': 'none',
            'target-arrow-color': 'black',
            'curve-style': 'bezier',
            'control-point-step-size': '300px',
            'loop-sweep': '40deg',
            'loop-direction': '90deg',
            'source-endpoint': 'outside-to-line',
            'target-endpoint': 'outside-to-line',
            'source-distance-from-node': '50%',
        }
    },
    {
        selector: 'node:selected',
        css: {
            'background-color': 'white',
            'line-color': 'white',
            'target-arrow-color': 'white',
            'source-arrow-color': 'white'
        }
    },
    {
        selector: ':parent',
        style: {
            'background-opacity': 0.133,
            // 'shape': 'circle',
            'border-width': 5,
            'border-color': 'black',
        }
    },
    {
        selector: 'node[type="clique"]',
        css: {
            'border-color': 'green',
        }
    },
    {
        selector: '.top-center',
        css: {
            'text-valign': 'top',
            'text-halign': 'center',
        }
    },
  ],

  elements: {
    nodes: [
""".strip().splitlines(False)
