from cadquery import *
def circlemount():
    r = Workplane("front").circle(2.0)                       # make base
    r = r.pushPoints( [ (1.5,0),(0,1.5),(-1.5,0),(0,-1.5) ] )     # now four points are on the stack
    r = r.circle( 0.25 )                                      # circle will operate on all four points
    result = r.extrude(0.125 )                               # make prism
    return result

with open('ex.stl','w') as f:
    f.write(exporters.toString(circlemount(),'STL'))

