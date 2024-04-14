import joblib
loaded_greet = joblib.load('greet.joblib')

# Test the deserialized function
print(loaded_greet("John"))