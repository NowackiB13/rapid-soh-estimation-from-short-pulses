
import numpy as np
import pandas as pd
from scipy import interpolate
import matplotlib as mpl
import matplotlib.pyplot as plt

import pickle
from pathlib import Path
import warnings
import os, sys
import re



cwd = os.path.abspath(__file__)
dir_repo_main = Path(str(cwd)[:str(cwd).rindex('rapid-soh-estimation-from-short-pulses') + len('rapid-soh-estimation-from-short-pulses')])
assert dir_repo_main.is_dir()


# =================================================================================
# GLOBAL PATH DEFINITONS
# =================================================================================
dir_figures = dir_repo_main.joinpath("figures")
dir_notebooks = dir_repo_main.joinpath("notebooks")
dir_processed_data = dir_repo_main.joinpath("processed_data")
dir_spreadsheets = dir_repo_main.joinpath("spreadsheets")


# =================================================================================
# GLOBAL VARIABLES
# =================================================================================
path_test_tracker = dir_spreadsheets.joinpath("Cell_Test_Tracker.xlsx")
df_test_tracker = pd.read_excel(path_test_tracker, sheet_name=0, engine='openpyxl')


if __name__ == '__main__':
    print('config.py()')