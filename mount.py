from cadquery import *

def circlemount():
    r = Workplane("front").circle(2.0)                       # make base
    r = r.pushPoints( [ (1.5,0),(0,1.5),(-1.5,0),(0,-1.5) ] )     # now four points are on the stack
    r = r.circle( 0.25 )                                      # circle will operate on all four points
    result = r.extrude(0.125 )                               # make prism
    return result

def solenoid():
    wp = Workplane("front") #work face
    boxh = 8.2
    boxl = 11.86
    body = wp.box(10.5, boxh, boxl) #basic shell
    bFace = body.faces(">Z")  
    nozzle = bFace.circle(1.55).extrude(5.0)  
    fFace = body.faces("<Z")
    fNozzle = fFace.circle(1.55).extrude(-5.0)
    joined = wp.union(fNozzle).union(nozzle).faces(">Z").hole(2)

    
    
    slotw = 6.18
    sloth = 2
    #create top slot
    slot = joined.faces(">X").workplane().center(boxh/2, 0)
    slotted = slot.rect(sloth*2,slotw).cutThruAll()
    #add coil
    pbFace = slotted.faces(">Z")
    coil  = pbFace.workplane(offset = -5).center(0,2).circle(4).extrude(-boxl)
  
    return coil

def export(name, shape):
    with open(name,'w') as f:
        f.write(exporters.toString(shape, 'STL'))

def main():
    export("ex.stl", solenoid())

if  __name__ == "__main__":
    main()
