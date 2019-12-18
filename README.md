# 3D human pose Inference from RGB images 
**Code Author: Shih-Yao (Mike) Lin**

![](figs/demo.gif)

## Features
+ Convert a video to images
+ Extract 2D human pose from 2D RGB images by using Openpose 
+ Crop image and set people in the center of the new image 

## Dependencies
+ python3, glob2, opencv-python

## Installation

* Clone this repo

```bash
git https://github.com/mikeshihyaolin/3d_body_pose_rgb_img.git
```

## Preparation
+ preprocess the data by using my [tools](https://github.com/mikeshihyaolin/2d_pose_openpose)
+ make a folder for repacing the pretrained [pose model](https://drive.google.com/file/d/1_2CCb_qsA1egT5c2s0ABuW3rQCDOLvPq/view) and download it
```
mkdir model
```

## Usages
1. generate run script
```
python generate_run_scripts.py -s [source_folder] -t [target_folder]
```
2. run script
```
sh ./run_script.sh
```

*The 3D human pose inference is based on the approach by [Zhou et al. (ICCV’17)](https://github.com/xingyizhou/pytorch-pose-hg-3d)