def download_image(id2):
    """
        store the input png file in .jpg and .tiff formats
        and output the base64 strings of these two formats

        :param id2: the input should be the name string of the processed image
        :raises ImportError:  if import is failure
        :raises TypeError: if the input image file is not .png


        :returns: a python dictionary contains the base64 string
                  of the processed image in .jpg and .tiff
        :rtype: python dictionary
    """
    try:
        import PIL
        from PIL import Image
        import logging
        import os
        from Server.image_module.encode_image \
            import encode_image
    except ImportError:
        print("Necessary imports failed")
    else:
        logging.basicConfig(filename='download_image.log', level=logging.DEBUG,
                            filemode='w')

    if id2.find('png') == -1:  # Ensure that the input image is a png file
        logging.error('This function does not support this format')
        raise TypeError("Input image is of the wrong format")

    index = id2.find('.png')  # Strip off the png suffix
    id2_uuid = id2[0: index]
    id2_jpg = id2_uuid + '.jpg'
    id2_tiff = id2_uuid + '.tiff'

    im = Image.open(id2)
    rgb_im = im.convert('RGB')
    rgb_im.save(id2_jpg)
    rgb_im.save(id2_tiff)

    a2_jpg = str(encode_image(id2_jpg))
    a2_tiff = str(encode_image(id2_tiff))

    os.remove(id2_jpg)  # Remove the .jpg file from VCM
    os.remove(id2_tiff)  # Remove the .tiff file from VCM

    images_formats = {'base64_jpg': a2_jpg, 'base64_tiff': a2_tiff}
    logging.info("Returning dictionary with .jpg image base64 string"
                 " and with .tiff image base64 string")

    return images_formats
