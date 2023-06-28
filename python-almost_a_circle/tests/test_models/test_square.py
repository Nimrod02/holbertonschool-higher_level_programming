import unittest
from models.square import Square


class TestSquareMethods(unittest.TestCase):
    def test_constructor(self):
        square = Square(5)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertIsNotNone(square.id)

        square = Square(3, 2, 3, 10)
        self.assertEqual(square.size, 3)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 10)

    def test_string_representation(self):
        square = Square(4, 1, 2, 7)
        expected = "[Square] (7) 1/2 - 4"
        self.assertEqual(str(square), expected)

    def test_size_property(self):
        square = Square(5)
        square.size = 8
        self.assertEqual(square.size, 8)
        self.assertEqual(square.width, 8)
        self.assertEqual(square.height, 8)

    def test_update_method(self):
        square = Square(3, 1, 2, 7)
        square.update(10)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 3)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)

        square.update(20, 5, 6, 7)
        self.assertEqual(square.id, 20)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 6)
        self.assertEqual(square.y, 7)

        square.update(x=3, y=4)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

    def test_to_dictionary_method(self):
        square = Square(4, 1, 2, 7)
        expected = {'x': 1, 'y': 2, 'id': 7, 'size': 4}
        self.assertEqual(square.to_dictionary(), expected)


if __name__ == '__main__':
    unittest.main()
