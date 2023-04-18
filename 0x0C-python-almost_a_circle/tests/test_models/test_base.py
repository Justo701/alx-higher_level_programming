#!/usr/bin/python3
"""unittest base.
test cases for base class.
each test has the number of the task,
and the number of the test for that task
(i.e 'test_17_0' for the first test of task 17)
"""

import unittest
import os
from models.base import base
from models.rectangle import rectangle
from models.square import square


class testbase(unittest.testcase):
    """test class for base class."""

    def setup(self):
        base._base__nb_objects = 0

    def test_1_0(self):
        """create new instances: check for id."""

        b0 = base()
        self.assertequal(b0.id, 1)
        b1 = base()
        self.assertequal(b1.id, 2)
        b2 = base(12)
        self.assertequal(b2.id, 12)
        b3 = base(0)
        self.assertequal(b3.id, 0)
        b4 = base(927)
        self.assertequal(b4.id, 927)
        b5 = base(-5)
        self.assertequal(b5.id, -5)
        b6 = base(9)
        self.assertequal(b6.id, 9)

    def test_1_1(self):
        """test for type and instance."""

        b6 = base()
        self.assertequal(type(b6), base)
        self.asserttrue(isinstance(b6, base))

    def test_15_0(self):
        """test static method to_json_string with regular dict."""

        d = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_d = base.to_json_string([d])
        self.asserttrue(isinstance(d, dict))
        self.asserttrue(isinstance(json_d, str))
        self.assertcountequal(
            json_d, '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]')
        json_d_1 = base.to_json_string([])
        self.assertequal(json_d_1, "[]")
        json_d_2 = base.to_json_string(none)
        self.assertequal(json_d_1, "[]")

    def test_15_1(self):
        """test static method to_json_string with wrong types."""

        with self.assertraises(typeerror) as x:
            base.to_json_string(9)
        self.assertequal(
            "list_dictionaries must be a list of dictionaries", str(
                x.exception))
        with self.assertraises(typeerror) as x:
            base.to_json_string("hello")
        self.assertequal(
            "list_dictionaries must be a list of dictionaries", str(
                x.exception))
        with self.assertraises(typeerror) as x:
            base.to_json_string(["hi", "here"])
        self.assertequal(
            "list_dictionaries must be a list of dictionaries", str(
                x.exception))
        with self.assertraises(typeerror) as x:
            base.to_json_string(7.8)
        self.assertequal(
            "list_dictionaries must be a list of dictionaries", str(
                x.exception))
        with self.assertraises(typeerror) as x:
            base.to_json_string([2, 1, 3, 4])
        self.assertequal(
            "list_dictionaries must be a list of dictionaries", str(
                x.exception))
        with self.assertraises(typeerror) as x:
            base.to_json_string({1: 'hi', 2: 'there'})
        self.assertequal(
            "list_dictionaries must be a list of dictionaries", str(
                x.exception))
        with self.assertraises(typeerror) as x:
            base.to_json_string((9, 0))
        self.assertequal(
            "list_dictionaries must be a list of dictionaries", str(
                x.exception))
        with self.assertraises(typeerror) as x:
            base.to_json_string(true)
        self.assertequal(
            "list_dictionaries must be a list of dictionaries", str(
                x.exception))

    def test_15_2(self):
        """test static method to_json_string with wrong number of args."""

        s1 = ("to_json_string() missing 1 required positional argument: " +
              "'list_dictionaries'")
        with self.assertraises(typeerror) as x:
            base.to_json_string()
        self.assertequal(s1, str(x.exception))
        s2 = "to_json_string() takes 1 positional argument but 2 were given"
        with self.assertraises(typeerror) as x:
            base.to_json_string([{1, 2}], [{3, 4}])
        self.assertequal(s2, str(x.exception))

    def test_16_0(self):
        """test class method save_to_file with normal types."""

        r0 = rectangle(10, 7, 2, 8)
        r1 = rectangle(2, 4)
        rectangle.save_to_file([r0, r1])
        res = ('[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7},' +
               ' {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]')
        with open("rectangle.json", "r") as f:
            self.assertequal(len(f.read()), len(res))
        rectangle.save_to_file(none)
        res = "[]"
        with open("rectangle.json", "r") as f:
            self.assertequal(f.read(), res)
        os.remove("rectangle.json")
        rectangle.save_to_file([])
        with open("rectangle.json", "r") as f:
            self.assertequal(f.read(), res)
        s0 = square(9, 3, 1, 12)
        s1 = square(6, 7)
        square.save_to_file([s0, s1])
        res = ('[{"id": 12, "size": 9, "x": 3, "y": 1},' +
               ' {"id": 3, "size": 6, "x": 7, "y": 0}]')
        with open("square.json", "r") as f:
            self.assertequal(len(f.read()), len(res))
        square.save_to_file(none)
        res = "[]"
        with open("square.json", "r") as f:
            self.assertequal(f.read(), res)
        os.remove("square.json")
        square.save_to_file([])
        with open("square.json", "r") as f:
            self.assertequal(f.read(), res)

    def test_16_1(self):
        """test class method save_to_file with errors."""

        with self.assertraises(attributeerror) as x:
            base.save_to_file([base(9), base(5)])
        self.assertequal(
            "'base' object has no attribute 'to_dictionary'", str(
                x.exception))
        with self.assertraises(attributeerror) as x:
            rectangle.save_to_file([3, 4])
        self.assertequal(
            "'int' object has no attribute 'to_dictionary'", str(
                x.exception))
        with self.assertraises(typeerror) as x:
            rectangle.save_to_file(5)
        self.assertequal(
            "'int' object is not iterable", str(
                x.exception))

    def test_16_2(self):
        """test class method save_to_file with wrong args."""

        s1 = ("save_to_file() missing 1 required" +
              " positional argument: 'list_objs'")
        with self.assertraises(typeerror) as x:
            rectangle.save_to_file()
        self.assertequal(s1, str(x.exception))
        s2 = ("save_to_file() takes 2 positional" +
              " arguments but 3 were given")
        with self.assertraises(typeerror) as x:
            rectangle.save_to_file([rectangle(9, 4), rectangle(8, 9)], 98)
        self.assertequal(s2, str(x.exception))

    def test_17_0(self):
        """test static method from_json_string with normal types."""

        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = rectangle.to_json_string(list_input)
        list_output = rectangle.from_json_string(json_list_input)
        res = [{'width': 10, 'height': 4, 'id': 89},
               {'width': 1, 'height': 7, 'id': 7}]
        self.assertcountequal(list_output, res)
        self.assertequal(type(list_output), list)

        list_output_1 = rectangle.from_json_string('')
        self.assertequal(list_output_1, [])

        list_output_2 = rectangle.from_json_string(none)
        self.assertequal(list_output_2, [])

    def test_17_1(self):
        """test static method from_json_string with wrong types."""

        with self.assertraises(typeerror) as x:
            list_output = rectangle.from_json_string([8, 9])
        self.assertequal("json_string must be a string", str(x.exception))
        with self.assertraises(typeerror) as x:
            list_output = rectangle.from_json_string(8)
        self.assertequal("json_string must be a string", str(x.exception))
        with self.assertraises(typeerror) as x:
            list_output = rectangle.from_json_string(9.6)
        self.assertequal("json_string must be a string", str(x.exception))
        with self.assertraises(typeerror) as x:
            list_output = rectangle.from_json_string((4, 5))
        self.assertequal("json_string must be a string", str(x.exception))
        with self.assertraises(typeerror) as x:
            list_output = rectangle.from_json_string({1: 'hello', 2: 'hi'})
        self.assertequal("json_string must be a string", str(x.exception))

    def test_17_2(self):
        """test static method from_json_string with wrong args."""

        s1 = ("from_json_string() missing 1" +
              " required positional argument: 'json_string'")
        with self.assertraises(typeerror) as x:
            rectangle.from_json_string()
        self.assertequal(s1, str(x.exception))
        s2 = "from_json_string() takes 1 positional argument but 2 were given"
        with self.assertraises(typeerror) as x:
            rectangle.from_json_string("hi", 98)
        self.assertequal(s2, str(x.exception))

    def test_18_0(self):
        """test class method create with normal types."""

        r1 = rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = rectangle.create(**r1_dictionary)
        self.assertequal(str(r1), str(r2))
        self.assertfalse(r1 is r2)
        self.assertfalse(r1 == r2)
        s1 = square(3, 5)
        s1_dictionary = s1.to_dictionary()
        s2 = square.create(**s1_dictionary)
        self.assertequal(str(s1), str(s2))
        self.assertfalse(s1 is s2)
        self.assertfalse(s1 == s2)

    def test_18_1(self):
        """test class method create with wrong types."""

        with self.assertraises(typeerror) as x:
            r1 = "hello"
            r2 = rectangle.create(r1)
        self.assertequal(
            "create() takes 1 positional argument but 2 were given", str(
                x.exception))

    def test_19_0(self):
        """test class method load_from_file with normal types."""

        r1 = rectangle(10, 7, 2, 8)
        r2 = rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = rectangle.load_from_file()
        for x in zip(list_rectangles_input, list_rectangles_output):
            self.assertequal(str(x[0]), str(x[1]))

        s1 = square(10, 2)
        s2 = square(9)
        list_squares_input = [s1, s2]
        square.save_to_file(list_squares_input)
        list_squares_output = square.load_from_file()
        for x in zip(list_squares_input, list_squares_output):
            self.assertequal(str(x[0]), str(x[1]))

    def test_19_1(self):
        """test class method load_from_file with missing files."""

        if os.path.exists("rectangle.json"):
            os.remove("rectangle.json")
        if os.path.exists("square.json"):
            os.remove("square.json")
        if os.path.exists("base.json"):
            os.remove("base.json")
        list_rectangles_output = rectangle.load_from_file()
        self.assertequal(list_rectangles_output, [])
        list_squares_output = square.load_from_file()
        self.assertequal(list_squares_output, [])

    def test_19_2(self):
        """test class method load_from_file with wrong args."""

        s = "load_from_file() takes 1 positional argument but 2 were given"
        with self.assertraises(typeerror) as x:
            list_rectangles_output = rectangle.load_from_file("hello")
        self.assertequal(s, str(x.exception))

    def test_20_0(self):
        """test class method save_to_file_csv with normal types."""

        r0 = rectangle(10, 7, 2, 8)
        r1 = rectangle(2, 4)
        rectangle.save_to_file_csv([r0, r1])
        res = "id,width,height,x,y\n1,10,7,2,8\n2,2,4,0,0\n"
        with open("rectangle.csv", "r") as f:
            self.assertequal(len(f.read()), len(res))
        s0 = square(9, 3, 1, 12)
        s1 = square(6, 7)
        square.save_to_file_csv([s0, s1])
        res = "id,size,x,y\n12,9,3,1\n3,6,7,0\n"
        with open("square.csv", "r") as f:
            self.assertequal(len(f.read()), len(res))

    def test_20_1(self):
        """test class method save_to_file_csv with errors."""

        with self.assertraises(attributeerror) as x:
            base.save_to_file_csv([base(9), base(5)])
        self.assertequal(
            "'base' object has no attribute 'to_dictionary'", str(
                x.exception))
        with self.assertraises(typeerror) as x:
            rectangle.save_to_file_csv([3, 4])
        self.assertequal(
            "list_objs must be a list of instances", str(
                x.exception))
        with self.assertraises(typeerror) as x:
            rectangle.save_to_file_csv(5.9)
        self.assertequal(
            "list_objs must be a list of instances", str(
                x.exception))

    def test_20_2(self):
        """test class method save_to_file_csv with wrong args."""

        s1 = ("save_to_file_csv() missing 1 required" +
              " positional argument: 'list_objs'")
        with self.assertraises(typeerror) as x:
            rectangle.save_to_file_csv()
        self.assertequal(s1, str(x.exception))
        s2 = "save_to_file_csv() takes 2 positional arguments but 3 were given"
        with self.assertraises(typeerror) as x:
            rectangle.save_to_file_csv([rectangle(9, 4), rectangle(8, 9)], 98)
        self.assertequal(s2, str(x.exception))

    def test_20_3(self):
        """test class method load_from_file_csv with normal types."""

        r1 = rectangle(10, 7, 2, 8)
        r2 = rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = rectangle.load_from_file_csv()
        for x in zip(list_rectangles_input, list_rectangles_output):
            self.assertequal(str(x[0]), str(x[1]))

        s1 = square(10, 2)
        s2 = square(9)
        list_squares_input = [s1, s2]
        square.save_to_file_csv(list_squares_input)
        list_squares_output = square.load_from_file_csv()
        for x in zip(list_squares_input, list_squares_output):
            self.assertequal(str(x[0]), str(x[1]))

    def test_20_4(self):
        """test class method load_from_file_csv with missing files."""

        os.remove("rectangle.csv")
        os.remove("square.csv")
        os.remove("base.csv")
        list_rectangles_output = rectangle.load_from_file_csv()
        self.assertequal(list_rectangles_output, [])
        list_squares_output = square.load_from_file_csv()
        self.assertequal(list_squares_output, [])

    def test_20_5(self):
        """test class method load_from_file_csv with wrong args."""

        s = "load_from_file_csv() takes 1 positional argument but 2 were given"
        with self.assertraises(typeerror) as x:
            list_rectangles_output = rectangle.load_from_file_csv("hello")
        self.assertequal(s, str(x.exception))

if __name__ == '__main__':
    unittest.main()


