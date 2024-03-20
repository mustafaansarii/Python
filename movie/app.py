import pickle
with open('ml_instance.pkl', 'rb') as file:
    loaded_obj = pickle.load(file)
loaded_obj.recommend('avatar')