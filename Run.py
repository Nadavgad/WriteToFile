"""
Example usage:
"""
from WriteToFile.DelimFile import DelimFile
from WriteToFile.LogFile import LogFile

log = LogFile('log.txt')
csv_file = DelimFile('text.csv', ',')

log.write('this is a log message')
log.write('another log message')

csv_file.write(['a', 'b', 'c', 'd'])
csv_file.write(['1', '2', '3'])

"""
Check the content of the log file.
'r': Read mode. Opens the file for reading.
"""
with open('log.txt', 'r') as log_file:
    log_content = log_file.read()
print("Content of log.txt:")
print(log_content)

"""
Check the content of the CSV file
"""
with open('text.csv', 'r') as csv_file:
    csv_content = csv_file.read()
print("\nContent of text.csv:")
print(csv_content)
