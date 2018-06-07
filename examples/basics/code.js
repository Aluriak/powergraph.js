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
      selector: '$node > node',
      css: {
        'padding-top': '10px',
        'padding-left': '10px',
        'padding-bottom': '10px',
        'padding-right': '10px',
        'text-valign': 'top',
        'text-halign': 'center',
        'background-color': '#eee'
      }
    },
    {
      selector: 'edge',
      css: {
        'width': '1',
        'target-arrow-shape': 'none',
        'source-arrow-shape': 'none',
        'target-arrow-color': 'black',
      }
    },
    // {
      // selector: 'edge[type="edge"]',
      // css: {
        // 'width': '1',
        // 'target-arrow-shape': 'none',
        // 'source-arrow-shape': 'none',
        // 'target-arrow-color': 'black',
      // }
    // },
    {
      selector: 'edge[type="poweredge"]',
      css: {
        'width': '8',
        'target-arrow-shape': 'none',
        'source-arrow-shape': 'none',
        'target-arrow-color': 'black',
      }
    },
    {
      selector: ':selected',
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
      }
    },
  ],

  elements: {
    nodes: [
      { data: { id: 'g' } },
      { data: { id: 'a', parent: 'b' } },
      { data: { id: 'b', parent: 'g' } },
      { data: { id: 'c', parent: 'b' } },
      { data: { id: 'd' } },
      { data: { id: 'e', parent: 'g' } },
      { data: { id: 'f', parent: 'e' } }
    ],
    edges: [
      { data: { id: 'ac', source: 'a', target: 'c' } },
      { data: { id: 'ad', source: 'a', target: 'd', type: 'edge' } },
      { data: { id: 'eb', source: 'e', target: 'b', type: 'poweredge' } },
    ]
  },

  layout: {
    name: 'cose-bilkent',
    // padding: 5
  }
});

