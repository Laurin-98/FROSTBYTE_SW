import subprocess

# Liste der Jupyter-Notebook-Dateien
notebooks = [
    "1_RegimeClassification.ipynb",
    "2_StreamflowPreprocessing.ipynb",
    "3_SWEPreprocessing.ipynb",
    "4_AnotherNotebook.ipynb",
    "5_LastNotebook.ipynb"
]


# Funktion zur Ausführung von Notebooks
def run_notebook(notebook):
    try:
        # Befehl zum Ausführen des Notebooks
        command = [
            "jupyter", "nbconvert",
            "--to", "notebook",
            "--execute",
            "--inplace",
            notebook
        ]
        subprocess.run(command, check=True)
        print(f"Notebook {notebook} wurde erfolgreich ausgeführt.")
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Ausführen von {notebook}: {e}")


# Notebooks nacheinander ausführen
for notebook in notebooks:
    run_notebook(notebook)
