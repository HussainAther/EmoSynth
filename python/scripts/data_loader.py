import numpy as np

def load_data(filepath):
    data = np.load(filepath)
    return data

if __name__ == "__main__":
    filepath = "path/to/your/dataset.npy"
    data = load_data(filepath)
    print(data.shape)

