from pathlib import Path


class FolderIterator:
    """.Iterates through the supplied folder, finding duplicates.

    Call the iter_folder() method to parse the directory.

    Attributes
    ----------
    foldername : path-like
        Name of base folder to iterate on.
    uniques : list
        A list of unique files in the folder and their content.
    duplicates : dict
        The keys are the parent files and the values are a list of filenames
        with the same content.
    """

    def __init__(self, foldername='base'):
        self.foldername = Path(str(foldername))  # pathlib.Path instance
        self.uniques = []  # list instance
        self.duplicates = {}  # dict instance
        self.readable_files = []  # list instance
        self.file_content = {}  # dict instance

    def get_readable_files(self):
        """Function checks if the folder is a directory and returns only the files that are readable"""
        if self.foldername.is_dir():  # folder is a directory- get all sub-directories
            sub_files = (self.foldername.rglob('*'))
            readable_files = [file_path for file_path in sub_files if file_path.suffix != '']
        else:  # folder is not a directory
            readable_files = [file_path for file_path in self.foldername if file_path.suffix != '']
        return readable_files

    def get_content(self):
        """Function reads files content and stores them in a dict{file_name: content}"""
        file_content = {}
        for i in range(len(self.readable_files)):
            file_content.update({self.readable_files[i].name: self.readable_files[i].read_text()})
        return file_content

    def iter_folder(self):
        """Main function to find duplicate and unique files in the filesystem."""
        uniques = []
        duplicates = {}
        self.readable_files = FolderIterator.get_readable_files(self)
        self.file_content = FolderIterator.get_content(self)
        repeated_values = set([v for k, v in self.file_content.items()])
        for value in repeated_values:
            keys_specified_value = [v for k, v in self.file_content.items() if v == value]
            uniques.append(keys_specified_value[0])
            keys_specified_value = [k for k, v in self.file_content.items() if v == value]
            if len(keys_specified_value) != 1:
                duplicates.update({keys_specified_value[0]: keys_specified_value[1::]})
            self.duplicates, self.uniques = (duplicates, uniques)
        return self.duplicates, self.uniques
