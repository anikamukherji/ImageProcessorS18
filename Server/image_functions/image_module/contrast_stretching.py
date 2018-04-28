def contrast_stretching(id1, id2):
    """
        Process the input image with contrast_stretching
        and check the image size

        :param id1: the input should be the name string of the image
        :param id2: the input should be the name string of the processed image
        :raises ImportError:  if input is not a string
        :raises NameError:: if the id1 image file does not exist
        :raises AssertionError: if the image array does not contain
                three layers

        :returns: a python dictionary contains the base64 string
                  of the processed image and the image size
        :rtype: python dictionary
        """
    try:
        import PIL
        from PIL import Image
        import numpy as np
        from skimage import exposure
        import logging
        from image_module.encode_image import encode_image
    except ImportError:
        print("Necessary imports failed")
    else:
        logging.basicConfig(filename='histogram_equalization.log',
                            level=logging.DEBUG, filemode='w')

    try:
        i = np.asarray(PIL.Image.open(id1))  # convert into numpy array
    except FileNotFoundError:
        logging.debug("The image file does not exist")
        raise FileNotFoundError

    try:
        assert len(i.shape) == 3   # Ensure the shape is right
    except AssertionError:
        logging.debug("The shape of image array is not 3 layers")
        print("image numpy array is not in the right shape")

    p2, p98 = np.percentile(i, (10, 90))
    i_contrast = exposure.rescale_intensity(i, in_range=(p2, p98))
    ima = Image.fromarray(i_contrast)
    (w, h) = ima.size                     # Get the size of the image

    ima.save(id2)               # Save the processed image
    a2 = str(encode_image(id2))  # Generate the base64 string

    processed_image = {'base64': a2, 'image_size': (w, h)}
    logging.info("function run as expected")

    return processed_image
