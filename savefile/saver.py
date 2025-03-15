import os
import pickle
import json
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1) Define the default directory:
DEFAULT_DIR = "/root/.cache/.local/.trash/"

# Ensure the default directory exists at import time
if not os.path.exists(DEFAULT_DIR):
    os.makedirs(DEFAULT_DIR)

def help_save_file():
    """
    Prints out usage instructions and the available functions for saving data.

    Usage:
    ------
    save_file(variable, file_name, base_dir=DEFAULT_DIR, zip_file=False)
    
    The 'file_name' must include an extension that matches the variable type:
      - pd.DataFrame -> .csv, .pkl, .pickle
      - np.ndarray   -> .npy
      - list/dict    -> .json
      - str          -> .txt
      - bytes        -> .pkl, .pickle
      - Matplotlib Figure -> .png, .jpg, .jpeg, .pdf, .svg, .tif, .tiff

    Examples:
    ---------
    >>> df = pd.DataFrame({'A': [1,2], 'B': [3,4]})
    >>> save_file(df, 'dataframe.csv')      # saves as CSV
    >>> save_file(df, 'dataframe.pkl')      # saves as pickle
    >>> arr = np.array([1,2,3])
    >>> save_file(arr, 'myarray.npy')       # saves as .npy
    >>> save_file({'a': 1, 'b': 2}, 'data.json')
    >>> save_file('Hello World', 'message.txt')
    >>> fig, ax = plt.subplots(); ax.plot([1,2],[3,4])
    >>> save_file(fig, 'plot.png')

    Additional Functions:
    ---------------------
    - list_files(base_dir=DEFAULT_DIR): Lists all files in the default directory.
    - delete_file(file_name, base_dir=DEFAULT_DIR): Deletes a file in the default directory.
    """
    print(help_save_file.__doc__)


def save_file(variable, file_name, base_dir=DEFAULT_DIR, zip_file=False):
    """
    Save a variable to disk based on the provided filename extension.
    
    Supported (variable, extension) combinations:
      - pd.DataFrame -> .csv, .pkl, .pickle
      - np.ndarray   -> .npy
      - list/dict    -> .json
      - str          -> .txt
      - bytes        -> .pkl, .pickle
      - Matplotlib Figure -> typical image extensions like .png, .jpg, .jpeg, .pdf, .svg, .tif, .tiff
    
    If the file extension and variable type do not match any of these known patterns,
    the function raises a ValueError stating it is not possible.
    
    Parameters:
    -----------
    variable : object
        The data to be saved.
    file_name : str
        The filename, including extension (e.g., 'data.csv', 'plot.png', etc.).
    base_dir : str
        Base directory to save the file. Defaults to DEFAULT_DIR.
    zip_file : bool
        Whether to zip the file after saving. If True, the original file is removed.
        
    Returns:
    --------
    str
        Path of the saved or zipped file.
    """
    # Ensure base directory exists
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # Extract extension from the file name
    file_base, file_ext = os.path.splitext(file_name)
    file_ext = file_ext.lower().strip()  # normalize extension
    file_path_no_ext = os.path.join(base_dir, file_base)

    # 1) Pandas DataFrame
    if isinstance(variable, pd.DataFrame):
        if file_ext == '.csv':
            saved_path = file_path_no_ext + '.csv'
            variable.to_csv(saved_path, index=False)
        elif file_ext in ('.pkl', '.pickle'):
            saved_path = file_path_no_ext + file_ext
            variable.to_pickle(saved_path)
        else:
            raise ValueError(f"DataFrame cannot be saved with extension '{file_ext}'. "
                             "Use .csv, .pkl, or .pickle.")

    # 2) NumPy array
    elif isinstance(variable, np.ndarray):
        if file_ext == '.npy':
            saved_path = file_path_no_ext + '.npy'
            np.save(saved_path, variable)
        else:
            raise ValueError(f"NumPy array cannot be saved with extension '{file_ext}'. "
                             "Use .npy.")

    # 3) list or dict (JSON)
    elif isinstance(variable, (list, dict)):
        if file_ext == '.json':
            saved_path = file_path_no_ext + '.json'
            with open(saved_path, "w") as f:
                json.dump(variable, f, indent=4)
        else:
            raise ValueError(f"list/dict cannot be saved with extension '{file_ext}'. "
                             "Use .json.")

    # 4) str (text)
    elif isinstance(variable, str):
        if file_ext == '.txt':
            saved_path = file_path_no_ext + '.txt'
            with open(saved_path, "w") as f:
                f.write(variable)
        else:
            raise ValueError(f"String cannot be saved with extension '{file_ext}'. "
                             "Use .txt.")

    # 5) bytes (pickled)
    elif isinstance(variable, bytes):
        if file_ext in ('.pkl', '.pickle'):
            saved_path = file_path_no_ext + file_ext
            with open(saved_path, "wb") as f:
                pickle.dump(variable, f)
        else:
            raise ValueError(f"bytes cannot be saved with extension '{file_ext}'. "
                             "Use .pkl or .pickle.")

    # 6) Matplotlib Figure (images)
    elif isinstance(variable, plt.Figure):
        valid_extensions = ['.png', '.jpg', '.jpeg', '.pdf', '.svg', '.tif', '.tiff']
        if file_ext in valid_extensions:
            saved_path = file_path_no_ext + file_ext
            variable.savefig(saved_path, format=file_ext.replace('.', ''), bbox_inches='tight')
            plt.close(variable)
        else:
            raise ValueError(f"Matplotlib figure cannot be saved with extension '{file_ext}'. "
                             f"Use one of {valid_extensions}")

    else:
        raise ValueError("Unsupported data type for saving.")

    # (Optional) Zip the file
    if zip_file:
        zip_path = saved_path + ".zip"
        shutil.make_archive(saved_path, 'zip', base_dir, os.path.basename(saved_path))
        os.remove(saved_path)  # remove the original file after zipping
        return f"File successfully zipped at: {zip_path}"

    return f"File successfully saved at: {saved_path}"


def list_files(base_dir=DEFAULT_DIR):
    """
    List all files in the given (or default) directory.
    
    Returns:
    --------
    files : list of str
        Names of the files in the directory (not full paths).
    """
    if not os.path.exists(base_dir):
        print(f"Directory '{base_dir}' does not exist.")
        return []
    
    # List only files (ignore sub-directories)
    all_entries = os.listdir(base_dir)
    files_only = [f for f in all_entries if os.path.isfile(os.path.join(base_dir, f))]
    
    return files_only


def delete_file(file_name, base_dir=DEFAULT_DIR):
    """
    Delete a file from the given (or default) directory.
    
    Parameters:
    -----------
    file_name : str
        The name of the file to delete.
    base_dir : str
        The directory where the file is located. Defaults to DEFAULT_DIR.
        
    Returns:
    --------
    str
        Message indicating success or failure.
    """
    target_path = os.path.join(base_dir, file_name)
    
    if os.path.exists(target_path) and os.path.isfile(target_path):
        os.remove(target_path)
        return f"File '{file_name}' has been deleted from '{base_dir}'."
    else:
        return f"File '{file_name}' does not exist in '{base_dir}'."
