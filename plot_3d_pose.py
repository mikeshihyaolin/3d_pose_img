# plot_3d_pose.py
import h5py
path = "/Users/shihyaolin/Documents/data/scoliosis/3d_pose_res/"
filename = '20190730_1_5.walk_jpg.h5keypoints.h5'


f = h5py.File(path+filename, 'r')

# List all groups
print("Keys: %s" % f.keys())
a_group_key = list(f.keys())[0]

# Get the data
data = list(f[a_group_key])

print(len(data))

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import os


bone_list = [[0, 1], [1, 2], [2, 6], [6, 3], [3, 4], [4, 5], 
              [10, 11], [11, 12], [12, 8], [8, 13], [13, 14], [14, 15], 
              [6, 8], [8, 9]]

# H36M_NAMES[0]  = MPII[6] =  new_data[0] = 'Hip'        
# H36M_NAMES[1]  = MPII[2] =  new_data[1] = 'RHip'   
# H36M_NAMES[2]  = MPII[1] =  new_data[2] = 'RKnee'   
# H36M_NAMES[3]  = MPII[0] =  new_data[3] = 'RFoot'   
# H36M_NAMES[6]  = MPII[3] =  new_data[4] = 'LHip'    
# H36M_NAMES[7]  = MPII[4] =  new_data[5] = 'LKnee'   
# H36M_NAMES[8]  = MPII[5] =  new_data[6] = 'LFoot'   
# H36M_NAMES[12] = MPII[7] =  new_data[7] = 'Spine'        
# H36M_NAMES[13] = MPII[8] =  new_data[8] = 'Thorax' 
# H36M_NAMES[14] = MPII[-1] = new_data[9] =  'Neck/Nos
# H36M_NAMES[15] = MPII[9] =  new_data[10] = 'Head'         
# H36M_NAMES[17] = MPII[13] = new_data[11] =  'LShoulde
# H36M_NAMES[18] = MPII[11] = new_data[12] =  'LElbow' 
# H36M_NAMES[19] = MPII[15] = new_data[13] =  'LWrist' 
# H36M_NAMES[25] = MPII[12] = new_data[14] =  'RShoulde
# H36M_NAMES[26] = MPII[14] = new_data[15] =  'RElbow' 
# H36M_NAMES[27] = MPII[10] = new_data[16] =  'RWrist' 

def convert_mpii_2_human36(bone_list):

	m = {6:0, 2:1, 1:2, 0:3, 3:4, 4:5, 5:6, 7:7, 8:8, 9:10, 13:11, 11:12, 15:13, 12:14, 14:15, 10:16}  

	bone_list_tmp = []
	for item in bone_list:
		point = []
		print(item)
		if item[0]!= 9 and item[1]!= 9:
			point.append(m[item[0]])
			point.append(m[item[1]])
			bone_list_tmp.append(point)

	return bone_list_tmp

bone_list = convert_mpii_2_human36(bone_list)


bone_list = np.array(bone_list) 

 

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.view_init(azim=0, elev=0)


x = []
y = []
z = []

for i, pt in enumerate(data[0]):
	print(pt)
	x_ = [pt[0]]
	y_ = [pt[1]]
	z_ = [pt[2]]
	ax.plot(x_, y_, z_, 'bo')
	ax.text(pt[0], pt[1], pt[2], "%d"%i, fontsize=12)

	x.append(pt[0])
	y.append(pt[1])
	z.append(pt[2])


for bone in bone_list:
	print(bone)
	ax.plot([x[bone[0]], x[bone[1]]],[y[bone[0]], y[bone[1]]], [z[bone[0]], z[bone[1]]], 'b')


# ax.scatter3D(x,y,z)	
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

