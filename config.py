"""
NETWORK CONFIG FILE

"""
# min-batch size
size_batch=49	

# size of hidden vector z
num_z_channels=50 	

# width and height of input image
size_image = 96

# path to save checkpoints, samples, and summary
save_dir='./save'  	

#Path where the training data is

path = "./data/affectnet/"

#path where the validation data is

validation_path = './data/Validation/'

# value range of single pixels in an input image
image_value_range = (-1, 1) 
