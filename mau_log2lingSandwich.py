#--------------------------------------------------
# mau_log2lin_sandwich.py
# version: 0.0.1
# last updated: 22.01.22 (DD.MM.YY)
#--------------------------------------------------

import nuke
import nukescripts

def log2linSelected():
    sel = nuke.selectedNode()
    sel_x = sel['xpos'].value()
    sel_y = sel['ypos'].value()
    #print sel_y
    
    lin = nuke.nodes.Log2Lin()
    lin['operation'].setValue(1)
    lin['xpos'].setValue(sel_x)
    lin['ypos'].setValue(sel_y-50)
    
    sel.setInput(0,lin)
    
    sel_name = sel.name()
    nukescripts.clear_selection_recursive()
    nuke.toNode(sel_name).setSelected(True)
    sel = nuke.selectedNode()
    sel_y = sel['ypos'].value()
    #print sel_y
    
    log = nuke.nodes.Log2Lin()
    
    log['operation'].setValue(0)
    log['xpos'].setValue(sel_x)
    log['ypos'].setValue(sel_y+50)
    log.setInput(0,sel)
    nukescripts.clear_selection_recursive()


nuke.menu('Nodes').addCommand('Color/Log2Lin_Sandwich','log2linsandwich.log2linSelected()','ctrl+shift+l',icon='Log2Lin.png')
