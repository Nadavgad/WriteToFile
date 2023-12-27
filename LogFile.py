"""
LogFile inherits from WriteFile and uses the write_line function to write the current time and the text.
"""
from datetime import datetime

from WriteToFile.WriteFile import WriteFile


class LogFile(WriteFile):
    def __init__(self, file_name):
        super().__init__(file_name)

    def write(self, text):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M')
        log_line = f'{current_time} {text}'
        self.write_line(log_line)

