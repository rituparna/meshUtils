import maya.api.OpenMaya as om2
##works on selection in maya scene
selectList=om2.MGlobal.getActiveSelectionList()
dagPath=om2.MDagPath()
if (selectList.length()<1):
    raise Exception('select atleast one object')
else:
    dagPath=selectList.getDagPath(0)
    print dagPath.fullPathName()
    
meshFn=om2.MFnMesh(dagPath)
mItVert=om2.MItMeshVertex(dagPath)
positions=om2.MPointArray()
locList=[]
while not mItVert.isDone():
    index=mItVert.index()
    pos=mItVert.position(om2.MSpace.kWorld)
  
    loc=mc.spaceLocator(n='loc_%02d'%index)[0]
    mc.xform(loc,ws=True,t=(pos.x,pos.y,pos.z))
    locList.append(loc)
    mItVert.next()
