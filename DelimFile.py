"""
DelimFile gets file, delimiter (delimiter is a character or a string of characters that will be used
to separate the elements of a list when writing to the file)
"""
from WriteToFile.WriteFile import WriteFile


class DelimFile(WriteFile):
    """
    DelimFile Constructor
    """

    def __init__(self, file_name, delimiter):
        super().__init__(file_name)
        self.delimiter = delimiter

    def write(self, data_list):
        if isinstance(data_list, list):
            data_line = self.delimiter.join(data_list)
            self.write_line(data_line)
        else:
            raise ValueError("Only lists can be written to DelimFile.")
