def encode_image(image_name):
    """
        Encode the image data into the base64 data

        :param image_name: the input should be the name string of the image
        :raises ImportError:  if import is failure
        :raises TypeError: if the input is not a string

        :returns: return a base64 bytes file
        :rtype: base64 bytes
        """

    try:
        import base64
        import logging
    except ImportError as e:
        print("Necessary imports failed: {}".format(e))
        return

    logging.basicConfig(filename='encode_image.log', level=logging.DEBUG,
                        filemode='w')

    if type(image_name) is not str:
        logging.error('Watch out!The input should be string')
        raise TypeError('TypeError with the input')

    with open(image_name, 'rb') as image_file:
        image_string = base64.b64encode(image_file.read())
        print(image_string[:100])
        logging.info("Image file {} being read".format(image_name))

    return image_string
