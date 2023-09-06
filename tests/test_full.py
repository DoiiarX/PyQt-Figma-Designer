import test_read_figma
import pyqt_generator
import pickle

test_read_figma.run()

with open('../resources/f.fig', 'rb') as file:
    figma_file = pickle.load(file)
python_code = '\n'.join(pyqt_generator.generate_pyqt_design(figma_file))
with open('../resources/f.py', 'w') as file:
    file.write(python_code)
exec(python_code)
