#generate_run_scripts
#author: Shih-Yao (Mike) Lin
#email: mike.lin@ieee.org
#date: 2019-12-18
#usage python generate_run_scripts.py -s ~/Documents/data/scoliosis/cropped/ -t ~/Documents/data/scoliosis/3d_pose_res/

import glob
import argparse
import os, sys
from os import listdir, makedirs
import shutil

def reset(reset_path):
    path = reset_path
    if os.path.isdir(path):
        shutil.rmtree(path)
        print("remove existing "+path)
        makedirs(path)
        print("create folder: "+path)
    else:
        makedirs(path)
        print("create foder: "+path)


def generate_scripts(source_folder, target_folder):
	
	reset(target_folder)

	os.chdir(source_folder)
	all_subdirs = [d for d in os.listdir('.') if os.path.isdir(d)]
	print(all_subdirs)

	f= open("../run_scripts.sh","w")

	for folder in all_subdirs:
		cmd = "python ./src/demo.py --demo "+source_folder+folder+" --output_path "+target_folder+"/"+folder+"  --gpus -1  --load_model ./models/fusion_3d_var.pth "
		f.write(cmd+"\n")

	f.close()
	
if __name__=="__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument("-s", "--source_folder", type=str)
	parser.add_argument("-t", "--target_folder", type=str)

	args = parser.parse_args()

	generate_scripts(args.source_folder, args.target_folder)