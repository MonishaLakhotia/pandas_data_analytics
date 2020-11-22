from tpot import TPOTRegressor
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split

# config file /home/manyu/.config/virtualenv/virtualenv.ini missing (change via env var VIRTUALENV_CONFIG_FILE)


def main():
    print("hi")

    housing = load_boston()
    print(housing)
    # print([1, 2, 3, 4][:-1])
    X_train, X_test, y_train, y_test = train_test_split(housing.data, housing.target,
                                                        train_size=0.75, test_size=0.25, random_state=42)

    # tpot = TPOTRegressor(generations=5, population_size=50,
    #                      verbosity=2, random_state=42)
    # tpot.fit(X_train, y_train)
    # print(tpot.score(X_test, y_test))
    # tpot.export('tpot_boston_pipeline.py')


main()
