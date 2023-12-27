"""
Base class that handles the basic functionality of writing lines to a file.
"""


class WriteFile:
    """
    WriteFile Constructor
    """

    def __init__(self, file_name):
        self.file_name = file_name

    """
    Write the text we get to the file
    'a': Append mode. Opens the file for writing. If the file does not exist, it creates a new file.
    If the file exists, it appends data to the end of the file.
    """

    def write_line(self, text):
        with open(self.file_name, 'a') as file:
            file.write(f'{text}\n')
