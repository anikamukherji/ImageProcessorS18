def test_reverse_video():
    """
    Tests the reverse_video function
    """

    import pytest
    from image_module.reverse_video import reverse_video
    from PIL import Image

    test_id1 = 'test_image78374897498.png'
    test_id2 = 'test_image898490384903.png'
    test_id3 = 'test.png'
    ima = Image.open('test.png')
    (w, h) = ima.size

    with pytest.raises(FileNotFoundError):
        reverse_video(test_id1, test_id2)

    processed_image = reverse_video(test_id3, test_id2)
    assert (w, h) == processed_image['image_size']
