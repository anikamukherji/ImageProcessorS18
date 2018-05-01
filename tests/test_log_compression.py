def test_log_compression():
    """
    Tests the log_compression function
    """

    import pytest
    from Server.image_module.log_compression import log_compression
    import PIL
    from PIL import Image

    test_id1 = 'test_image78374897498.png'
    test_id2 = 'test_image898490384903.png'
    # test_id3 = 'test.png'
    # ima = Image.open(test_id3)
    # (w, h) = ima.size

    with pytest.raises(FileNotFoundError):
        log_compression(test_id1, test_id2)

    # processed_image = log_compression(test_id3, test_id2)
    # assert (w, h) == processed_image['image_size']
