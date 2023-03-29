from drewcopytools.jsontools import load_json
from drewcopytools.jsontools import map_json_to_class

# -----------------------------------------------------------------------------------------------
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


# Test types....
class Person:
    def __init__(self):
        self.name = None
        self.age = None

class Car:
    def __init__(self):
        self.make = None
        self.model = None
        self.year = None


# -------------------------------------------------------------------------------------
def test_can_map_person_from_json():
    json_data = {"name": "Alice", "age": 30}
    person = map_json_to_class(json_data, Person)
    assert person.name == "Alice"
    assert person.age == 30

# -------------------------------------------------------------------------------------
def test_can_map_car_from_json():
    json_data = {"make": "Ford", "model": "Mustang", "year": 2022}
    car = map_json_to_class(json_data, Car)
    assert car.make == "Ford"
    assert car.model == "Mustang"
    assert car.year == 2022