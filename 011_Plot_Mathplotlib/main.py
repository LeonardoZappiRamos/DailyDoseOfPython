import os
import matplotlib.pyplot as plt

FILES_PATH = os.path.join(os.path.dirname(__file__), 'files') 
OUTPUT_PATH = os.path.join(os.path.dirname(__file__))

if __name__ == '__main__':
    files = os.listdir(FILES_PATH)
    filenames = [file.split('.')[0] for file in files]
    numbers = [float(open(os.path.join(FILES_PATH,file),'r').read()) for file in files]
    
    fig, ax = plt.subplots()
    
    ax.plot(filenames, numbers)
    
    fig.savefig(os.path.join(OUTPUT_PATH,'sample.png'))