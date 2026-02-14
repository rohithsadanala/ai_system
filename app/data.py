import json
import numpy as np
import os

def load_task(task_id, data_path="data/training"):
    with open(f'{data_path}/{task_id}.json') as f:
        data = json.load(f)

    train_data = [np.array(pair['input']) for pair in data['train']]
    train_output = [np.array(pair['output']) for pair in data['train']]
    train_input = [np.array(pair['input']) for pair in data['test']]

    return train_data, train_output, train_input