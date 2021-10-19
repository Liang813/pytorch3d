
from pytorch3d.loss import mesh_laplacian_smoothing
from pytorch3d.utils import ico_sphere

if __name__ == '__main__':
    for i in range(5):
        print(mesh_laplacian_smoothing(ico_sphere(i), 'cotcurv'))

