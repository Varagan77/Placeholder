import os

def create_project_structure(base_dir="Project"):
    structure = {
        "bin": ["project"],
        "project": {
            "test": ["__init__.py", "test_main.py"],
            "__init__.py": None,
            "main.py": None
        },
        "setup.py": None,
        "README": None
    }

    def create_structure(base_path, struct):
        for name, content in struct.items():
            path = os.path.join(base_path, name)
            if isinstance(content, dict):  # It's a folder
                os.makedirs(path, exist_ok=True)
                create_structure(path, content)
            elif isinstance(content, list):  # Folder containing files
                os.makedirs(path, exist_ok=True)
                for file in content:
                    open(os.path.join(path, file), 'a').close()
            else:
                # It's a file
                open(path, 'a').close()

    os.makedirs(base_dir, exist_ok=True)
    create_structure(base_dir, structure)
    print(f"Project structure created successfully in '{base_dir}'")

if __name__ == "__main__":
    create_project_structure()
