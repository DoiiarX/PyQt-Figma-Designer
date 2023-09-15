import subprocess
import pathlib

if __name__ == '__main__':
    directory = (pathlib.Path(__file__).parent / 'gui_v4').absolute()
    process = subprocess.Popen(f'python gui.py',
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT,
                               cwd=directory)
    for line in process.stdout.readlines():
        print(line.decode('utf-8').strip())
