from pyvis.network import Network

def DirectedGraph(start_node_id, label, color, physics=True):
    g = Network(height='1000px', width='100%', directed=True, notebook=False, layout="hierarchical")
    g.toggle_physics(physics)
    g.set_options("""
        options = {
            "layout": {
                "hierarchical": {
                    "enabled": true,
                    "levelSeparation": 130,
                    "nodeSpacing": 265,
                    "treeSpacing": 390,
                    "blockShifting": false,
                    "sortMethod": "directed"
                }
            },  
            "physics": {
                "hierarchicalRepulsion": {
                    "centralGravity": 0,
                    "springConstant": 0.025,
                    "damping": 0.09,
                    "avoidOverlap": 0.04
                },
                "minVelocity": 0.75,
                "solver": "hierarchicalRepulsion"
            }
        }
    """)
    g.add_node(start_node_id, label=label, color=color, x='50%', y='300px', physics=False, level=1)
    return g

def AddConnectedNode(g, prev_node_id, new_node_id, color=None, label=None, level=None):
    g.add_node(new_node_id, label=label, color=color, level=level)
    g.add_edge(prev_node_id, new_node_id, color=color)
    return

def highlightPath(g, path):
    for i in range(len(path)-1):
        g.add_edge(str(path[i]), str(path[i+1]), color='green', width=5)
    return