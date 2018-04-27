def test_histogram():
    """
    Tests the histogram function
    """
    try:
        import pytest
        from Image_module.histogram import histogram
    except ImportError:
        print("Necessary imports for this test function failed")
        return

    test_data1 = 'test_image384935893.tiff'
    test_data2 = 'test_image8439843948390.jpg'

    with pytest.raises(TypeError):
        histogram(test_data1)

    with pytest.raises(TypeError):
        histogram(test_data2)
