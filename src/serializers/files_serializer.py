class FilesSerializer:
    @classmethod
    def serialize(self, files):
        serialized_files = ""

        for index, _ in enumerate(files["ids"][0]):
            file_path = files["metadatas"][0][index]["path"]
            document = files["documents"][0][index]

            serialized_file = f"File: {file_path}\n" f"Code: {document}\n\n"
            serialized_files += serialized_file

        return serialized_files
