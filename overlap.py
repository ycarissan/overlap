import numpy as np
import geode
import pyvista as pv
from pyvista import examples
from matplotlib.colors import ListedColormap


points=[]
data=[]
nalpha=20
nr = 7
rmax = 20
if False:
    for theta in np.linspace(0, np.pi, nalpha):
        for phi in np.linspace(0, 2*np.pi, 2 * nalpha):
            for r in np.linspace(0, 5, nr):
                x = r * np.sin(theta) * np.cos(phi)
                y = r * np.sin(theta) * np.sin(phi)
                z = r * np.cos(theta)
                points.append([x, y, z])
                data.append(np.exp(-r))
else:
    geode_pts = geode.get_geode_points(depth=5)
    points = []
    data = []
    dr = rmax/nr
    for r in np.linspace(0, 5, nr):
        for pt in geode_pts:
            r_ = r + dr * (np.random.random() - 0.5)
            points.append(pt * r_)
            theta = np.abs(np.arccos(pt[2] / r_))
            data.append(r_ * np.cos(theta) * np.exp(-r_))

points = pv.pyvista_ndarray(points)
datac = pv.pyvista_ndarray(data)

point_cloud = pv.PolyData(points)
point_cloud["Psi"] = datac

mapping = np.linspace(datac.min(), datac.max(), 256)
newcolors = np.empty((256, 4))
newcolors[mapping >= 0.9*256] = np.array([256/256, 0/256, 0/256, 1])
newcolors[mapping <= 0.8*256] = np.array([256/256, 0/256, 0/256, .9])
newcolors[mapping <= 0.7*256] = np.array([256/256, 0/256, 0/256, .8])
newcolors[mapping <= 0.6*256] = np.array([256/256, 0/256, 0/256, .7])
newcolors[mapping <= 0.5*256] = np.array([256/256, 0/256, 0/256, .6])
newcolors[mapping <= 0.4*256] = np.array([256/256, 0/256, 0/256, .5])
newcolors[mapping <= 0.3*256] = np.array([256/256, 0/256, 0/256, .4])
newcolors[mapping <= 0.2*256] = np.array([256/256, 0/256, 0/256, .3])
newcolors[mapping <= 0.1*256] = np.array([256/256, 0/256, 0/256, .2])
my_colormap = ListedColormap(newcolors)




point_cloud.plot(render_points_as_spheres=False, cmap = my_colormap)

