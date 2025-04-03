import os

# Define the project structure
project_structure = {
    "dags/": ["ml_pipeline.py"],
    "data/": {
        "raw/": ["iris.csv"],
        "processed/": []
    },
    "models/": ["model.pkl"],
    "scripts/": ["preprocess.py", "train.py", "evaluate.py"],
    "mlflow_tracking/": [],
    "config.yaml": "",
    "requirements.txt": "",
    "dvc.yaml": "",
    "docker-compose.yml": ""
}

def create_structure(base_path, structure):
    for key, value in structure.items():
        path = os.path.join(base_path, key)
        if isinstance(value, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, value)
        elif isinstance(value, list):
            os.makedirs(path, exist_ok=True)
            for file in value:
                file_path = os.path.join(path, file)
                with open(file_path, "w") as f:
                    f.write(f"# {file}\n")
        elif isinstance(value, str):
            with open(path, "w") as f:
                f.write(f"# {key}\n")

# Run script in the current project folder
current_directory = os.getcwd()
create_structure(current_directory, project_structure)

print("MLOps project structure created successfully!")
