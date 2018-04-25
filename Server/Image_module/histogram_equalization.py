def histogram_equalization(id1,id2):
    """
        Strip the prefix of the base64string

        :param id1: the input should be the name string of the image
        :param id2: the input should be the name string of the processed image
        :raises ImportError:  if input is not a string

        :returns: a python library contains the base64 string of the processed image and the image size
        :rtype: python library
        """
    try:
        import PIL
        from PIL import Image
        import numpy as np
        from skimage import exposure
        import os
        from skimage import util
        import logging
        import uuid
        from Image_module.encode_image import encode_image
    except ImportError:
        print("Necessary imports failed")
    else:
        logging.basicConfig(filename='histogram_equalization.log',
                            level=logging.DEBUG, filemode='w')

    try:
        i = np.asarray(PIL.Image.open(id1))  # convert the image into the numpy array
    except NameError:
        logging.debug("The image file does not exist")
        raise NameError


    try:
        assert len(i.shape) == 3            # Ensure the shape of the image array is right
    except AssertionError:
        logging.debug("The shape of image array is 3 layers")
        print("image numpy array is not in the right shape")

    i_histogram1 = exposure.equalize_hist(i[:, :, 0])   #Conduct the histogram equalization for each layer of the image
    i_histogram2 = exposure.equalize_hist(i[:, :, 1])
    i_histogram3 = exposure.equalize_hist(i[:, :, 2])
    i_histogram = np.dstack((i_histogram1, i_histogram2, i_histogram3))
    ima = Image.fromarray(np.uint8(i_histogram * 255))  #Rescale the numpy array to convert the data type to uint8
    (w , h) = ima.size                                  #Get the size of the image

    ima.save(id2)                       #save the processed image as a jpg file on the VCM
    a2 = str(encode_image(id2))         #Generate the base64 string for the processed image

    processed_image = {'base64': a2, 'image_size': (w , h)}

    return processed_image
