import maya.api.OpenMaya as om2
##works on selection in maya scene
selectList=om2.MGlobal.getActiveSelectionList()
dagPath=om2.MDagPath()
if (selectList.length()<1):
    raise Exception('select atleast one object')
else:
    dagPath=selectList.getDagPath(0)
    print dagPath.fullPathName()
