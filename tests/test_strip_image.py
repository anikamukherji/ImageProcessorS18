def test_strip_image():
    """
    Tests the strip_image function
    """

    import pytest
    from Server.image_module.strip_image import strip_image

    test_data1 = 'data:image/jpeg:base64,/9j'
    test_data2 = 'data:image/jpeg:base64,dshjhurbsdb'
    test_answer1 = '/9j'
    test_answer2 = 'dshjhurbsdb'
    test_data3 = 58989

    assert test_answer1 == strip_image(test_data1, 'png').decode()
    assert test_answer2 == strip_image(test_data2, 'png').decode()

    with pytest.raises(TypeError):
        strip_image(test_data3, 'png')
