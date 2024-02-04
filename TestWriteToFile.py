import unittest
from datetime import datetime
from WriteToFile.WriteFile import WriteFile
from WriteToFile.LogFile import LogFile
from WriteToFile.DelimFile import DelimFile
import os


class TestWriteToFile(unittest.TestCase):

    def setUp(self):
        # Clean the test files before each test
        self.clean_file("test_write_file.txt")
        self.clean_file("test_delim_file.txt")

    def tearDown(self):
        # Clean up any remaining files after each test
        self.clean_file("test_write_file.txt")
        self.clean_file("test_delim_file.txt")

    def clean_file(self, file_name):
        # Delete or truncate the file to clean it
        if os.path.exists(file_name):
            os.remove(file_name)
        with open(file_name, 'w'):
            pass

    def test_write_file(self):
        # Test WriteFile class
        file_name = "test_write_file.txt"
        write_file_name = WriteFile(file_name)
        write_file_name.write_line("Test Line")
        with open(file_name, 'r') as file:
            content = file.read()
        self.assertEqual(content.strip(), "Test Line",
                         f"Line should be 'Test Line' we got {content}")

    def test_log_file(self):
        # Test LogFile class
        file_name = "test_write_file.txt"
        log_file = LogFile(file_name)
        log_file.write("Log Test")
        with open(file_name, 'r') as file:
            content = file.read()
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M')
        expected_content = f'{current_time} Log Test\n'
        self.assertEqual(content, expected_content,
                         f"Line should be {expected_content} we got {content}")

    def test_delim_file(self):
        # Test DelimFile class
        file_name = "test_delim_file.txt"
        delimiter = ","
        delim_file = DelimFile(file_name, delimiter)
        data_list = ["item1", "item2", "item3"]
        delim_file.write(data_list)
        with open(file_name, 'r') as file:
            content = file.read()
        expected_content = "item1,item2,item3\n"
        self.assertEqual(content, expected_content,
                         f"Line should be {expected_content} we got {content}")


if __name__ == '__main__':
    unittest.main()
