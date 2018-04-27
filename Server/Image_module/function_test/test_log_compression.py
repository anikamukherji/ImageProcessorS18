def test_log_compression():
    """
    Tests the log_compression function
    """
    try:
        import pytest
        from Image_module.log_compression import log_compression
    except ImportError:
        print("Necessary imports for this test function failed")
        return

    test_id1 = 'test_image78374897498.png'
    test_id2 = 'test_image898490384903.png'

    with pytest.raises(NameError):
        log_compression(test_id1, test_id2)
