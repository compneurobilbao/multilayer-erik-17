# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary test file.
"""

from nilearn.image import resample_img
from nilearn.image import math_img

import nibabel as nib
import numpy as np
import os
from os.path import join as opj

cwd = os.getcwd()

path_file_1 = opj(cwd, 'data', 'test_1.nii.gz')
path_file_2 = opj(cwd, 'data', 'test_2.nii.gz')

img1_data = nib.load(path_file_1).get_data()
img2_data = nib.load(path_file_2).get_data()

## binarize
#img1_data[np.nonzero(img1_data)] = 1
#img2_data[np.nonzero(img2_data)] = 1

# binarize
img1_data[img1_data > 0.5] = 1
img1_data[img1_data <= 0.5] = 0

img2_data[img2_data >= -0.5] = 0
img2_data[img2_data < -0.5] = 1



# count img1
img1_count = np.count_nonzero(img1_data)


logical_and = np.logical_and(np.ndarray.flatten(img1_data),
                             np.ndarray.flatten(img2_data))

count_overlap = np.count_nonzero(logical_and)

overlap_ratio_perc = count_overlap/img1_count*100