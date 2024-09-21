import pickle


def dictionary_data(dictionary_data, file_path):
    with open(file_path, "wb") as file:
        pickle.dump(dictionary_data, file)


def load_dict(file_path):
    with open(file_path, "rb") as file:
        return pickle.load(file)


dictt = {"laptop": "apple,dell,lenovo,acer"}

dictionary_data(dictt, "dictt.pickle")


print(load_dict("dictt.pickle"))
