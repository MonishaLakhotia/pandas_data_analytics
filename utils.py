from sklearn import preprocessing


def get_label_encoders(columns, dataframe):
    le = preprocessing.LabelEncoder()
    labelEncoders = {}
    for c in columns:
        labelEncoders[c] = le.fit(dataframe[c])
    return labelEncoders


def label_encode_transform(labelEncoders, columns, dataframe):
    for c in columns:
        dataframe[c] = labelEncoders[c].transform(dataframe[c])


def label_encode_inverse_transform(labelEncoders, columns, dataframe):
    for c in columns:
        dataframe[c] = labelEncoders[c].inverse_transform(dataframe[c])


def foreach(action, iterable):
    for element in iterable:
        action(element)
