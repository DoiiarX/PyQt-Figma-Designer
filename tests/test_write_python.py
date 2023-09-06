import pickle
import pyqt_generator

with open('../resources/f.fig', 'rb') as file:
    figma_file = pickle.load(file)
python_code = '\n'.join(pyqt_generator.generate_pyqt_design(figma_file))
print(python_code)
exec(python_code)
