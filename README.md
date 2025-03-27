# SaveFile Utility Package

## 📝 Description
**SaveFile** is a Python utility package that allows you to **save various data formats** (CSV, TXT, JSON, NumPy arrays, Pickle, Matplotlib figures, etc.) and optionally **zip** them. It helps in organizing and storing different file types efficiently.

---

## 📦 Installation

First, clone the repository then install the package using `pip`:

```bash
git clone https://github.com/datawars-io-content/savefile_package.git
cd savefile_package
pip install .
```

---

## 🚀 Usage

### Import the package:
```python
from savefile import save_file, list_files, delete_file
```
*(Or `from savefile.saver import save_file` if you only need `save_file`.)*

---

### ✅ Default Save Location (No `base_dir` Provided)

By default, if you do not specify a `base_dir`, your file will be saved to:
```plaintext
/root/.cache/.local/.trash/
```

**Example:**
```python
import pandas as pd
df = pd.DataFrame({"col": [1, 2, 3]})

# No base_dir provided, so it goes to the default directory:
save_file(df, "my_df.csv")
```
> **Saves** to `/root/.cache/.local/.trash/my_df.csv`

---

### ✅ Saving a Pandas DataFrame as CSV
```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
save_file(df, "dataframe.csv", base_dir="output")
```
> **Saves** to `output/dataframe.csv`

To save as Pickle instead:
```python
save_file(df, "dataframe.pkl", base_dir="output")
```
> **Saves** to `output/dataframe.pkl`

---

### ✅ Saving a NumPy Array as `.npy`
```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
save_file(arr, "array.npy", base_dir="output")
```
> **Saves** to `output/array.npy`

---

### ✅ Saving a Dictionary or List as JSON
```python
data_dict = {"name": "Anurag", "age": 25}
save_file(data_dict, "info.json", base_dir="output")
```
> **Saves** to `output/info.json`

---

### ✅ Saving Text as a TXT File
```python
save_file("Hello, world!", "message.txt", base_dir="output")
```
> **Saves** to `output/message.txt`

---

### ✅ Saving Binary Data as Pickle
```python
binary_data = b"Some binary data"
save_file(binary_data, "binary_data.pkl", base_dir="output")
```
> **Saves** to `output/binary_data.pkl`

---

### ✅ Saving a Matplotlib Figure
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [10, 20, 25, 30])
ax.set_title("Sample Plot")

save_file(fig, "plot.png", base_dir="output")
```
> **Saves** to `output/plot.png`

You can also save in other supported formats (e.g. `.pdf`, `.jpg`, `.svg`, `.tif`, etc.) by including the appropriate extension in the filename:
```python
save_file(fig, "plot.pdf", base_dir="output")
```
> **Saves** to `output/plot.pdf`

---

### ✅ Saving and Zipping a File
```python
save_file(df, "dataframe.csv", base_dir="output", zip_file=True)
```
> **Saves** to `output/dataframe.csv.zip` and removes the original `dataframe.csv`.

---

## ⚙️ Supported File Formats
| Data Type          | Valid Extensions                           | Example                     |
|--------------------|--------------------------------------------|-----------------------------|
| Pandas DataFrame   | `.csv`, `.pkl`, `.pickle`                  | `dataframe.csv`            |
| NumPy Array        | `.npy`                                     | `array.npy`                |
| Dictionary/List    | `.json`                                    | `info.json`                |
| String (Text)      | `.txt`                                     | `message.txt`              |
| Binary Data        | `.pkl`, `.pickle`                          | `binary_data.pkl`          |
| Matplotlib Figure  | `.png`, `.jpg`, `.jpeg`, `.pdf`, `.svg`, `.tif`, `.tiff` | `plot.png` |

---

## 🛠️ Additional Utility Functions

### Listing Files
```python
files = list_files(base_dir="output")
print(files)
```
> Lists all files in `output`.

### Deleting Files
```python
message = delete_file("dataframe.csv", base_dir="output")
print(message)
```
> Deletes `dataframe.csv` from `output` and prints a success/failure message.

---

## 🛠️ Features
- ✅ Save multiple data types effortlessly  
- ✅ Supports **Pandas DataFrames, NumPy arrays, JSON, text, binary files, and Matplotlib figures**  
- ✅ **Optional zipping** for easy storage  
- ✅ Flexible **base directory** for saving files (defaults to `/root/.cache/.local/.trash/`)  
- ✅ **Auto-creates directories** if they don’t exist  

---

## ⚠️ Important Notes
1. **Always specify the correct file extension** when calling `save_file(variable, file_name)`.  
2. If the extension and data type don’t match, the function raises a `ValueError`.  
3. Use `zip_file=True` if you want the file automatically archived and the original removed.  
4. If you do **not** provide a `base_dir`, the file will be saved to `/root/.cache/.local/.trash/`.
