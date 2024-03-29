from geomdl import BSpline
from geomdl import multi
from geomdl import knotvector
from geomdl import CPGen
# Create the curve instance #1
crv1 = BSpline.Curve()
# Set degree
crv1.degree = 2
# Set control points
crv1.ctrlpts = [[22, 7, 22], [5, 12, 0], [3, 1, 0]]
# Generate a uniform knot vector
crv1.knotvector = knotvector.generate(crv1.degree, crv1.ctrlpts_size)

# Create the curve instance #2
crv2 = BSpline.Curve()
# Set degree
crv2.degree = 3
# Set control points
crv2.ctrlpts = [[1, 0, 0], [1, 21, 0], [2, 1, 0], [1, 1, 0]]
# Generate a uniform knot vector
crv2.knotvector = knotvector.generate(crv2.degree, crv2.ctrlpts_size)




# Create a curve container
mcrv = multi.CurveContainer(crv1, crv2)

# Import Matplotlib visualization module
from geomdl.visualization import VisMPL
# Set the visualization component of the curve container
mcrv.vis = VisMPL.VisCurve3D()
# Plot the curves in the curve container
mcrv.render()