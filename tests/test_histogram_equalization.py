def test_histogram_equalization():
    """
    Tests the histogram_equalization function
    """

    import pytest
    from Server.image_module.histogram_equalization \
        import histogram_equalization
    import PIL
    from PIL import Image

    test_id1 = 'test_image78374897498.png'
    test_id2 = 'test_image898490384903.png'
    # test_id3 = 'test.png'
    # ima = Image.open(test_id3)
    # (w, h) = ima.size

    with pytest.raises(FileNotFoundError):
        histogram_equalization(test_id1, test_id2)

    # processed_image = histogram_equalization(test_id3, test_id2)
    # assert (w, h) == processed_image['image_size']
