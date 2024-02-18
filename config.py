import pathlib
import os

working_dir_path = pathlib.Path().absolute()

TRAINING_FILES_PATH = os.path.join(str(working_dir_path), 'features') #just remove the 'features' with  your actual training datasets directory
SAVE_DIR_PATH = os.path.join(str(working_dir_path), 'joblib_features')
MODEL_DIR_PATH = os.path.join(str(working_dir_path), 'model')
EXAMPLE_PATH = os.path.join(str(working_dir_path), 'examples')
TESS_ORIGINAL_FOLDER_PATH = os.path.join(str(working_dir_path), 'give the path of TESS dataset form working dir')
