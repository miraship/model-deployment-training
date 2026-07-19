import joblib as jb
model = jb.load("model.pkl")


def predict(age, salary, gender):
    output = model.predict([[age, salary, gender]])
    if output[0] == 1:
        return "Purchased"
    return "Not Purchased"