import pickle

def load_model(path):
    with open(path, 'rb') as file:
        return pickle.load(file)


def predict(model, input_data):
    return model.predict_proba(input_data)
