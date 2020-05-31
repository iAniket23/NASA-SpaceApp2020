"""
Author: James Schaefer-Pham

.h5 file reader

Assumes that all datasets contain array like elements. This program is designed to read data
from NASA's VNP46 product suite for analysis in the Spaceapps COVID-19 challenge. Converts datasets
into numpy Array objects.

Terminal uses spaces as a delimiter

Terminal Commands
-----------------
cd [dir]    - change directory
cd.         - go to parent directory
ls          - gives info about current directory; list elements
path        - gives path
dir         - gives current directory
data [src]  - converts data from source into a numpy array
quit        - exit shell
"""
import h5py
import numpy

class Terminal:

    def __init__(self, read_file):
        self.path = [read_file]

    def cd_fwd(self, dir):
        self.path.append(self.path[len(self.path)-1][dir])
        
    def cd_bck(self):
        self.path.pop()

    def ls(self):
        print(self.path[len(self.path)-1])

        for key in list(self.path[len(self.path)-1].keys()):
            print(key)

        return self.path[len(self.path)-1].keys()

    def path(self):
        print(self.path)
        return self.path

    def dir(self):
        print(self.path[len(self.path)-1])
        return self.path[len(self.path)-1]

    def read_data(self, dataset):
        # Returns numpy array containing the data from source
        
        array = None

        try:
            dataset = self.path[len(self.path)-1][dataset]
            datatype = dataset.dtype
            shape = dataset.shape

            array = numpy.empty(shape, dtype=datatype)
            dataset.read_direct(array)

            print(array)
            return array

        except Exception:
            print("Error")
            return

    def shell(self):
        run = True
        while run:

            terminal_input = input(str(self.path) + " >>> ").strip()
            commands = terminal_input.split(maxsplit=1)

            if commands[0] == 'cd':
                self.cd_fwd(commands[1])

            elif commands[0] == 'cd.':
                self.cd_bck()

            elif commands[0] == 'ls':
                self.ls()

            elif commands[0] == 'path':
                self.path()

            elif commands[0] == 'dir':
                self.dir()

            elif commands[0] == 'data':
                self.read_data(commands[1])
            
            elif commands[0] == 'quit':
                run = False

            else:
                print("Unknown command " + commands[0])

            print()

        print("Shell Closed")

if __name__ == "__main__":

    filename = 'VNP46A1.A2020017.h00v08.001.2020053010251.h5'
    file = h5py.File(filename, "r")

    terminal = Terminal(file)
    terminal.shell()
    del terminal
