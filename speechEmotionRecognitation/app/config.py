import pathlib
import os

working_dir_path = pathlib.Path().absolute()

TRAINING_FILES_PATH = os.path.join(str(working_dir_path), '..\features')
SAVE_DIR_PATH = os.path.join(str(working_dir_path), 'joblib_features')
MODEL_DIR_PATH = os.path.join(str(working_dir_path), 'app\model')
EXAMPLE_PATH = os.path.join(str(working_dir_path), 'examples')