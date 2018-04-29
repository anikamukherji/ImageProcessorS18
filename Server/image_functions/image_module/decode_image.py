def decode_image(base64bytes, image_name):
    """
        Decode the base64 data and return an image jpg image file

        :param base64bytes: the input should be the base64 bytes of the image
        :param image_name: the input should be the name string of the image
        :raises ImportError:  if import is failure
        :raises TypeError: if the first input is not in bytes format
        :raises TypeError: if the second input is not a string

        :returns: return a png image
        :rtype: bytes
        """

    try:
        import base64
        import logging
    except ImportError:
        print("Necessary imports failed")
        return

    logging.basicConfig(filename='decode_image.log',
                        level=logging.DEBUG, filemode='w')

    if type(base64bytes) is not bytes:
        logging.error('Watch out!The input should in bytes')
        raise TypeError('TypeError with the input')

    if type(image_name) is not str:
        logging.error('Watch out!The input should be string')
        raise TypeError('TypeError with the input')

    with open(image_name, 'wb') as image_out:
        image_out.write(base64.b64decode(base64bytes))
        logging.info("function run as expected")
