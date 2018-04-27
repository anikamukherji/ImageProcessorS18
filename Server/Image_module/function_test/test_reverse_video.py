def test_reverse_video():
    """
    Tests the reverse_video function
    """
    try:
        import pytest
        from Image_module.reverse_video import reverse_video
    except ImportError:
        print("Necessary imports for this test function failed")
        return

    test_id1 = 'test_image78374897498.png'
    test_id2 = 'test_image898490384903.png'

    with pytest.raises(NameError):
        reverse_video(test_id1, test_id2)
