# Task 2.1: Load the File
def load_abc_file(filename):
    """Load ABC file into list of lines"""
    with open(filename, 'r', encoding='latin-1') as f:
        lines = f.readlines()
    return lines

# Task 3.2: Extract Tune Metadata
def parse_tune(tune_lines):
    """Parse a single tune from lines"""
    tune = {
        'X': None,
        'title': None,
        'alt_title': None,
        'tune_type': None,
        'key': None,
        'notation': '\n'.join(tune_lines)
    }
    
    title_count = 0
    
    for line in tune_lines:
        line = line.strip()
        
        if line.startswith('X:'):
            tune['X'] = line[2:].strip()
        
        elif line.startswith('T:'):
            if title_count == 0:
                tune['title'] = line[2:].strip()
                title_count += 1
            elif title_count == 1:
                tune['alt_title'] = line[2:].strip()
                title_count += 1
        
        elif line.startswith('R:'):
            tune['tune_type'] = line[2:].strip()
        
        elif line.startswith('K:'):
            tune['key'] = line[2:].strip()
    
    return tune
