def test_decode_image():
    """
    Tests the decode_image function
    """

    import pytest
    from image_module.decode_image import decode_image
    import base64

    base64bytes1 = 'shjhjhds'
    base64bytes2 = base64bytes1.encode()
    image_name = 'test1.jpg'
    image_name2 = 5

    with pytest.raises(TypeError):
        decode_image(base64bytes1, image_name)
    with pytest.raises(TypeError):
        decode_image(base64bytes2, image_name2)
