# File Writing System README

## Overview

This Python code provides a simple file-writing system with three classes: `WriteFile`, `DelimFile`, and `LogFile`. These classes are designed to facilitate writing to files with different functionalities.

### Class Descriptions

1. **WriteFile:**
   - Base class for writing lines to a file.
   - Constructor: Takes a file name as a parameter.
   - Method: `write_line(text)` - Appends the provided text to the file in append mode.

2. **DelimFile:**
   - Inherits from `WriteFile`.
   - Constructor: Takes a file name and a delimiter as parameters.
   - Method: `write(data_list)` - Writes a list of data to the file, joining elements with the specified delimiter.

3. **LogFile:**
   - Inherits from `WriteFile`.
   - Constructor: Takes a file name as a parameter.
   - Method: `write(text)` - Writes a log line to the file with a timestamp and the provided text.
