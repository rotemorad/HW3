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
        self.readable_files = self._get_readable_files()  # list instance
        self.file_content = self._get_content()  # dict instance

    def _get_readable_files(self):
        """Function checks if the folder is a directory and returns only the files that are readable"""
        sub_files = self.foldername.rglob('*') if self.foldername.is_dir() else self.foldername
        return [file_path for file_path in sub_files if file_path.suffix != '']

    def _get_content(self):
        """Function reads files content and stores them in a dict{file_name: content}"""
        file_content = {}
        for file in self.readable_files:
            file_content.update({file.name: file.read_text()})
        return file_content

    def iter_folder(self):
        """Main function to find duplicate and unique files in the filesystem."""
        values = set(self.file_content.values())
        for value in values:
            #   use filter here :)
            #   use values instead of items
            unique_values = [v for v in self.file_content.values() if v == value]
            self.uniques.append(unique_values[0])
            keys = [k for k, v in self.file_content.items() if v == value]
            if len(keys) != 1:
                self.duplicates.update({keys[0]: keys[1:]})
        return self.duplicates, self.uniques
