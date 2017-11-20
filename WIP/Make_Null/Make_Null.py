selected_nodes = hou.selectedNodes()
for node in selected_nodes:
    parent = node.parent()
    name_node_selected = node.name()
    null = parent.createNode('null','OUT_' +
        name_node_selected)
    null.setInput(0,node)
    macolo = hou.Color((0,0.5,0))
    null.setColor(macolo)
    pos = node.position()
    null.setPosition(pos)
    null.move([0,-1])
    #flags
    null.setSelected(True,True)
    null.setDisplayFlag(True)
    null.setRenderFlag(True)