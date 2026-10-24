
import json # The json module handles JSON encoding and decoding.
from pathlib import Path
class Database:
    def __init__(self):
        self.file_path = Path(__file__).resolve().parent.parent / "students.data"
        # Path(__file__).resolve(): The absolute path of the current database.py file.
        # First .parent: The cli folder containing database.py.
        # Second .parent: The project root directory, CLIUniApp-Part2-Group9.
        # / "students.data": Use the / operator to append the data filename to the directory path.
        # self.file_path = ...: Store the full path as an attribute of the current 
        self.ensure_file_exists() #Creating a Database object will now also ensure that its data file exists.
    def ensure_file_exists(self):
        if not self.file_path.exists(): #Run the following block only if the path does not exist.
            with self.file_path.open("w", encoding="utf-8") as data_file:
            # Open the file for writing using UTF-8; create it if missing or truncate it if it exists.
            # data_file refers to the open file object, which is automatically closed when the with block ends.
                json.dump([], data_file)
                # Write an empty list in JSON format, representing no student records.
                # []: The data to save: an empty list.
                # data_file: The destination file object.
    def load_data(self):
        with self.file_path.open("r", encoding="utf-8") as data_file:
            return json.load(data_file)
    def save_data(self, data):
        with self.file_path.open("w", encoding="utf-8") as data_file:
            json.dump(data, data_file, indent=4)
    def find_record_by_email(self, email):
        records = self.load_data()
        for record in records:
            if record["email"] == email:
                return record
        return None