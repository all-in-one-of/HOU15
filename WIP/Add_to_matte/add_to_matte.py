import hou

selection = hou.selectedNodes()
names = [n.name() for n in selection]
my_list = ""
if len(selection) < 1 :
    my_list = "nothing selected, please select at least one object"
else:
    a=1
    for sel in selection:
        my_list = my_list + "\n" + "selected object " + str(a) + ":" + sel.name()
        a=a+1        
hou.ui.displayMessage(my_list, buttons=('OK',))
length = len(selection)
print "Number of nodes selected: " + str(length)
paths = [n.path() for n in hou.node('/out').allSubChildren()
         if n.type() == hou.nodeType('Driver/ifd')]
selected = hou.ui.selectFromTree(choices=paths)

mantras = [hou.node(path) for path in selected]
for m in mantras:
    m.parm('matte_objects').set(' '.join(n.name() for n in hou.selectedNodes())) # CHANGE PARAMETER NAME AS REQURIED
    print ("Selected mantra nodes : ") + m.name()
    new_name=' '.join(names)
hou.ui.displayMessage("( "+ (new_name) + " )  - added to selected mantra(s) matte objects.", buttons=('*Claps*',))
    