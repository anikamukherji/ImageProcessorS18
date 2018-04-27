def histogram_equalization(id1):
    """
        Strip the prefix of the base64string

        :param id1: the input should be the base64 string of the image
        :raises ImportError:  if input is not a string

        :returns: base64 bytes file that is ready to be decode
        :rtype: base64 bytes
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
        from encode_image import encode_image
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

    os.remove(id1)                          # Remove image from the VCM

    id2 = str(uuid.uuid4())
    suffix = '.jpg'
    id2 = id2 + suffix

    try:
        assert len(i.shape) == 3
    except AssertionError:
        print("image numpy array is not in the right shape")

    i_histogram1 = exposure.equalize_hist(i[:, :, 0])
    i_histogram2 = exposure.equalize_hist(i[:, :, 1])
    i_histogram3 = exposure.equalize_hist(i[:, :, 2])
    i_histogram = np.dstack((i_histogram1, i_histogram2, i_histogram3))
    ima = Image.fromarray(np.uint8(i_histogram * 255))

    ima.save(id2)
    a2 = encode_image(id2)               # Remove image from the VCM
    os.remove(id2)
    return a2
