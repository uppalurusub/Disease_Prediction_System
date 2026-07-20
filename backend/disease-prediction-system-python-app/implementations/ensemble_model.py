from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier

def build_ensemble():

    model = VotingClassifier(
        estimators=[
            ("lr", LogisticRegression()),
            ("rf", RandomForestClassifier()),
            ("svm", SVC(probability=True)),
            ("xgb", XGBClassifier())
        ],
        voting="soft"
    )

    return model