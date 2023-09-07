import pickle
import pyqt_generator

with open('../resources/f.fig', 'rb') as file:
    figma_file = pickle.load(file)
python_code = '\n'.join(pyqt_generator.generate_pyqt_design(figma_file))
with open('../resources/f.py', 'w', encoding="utf-8") as file:
    file.write(python_code)
handler_code = '\n'.join(pyqt_generator.generate_handler(figma_file))
with open('GuiHandler.py', 'w', encoding="utf-8") as file:
    file.write(handler_code)
exec(python_code)
