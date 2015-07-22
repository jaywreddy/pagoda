from cadquery import *

def circlemount():
    r = Workplane("front").circle(2.0)                       # make base
    r = r.pushPoints( [ (1.5,0),(0,1.5),(-1.5,0),(0,-1.5) ] )     # now four points are on the stack
    r = r.circle( 0.25 )                                      # circle will operate on all four points
    result = r.extrude(0.125 )                               # make prism
    return result

def solenoid():
    wp = Workplane("front") #work face
    body = wp.box(2.0, 2.0, 8)
    bFace = body.faces(">Z")      

    nozzle = wp.circle(2.0).extrude(2) #inner  
    
   # body =  

def export(name, shape):
    with open(name,'w') as f:
        f.write(exporters.toString(shape, 'STL'))

def main():
    export("ex.stl", circlemount())

if  __name__ == "__main__":
    main()
