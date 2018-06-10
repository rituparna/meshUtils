import maya.api.OpenMaya as om2

selectList=om2.MGlobal.getActiveSelectionList()
dagPath=om2.MDagPath()
dagPath=selectList.getDagPath(0)
print dagPath.fullPathName()
