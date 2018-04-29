def test_contrast_stretching():
    """
    Tests the contrast_stretching function
    """

    import pytest
    from image_module.contrast_stretching import contrast_stretching
    import PIL
    from PIL import Image

    test_id1 = 'test_image78374897498.png'
    test_id2 = 'test_image898490384903.png'
    # test_id3 = 'test.png'
    # ima = Image.open(test_id3)
    # (w, h) = ima.size

    with pytest.raises(FileNotFoundError):
        contrast_stretching(test_id1, test_id2)

    # processed_image = contrast_stretching(test_id3, test_id2)
    # assert (w, h) == processed_image['image_size']
