def strip_image(base64string):
    """
        Strip the prefix of the base64string

        :param base64string: the input should be the base64 string of the image
        :raises ImportError:  if input is not a string

        :returns: base64 bytes file that is ready to be decode
        :rtype: base64 bytes
        """
    if type(base64string) is not str:
        raise TypeError('TypeError with the input')

    index = base64string.find('/')          #Strip the base64 string until first '/'
    base64string = base64string[index:]
    base64bytes = base64string.encode()     #Convert the string into bytes
    return base64bytes
