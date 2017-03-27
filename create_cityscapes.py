import os
import glob
import argparse
import numpy as np
from scipy import misc

dir_name = 'cityscapes-comparison'
# backward  bigan  cogan  content_gan  forward  l1_gan  no_cycle  no_gan  pix2pix

def comparison():

  methods = ['bigan', 'cogan', 'cycle', 'pix2pix']
  subdirs = ['photo2label', 'label2photo']

  for filename in glob.glob('images/%s/%s/gt/*.jpg' % (dir_name,subdirs[0])):
    nameonly = os.path.basename(filename)
    
    direction = 0
    subdir = subdirs[direction]
    theotherdir = subdirs[1-direction]
    
    print(("| ![]({{site.baseurl}}/images/%s/%s/%s/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/%s) |") %
          (dir_name,theotherdir,'gt',nameonly,
           dir_name,subdir,methods[0],nameonly,
           dir_name,subdir,methods[1],nameonly,
           dir_name,subdir,methods[2],nameonly,
           dir_name,subdir,methods[3],nameonly,
           dir_name,subdir,'gt',nameonly,
         ))
    
    direction = 1
    subdir = subdirs[direction]
    theotherdir = subdirs[1-direction]
    
    print(("| ![]({{site.baseurl}}/images/%s/%s/%s/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/%s) " +
           "| ![]({{site.baseurl}}/images/%s/%s/%s/%s) |") %
          (dir_name,theotherdir,'gt',nameonly,
           dir_name,subdir,methods[0],nameonly,
           dir_name,subdir,methods[1],nameonly,
           dir_name,subdir,methods[2],nameonly,
           dir_name,subdir,methods[3],nameonly,
           dir_name,subdir,'gt',nameonly,
         ))

        
