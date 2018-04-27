def decode_image_string(base64string, image_name):
    """
        Decode the base64 data and return an image jpg image file

        :param base64string: the input should be the base64 bytes of the image
        :param image_name: the input should be the name string of the image
        :raises ImportError:  if import is failure

        :returns: return a jpg image
        :rtype: bytes
        """

    try:
        import base64
        import logging
    except ImportError:
        print("Necessary imports failed")

    else:
        logging.basicConfig(filename='decode_image_string.log', level=logging.DEBUG,
                            filemode='w')

    if type(base64string) is not bytes:
        logging.error('Watch out!The input should be string')
        raise TypeError('TypeError with the input')

    with open(image_name, 'wb') as image_out:
        image_out.write(base64.b64decode(base64string))
        logging.info("function run as expected")