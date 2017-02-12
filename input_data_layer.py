#!/usr/bin/env python

import io
import numpy as np
from config import *
from get_heatmap_data import get_heatmap_data
import cv2

class InputRead(caffe.Layer):

    def initialize(self):
        self.batch_size = 1
        self.channels = 81
        self.height = 448
        self.width = 448
        self.data_type = 'TRAIN'

        self.num_tops = 2
        self.top_names = ['data', 'label']
        self.top_channels = [81, 1]

        self.data = None
        self.label = None

        self.idx = 0
        self.num_images = 0

    def setup(self, bottom, top):

        params = self.param_str
        if len(params) < 1:
            params = ['TRAIN']
            print("Using standard initialization of params:", params)

        self.initialize()
        self.data_type = str(params)

        [self.data, self.label] = get_heatmap_data(1)
        print "here"
                                                
        self.num_images = NUM_DATA[self.data_type]
#        print (self.data[1,:,:,:]).shape
#        cv2.imshow("sss", (self.data[1,:,:,:]).T);
#        cv2.waitKey(0);
        print 'Outputs:', self.top_names
        if len(top) != len(self.top_names):
            raise Exception('Incorrect number of outputs (expected %d, got %d)' %
                            (len(self.top_names), len(top)))

    def reshape(self, bottom, top):
        for top_index, name in enumerate(self.top_names):
            shape = (self.batch_size, self.top_channels[top_index],
                    self.height, self.width)
            top[top_index].reshape(*shape)
        pass


    def forward(self, bottom, top):

        top[0].data[...] = self.data[self.idx : self.idx + self.batch_size, :, :, :]
        top[1].data[...] = self.label[self.idx : self.idx + self.batch_size, :, :, :]

        self.idx += self.batch_size
        if self.idx >= self.num_images:
            self.idx = self.idx - self.num_images

        pass


    def backward(self, top, propagate_down, bottom):
        pass
