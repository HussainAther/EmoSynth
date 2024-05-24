import numpy as np

def preprocess_data(data):
    processed_data = (data - np.mean(data)) / np.std(data)
    return processed_data

if __name__ == "__main__":
    raw_data = np.random.rand(100, 10)
    processed_data = preprocess_data(raw_data)
    print(processed_data.shape)

