import numpy as np
import sys

def get_heatmap_data(num_images):

    num_images = int(num_images)
    #np.random.seed(int(rand_seed))

    img_size = 448
    #tile_size = 20
    #noise_std = 0.02

    data = np.zeros((num_images, 81, img_size, img_size))
    labels = np.zeros((num_images, 1, img_size, img_size)).astype(int)
    #data = np.empty( shape=(num_images,81,img_size, img_size) )
    #labels = np.empty(shape=(num_images, 81, img_size, img_size)).astype(int)
    for t in range(num_images):
        print t
        k=0
        file_name= "heatmaps/frame%04d.txt" %(t)
        label_name="labels/frame%04d.txt" %(t)
        f = open(file_name, 'r')
        m = open(label_name, 'r')
        l = np.zeros(shape=(81, img_size, img_size))
        l_labels = np.empty(shape=(1, img_size, img_size))
        for line1,line2 in zip( f,m):
            row_list=line1.split(" ")
            #print row_list
            row_list_labels= line2.split(" ")
            l[:,((k/448)),(k%448)]=row_list[0:81]
            ind, maxv = max(row_list_labels)
            if(maxv == 0):
                ind = 0
            l_labels[:,(k/448),k%448]=ind
            k = k + 1
        f.close()
        m.close()
        data[t, :, :, :] = l
        labels[t, 0, :, :] =l_labels
        


        #fg_color = np.random.rand(3)
        #bg_color = np.random.rand(3)

        #rand_loc_row = int(np.random.rand(1) * (img_size - tile_size))\
        #    + tile_size / 2
        #rand_loc_col = int(np.random.rand(1) * (img_size - tile_size))\
        #    + tile_size / 2

        #bg_image = np.tile(bg_color, [img_size, img_size, 1])
        #label_image = np.zeros((img_size, img_size))

        #tile_image = np.tile(fg_color, [tile_size, tile_size, 1])

        #image = bg_image
        #image[rand_loc_row - tile_size / 2: rand_loc_row + tile_size / 2,
        #      rand_loc_col - tile_size / 2: rand_loc_col + tile_size / 2, :]\
        #    = tile_image

       # label_image[rand_loc_row - tile_size / 2: rand_loc_row + tile_size / 2,
        #            rand_loc_col - tile_size / 2: rand_loc_col + tile_size / 2]\
         #   = 1

       # noise_image = image + np.random.normal(0, noise_std, image.shape)
        #data[t, :, :, :] = noise_image.transpose((2, 0, 1))
        #labels[t, 0, :, :] = label_image.astype(int)

    return [data, labels]

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: ' + sys.argv[0] + ' <num_images> <rand_seed>')
    else:
        get_heatmap_data(sys.argv[1])
