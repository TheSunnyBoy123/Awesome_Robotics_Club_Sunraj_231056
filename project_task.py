def dist(a, b):
  return ((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2) + ((a[2] - b[2]) ** 2)

def backward(joints, lengths, target):
  n = len(joints)
  for i in range(n - 2, -1, -1):  
    diff = target - joints[i + 1]
    limit = lengths[i]
    if dist(diff, (0, 0, 0)) > limit**2:  
      diff = diff * (limit / mag(diff))
    joints[i] = joints[i + 1] - diff
  return joints

def forward(joints, lengths, origin):
  n = len(joints)
  for i in range(1, n):
    diff = joints[i - 1] - joints[i]
    limit = lengths[i - 1]
    if dist(diff, (0, 0, 0)) > limit**2:
      diff = diff * (limit / mag(diff)) 
    joints[i] = joints[i - 1] + diff
  return joints

def mag(vec):
  return (vec[0] ** 2 + vec[1] ** 2 + vec[2] ** 2) ** 0.5

lengths = [23, 15, 7]
tolerance = 0.01
joints = []
for _ in range(4):
    x,y,z = input(f"Position of joint (x, y, z) ").split()
    joints.append([float(x), float(y), float(z)])

x,y,z = input(f"Position of target (x, y, z) ").split()
target = [float(x), float(y), float(z)]

origin = joints[0]
totalLength = sum(lengths)

if totalLength < dist(origin, target):
    print("Target unreachable")
else:
    while joints[0] != origin and dist(target, joints[-1]) < tolerance:
        joints = backward(joints, lengths, origin)
        joints = forward(joints, lengths, origin)
  
print(joints)