import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def setUp(self):
        self.base = Base()

    def tearDown(self):
        del self.base

    def test_init_with_id(self):
        base = Base(10)
        self.assertEqual(base.id, 10)

    def test_init_without_id(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_to_json_string_with_empty_list(self):
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_with_non_empty_list(self):
        list_dictionaries = [{"key": "value"}]
        json_string = Base.to_json_string(list_dictionaries)
        self.assertEqual(json_string, '[{"key": "value"}]')

    def test_save_to_file_with_none_list(self):
        Base.save_to_file(None)


    def test_save_to_file_with_empty_list(self):
        Base.save_to_file([])

    def test_save_to_file_with_non_empty_list(self):
        pass

    def test_from_json_string_with_empty_string(self):
        instances = Base.from_json_string("")
        self.assertEqual(instances, [])

    def test_from_json_string_with_non_empty_string(self):
        json_string = '[{"key": "value"}]'
        instances = Base.from_json_string(json_string)
        self.assertEqual(instances, [{"key": "value"}])

    def test_create_with_rectangle(self):
        dictionary = {"width": 2, "height": 4}
        instance = Base.create(**dictionary)

    def test_create_with_square(self):
        dictionary = {"size": 3}
        instance = Base.create(**dictionary)

    def test_create_with_invalid_class(self):
        dictionary = {"invalid_key": "value"}
        instance = Base.create(**dictionary)
        self.assertIsNone(instance)

    def test_load_from_file_with_non_existent_file(self):
        instances = Base.load_from_file()
        self.assertEqual(instances, [])

    def test_load_from_file_with_empty_file(self):
        instances = Base.load_from_file()
        self.assertEqual(instances, [])

    def test_load_from_file_with_non_empty_file(self):
        instances = Base.load_from_file()

if __name__ == "__main__":
    unittest.main()
