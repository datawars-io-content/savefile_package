import os
import pickle
import numpy as np
import pandas as pd
import json
import shutil
import matplotlib.pyplot as plt

# Default global location
__GLOBAL_CSV_SOLUTIONS_LOCATION = "{{ SOLUTION_CSV_LOCATION }}"

def save_file(variable_name, file_name, base_dir=__GLOBAL_CSV_SOLUTIONS_LOCATION, zip_file=False, img_format="png"):
    """
    Save data in various formats (txt, csv, pickle, npy, parquet, image) and optionally zip it.

    Parameters:
    - variable_name: The data to be saved (pandas DataFrame, numpy array, text, dict, bytes, or Matplotlib figure).
    - file_name: Name of the file (without extension).
    - base_dir: The base directory where the file will be saved. Default is __GLOBAL_CSV_SOLUTIONS_LOCATION.
    - zip_file: Whether to zip the file after saving. Default is False.
    - img_format: Format to save Matplotlib figures. Default is 'png'. Can be 'jpg', 'pdf', etc.

    Returns:
    - Path of the saved file or zipped file.
    """

    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    file_path = os.path.join(base_dir, file_name)
    
    # Determine file type and save accordingly
    if isinstance(variable_name, pd.DataFrame):
        variable_name.to_csv(file_path + ".csv", index=False)
        saved_path = file_path + ".csv"
    elif isinstance(variable_name, np.ndarray):
        np.save(file_path + ".npy", variable_name)
        saved_path = file_path + ".npy"
    elif isinstance(variable_name, (list, dict)):
        with open(file_path + ".json", "w") as f:
            json.dump(variable_name, f, indent=4)
        saved_path = file_path + ".json"
    elif isinstance(variable_name, str):
        with open(file_path + ".txt", "w") as f:
            f.write(variable_name)
        saved_path = file_path + ".txt"
    elif isinstance(variable_name, bytes):
        with open(file_path + ".pkl", "wb") as f:
            pickle.dump(variable_name, f)
        saved_path = file_path + ".pkl"
    elif isinstance(variable_name, plt.Figure):  # Save Matplotlib figures
        image_path = f"{file_path}.{img_format}"
        variable_name.savefig(image_path, format=img_format, bbox_inches="tight")
        plt.close(variable_name)  # Close the figure to free memory
        saved_path = image_path
    else:
        raise ValueError("Unsupported data type for saving.")

    # Zip the file if required
    if zip_file:
        zip_path = saved_path + ".zip"
        shutil.make_archive(saved_path, 'zip', base_dir, saved_path.split("/")[-1])
        os.remove(saved_path)  # Remove original after zipping
        return zip_path

    return f"File is successfully saved at: {saved_path}"
