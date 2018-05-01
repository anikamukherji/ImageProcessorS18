def strip_image(base64string, file_type):
    """
        Strip the prefix of the base64string

        :param base64string: the input should be the base64 string of the image
        :raises TypeError:  if input is not a string

        :returns: base64 bytes file that is ready to be decode
        :rtype: base64 bytes
        """
    if type(base64string) is not str:
        raise TypeError('TypeError with the input，should be a string')

    index = base64string.find(',')  # Strip the string until first ','
    if file_type == "png":
        base64string = base64string[index+1:]
    if file_type == "jpg":
        base64string = base64string[index+1:]
    if file_type == "jpeg":
        base64string = base64string[index+1:]

    base64bytes = base64string.encode()     # Convert the string into bytes
    return base64bytes
