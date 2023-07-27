import os


def list_file_structure(path):
    file_structure = ""
    ignore_dirs = {".git", "node_modules", "venv", "__pycache__", "vendor"}

    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]

        for file in files:
            file_path = os.path.join(root, file)
            file_path = file_path.replace(path, "")
            file_path = f"./{file_path}"

            if not "git" in file_path:
                file_structure += f"{file_path}\n"

        for dir in dirs:
            dir_path = os.path.join(root, dir)
            dir_path = dir_path.replace(path, "")
            dir_path = f"./{dir_path}"

            if not "git" in dir_path:
                file_structure += f"{dir_path}\n"

    return file_structure
