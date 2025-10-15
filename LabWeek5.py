# Task 2.1: Load the File
def load_abc_file(filename):
    """Load ABC file into list of lines"""
    with open(filename, 'r', encoding='latin-1') as f:
        lines = f.readlines()
    return lines
