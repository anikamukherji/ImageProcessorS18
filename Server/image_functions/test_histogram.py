def test_histogram():
    """
    Tests the histogram function
    """

    import pytest
    from image_module.image_histogram import histogram

    test_data1 = 'test_image384935893.tiff'
    test_data2 = 'test_image8439843948390.jpg'

    with pytest.raises(TypeError):
        histogram(test_data1)

    with pytest.raises(TypeError):
        histogram(test_data2)
