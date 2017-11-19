##Original code for Maya from Stephane
## Modified by Kishen PJ
import toolutils
pathNodeAbc = hou.ui.selectNode()
nodeAbc = hou.node(pathNodeAbc)
listofNode = []
for child in nodeAbc.allSubChildren():
    if child.type().description() == "Alembic":
        child.parm("polysoup").set(0)
        listofNode.append(child.path())
#alembic node Display off
nodeAbc.setDisplayFlag(False)
#create new geo
root = hou.node("/obj")
nodeGeo = root.createNode("geo","Alembic_Extract_Geo")
pos = nodeAbc.position()
nodeGeo.setPosition(pos)
nodeGeo.move([0,-1])
nodeGeo.children()[0].destroy()
mergeNode = nodeGeo.createNode('merge', 'mergeAll')
#objectMerge node Creation
for index in range(len(listofNode)):
    node = nodeGeo.createNode('object_merge',"Geo_extract"+ str(index +1))
    node.parm('objpath1').set(listofNode[index])
    node.parm('xformtype').set(1)
    mergeNode.setInput(index,node)
   
#display
nodeGeo.layoutChildren()
#unpack+out node
null = nodeGeo.createNode('null', 'OUT_ALEMBIC')
unpack = nodeGeo.createNode('unpack','UNPACK_ALEMBIC')
null.setInput(0,unpack)
unpack.setInput(0,mergeNode)
pos_merge = mergeNode.position()
pos_unpack = unpack.position()
unpack.setPosition(pos_merge)
null.setPosition(pos_unpack)
unpack.move([0,-1])
green = hou.Color((0,0.533,0))
null.setColor(green)
null.move([0,-2])
null.setSelected(True,True)
null.setDisplayFlag(True)
null.setRenderFlag(True)