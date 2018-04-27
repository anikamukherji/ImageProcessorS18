def test_contrast_stretching():
    """
    Tests the contrast_stretching function
    """
    try:
        import pytest
        from Image_module.contrast_stretching import contrast_stretching
    except ImportError:
        print("Necessary imports for this test function failed")
        return

    test_id1 = 'test_image78374897498.png'
    test_id2 = 'test_image898490384903.png'

    with pytest.raises(NameError):
        contrast_stretching(test_id1, test_id2)
