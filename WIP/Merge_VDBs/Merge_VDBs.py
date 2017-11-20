selected_nodes = hou.selectedNodes()
vdbcombines = []

for x, node in enumerate(selected_nodes):
    if x < len(selected_nodes)-1:
        vdbcombine = node.createOutputNode('vdbcombine')
        vdbcombine.setNextInput(selected_nodes[x+1])
        vdbcombine.setParms({'operation':'add'})
        vdbcombines.append(vdbcombine)

for x, vdbcombine in enumerate(vdbcombines):
    if x < len(vdbcombines)-1:
        vdbcombine.setInput(1, vdbcombines[x+1])