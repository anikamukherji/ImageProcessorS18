def histogram(id1):
    """
        Plot the histogram for particular image and convert
        that image into base64 data

        :param id1: the input should be the name string of the image
        :raises ImportError:  if import is failure
        :raises TypeError: if the input image file is not .png

        :returns: return a base64 string of the histogram image
        :rtype: base64 string
        """

    try:
        import matplotlib.pyplot as plt
        import matplotlib.image as mpimg
        import numpy as np
        import logging
        import os
        from image_module.encode_image import encode_image
    except ImportError:
        print("Necessary imports failed")
        return

    logging.basicConfig(filename='encode_image.log', level=logging.DEBUG,
                        filemode='w')

    if id1.find('png') == -1:       # Ensure that the input image is a png file
        logging.error('This histogram function does not support this format')
        raise TypeError('TypeError with the input image')

    prefix = 'histogram_'
    id1_histogram = prefix + id1

    img = mpimg.imread(id1)
    lum_img = img[:, :, 0]
    plt.hist(lum_img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')
    plt.xlabel("pixel intensity")
    plt.ylabel("number of pixel")
    plt.savefig(id1_histogram)    # Store the histogram

    a1_histogram = str(encode_image(id1_histogram))

    os.remove(id1_histogram)

    logging.info("function run as expected")

    return a1_histogram
