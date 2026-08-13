import numpy as np
import matplotlib.pyplot as plt

# --- A tiny pinhole camera simulator ---
# Camera sits at the origin, looking down the +Z axis (into the scene).
# The image plane is at focal distance f.

f = 2.0   # focal length (distance from pinhole to image plane)

def project(point3d):
    """Take a 3D point (X, Y, Z) and return where it lands on the 2D image plane."""
    X, Y, Z = point3d
    # similar triangles: image coord = f * (world coord / depth)
    x = f * (X / Z)
    y = f * (Y / Z)
    return (x, y)

# Define a square in 3D space (4 corners), all at the SAME depth Z=5
square_near = [(-1, -1, 5), (1, -1, 5), (1, 1, 5), (-1, 1, 5)]
# The SAME square, but pushed FAR away, Z=10
z=10000
square_far  = [(-1, -1, z), (1, -1, z), (1, 1, z), (-1, 1, z)]

# Project both onto the 2D image plane
near_2d = [project(p) for p in square_near]
far_2d  = [project(p) for p in square_far]

# Plot what the "camera" sees
def draw(points, color, label):
    pts = points + [points[0]]   # close the loop
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    plt.plot(xs, ys, color=color, label=label, marker='o')

draw(near_2d, 'blue', 'square at Z=5 (near)')
draw(far_2d,  'red',  'square at Z=10 (far)')
plt.gca().set_aspect('equal'); plt.legend(); plt.title("Pinhole projection: same square, two depths")
plt.grid(True); plt.show()
print(project((1, 1, 5)))     # a point at X=1, Y=1, depth 5
print(project((2, 2, 10)))    # DIFFERENT 3D point: twice as far, twice as big
print(project((4, 4, 20)))    # different again: even farther, even bigger

fx, fy = 800, 800      # focal lengths in pixels
cx, cy = 960, 540      # principal point (image center of a 1920x1080 frame)

K = np.array([[fx,  0, cx],
              [ 0, fy, cy],
              [ 0,  0,  1]])

def project_K(point3d):
    X, Y, Z = point3d
    homogeneous = K @ np.array([X, Y, Z])   # matrix multiply -> (a, b, w)
    pixel = homogeneous / homogeneous[2]    # divide by last coord (the Z slot)
    return pixel[:2]                        # drop the trailing 1, keep (x, y)

print(project_K((1, 1, 5)))    # a point 5 units deep
print(project_K((2, 2, 10)))   # twice as far, twice as big -> SAME pixel again



# Intrinsics (from before)
K = np.array([[800,   0, 960],
              [  0, 800, 540],
              [  0,   0,   1]])

# Extrinsics: camera pushed back 5 units along Z, no rotation (identity R)
R = np.eye(3)                       # no rotation -> camera axes aligned with world
t = np.array([[0], [0], [5]])       # camera origin shifted; world points appear +5 deeper
Rt = np.hstack([R, t])              # 3x4  [R | t]

def project_world(point3d):
    world_h = np.array([point3d[0], point3d[1], point3d[2], 1])  # homogeneous (X,Y,Z,1)
    cam = Rt @ world_h              # STEP 1: world -> camera frame
    pix = K @ cam                   # STEP 2: camera frame -> pixel (still homogeneous)
    return (pix / pix[2])[:2]       # divide by last coord -> real (x, y)

print(project_world((0, 0, 0)))    # a world point at the origin
print(project_world((1, 1, 0)))    # off to the side