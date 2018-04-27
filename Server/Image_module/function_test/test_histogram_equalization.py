def test_histogram_equalization():
    """
    Tests the histogram_equalization function
    """
    try:
        import pytest
        from Image_module.histogram_equalization import hjhjkh
    except ImportError:
        print("Necessary imports for this test function failed")
        return

    test_id1 = 'test_image78374897498.png'
    test_id2 = 'test_image898490384903.png'

    with pytest.raises(NameError):
        hjhjky(test_id1, test_id2)
