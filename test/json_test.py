from drewcopytools.jsontools import load_json

def test_can_load_json_with_bom():
    """
    This test case shows us that we can load json data from disk whether it has a byte-order-mark (BOM) or not.
    I mean, if we are just trying to read data from disk and load it into JSON, why the heck would we would have
    to know that exact encoding of the data in the first place?
    """
    TEST_MESSAGE = "Test Message"
    TEST_NUMBER = 123

    path1 = "./test/data/json_no_bom.json"
    no_bom = load_json(path1)
    assert no_bom["Message"] == TEST_MESSAGE, "Invalid test message for no_bom!"
    assert no_bom["Number"] == TEST_NUMBER, "Invalid test number for no_bom!"

    path2 = "./test/data/json_with_bom.json"
    with_bom = load_json(path2)
    assert with_bom["Message"] == TEST_MESSAGE, "Invalid test message for with_bom!"
    assert with_bom["Number"] == TEST_NUMBER, "Invalid test number for with_bom!"
