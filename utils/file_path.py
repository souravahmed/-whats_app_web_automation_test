import os


class FilePathUtil:
    
    @classmethod
    def get_excel_file_path(self):
        return os.path.join(os.getcwd(), "Tests", "ExcelFile")