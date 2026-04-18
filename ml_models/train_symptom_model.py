import pickle
import random
from pathlib import Path

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer


PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODEL_OUTPUT_PATH = PROJECT_ROOT / "ml_models" / "symptom_model.pkl"
MLB_OUTPUT_PATH = PROJECT_ROOT / "ml_models" / "mlb.pkl"

random.seed(42)

CONDITION_PROFILES = {
    "Flu": {
        "core": ["fever", "cough", "fatigue"],
        "optional": ["body ache", "chills", "sore throat", "headache"],
    },
    "Cardiac concern": {
        "core": ["chest pain", "shortness of breath"],
        "optional": ["dizziness", "sweating", "arm pain", "palpitations"],
    },
    "Migraine": {
        "core": ["headache", "nausea", "light sensitivity"],
        "optional": ["vomiting", "blurred vision", "dizziness"],
    },
    "Diabetes risk": {
        "core": ["frequent urination", "excessive thirst"],
        "optional": ["fatigue", "blurred vision", "weight loss"],
    },
    "Arthritis": {
        "core": ["joint pain", "swelling"],
        "optional": ["stiffness", "reduced mobility", "fatigue"],
    },
    "Dermatitis": {
        "core": ["skin rash", "itching"],
        "optional": ["redness", "dry skin", "irritation"],
    },
    "IBS": {
        "core": ["abdominal pain", "bloating"],
        "optional": ["constipation", "diarrhea", "cramps", "gas"],
    },
    "Common Cold": {
        "core": ["sore throat", "runny nose"],
        "optional": ["cough", "sneezing", "mild fever", "congestion"],
    },
    "Musculoskeletal": {
        "core": ["back pain", "stiffness"],
        "optional": ["muscle spasm", "limited mobility", "joint pain"],
    },
    "Mental Health concern": {
        "core": ["anxiety", "insomnia", "fatigue"],
        "optional": ["poor concentration", "restlessness", "low mood"],
    },
}

NOISE_SYMPTOMS = [
    "headache",
    "fatigue",
    "mild fever",
    "dizziness",
    "nausea",
    "cough",
    "body ache",
    "poor appetite",
]


def build_dataset(samples_per_condition: int = 35):
    symptom_samples: list[list[str]] = []
    labels: list[str] = []

    for condition, profile in CONDITION_PROFILES.items():
        for _ in range(samples_per_condition):
            sample = set(profile["core"])

            optional_count = random.randint(1, min(3, len(profile["optional"])))
            sample.update(random.sample(profile["optional"], optional_count))

            if random.random() < 0.35:
                sample.update(random.sample(NOISE_SYMPTOMS, random.randint(1, 2)))

            if condition == "Common Cold" and random.random() < 0.4:
                sample.add("headache")
            if condition == "Flu" and random.random() < 0.5:
                sample.add("sore throat")
            if condition == "Cardiac concern" and random.random() < 0.4:
                sample.add("fatigue")

            symptom_samples.append(sorted(sample))
            labels.append(condition)

    return symptom_samples, labels


def main():
    symptom_samples, labels = build_dataset()

    mlb = MultiLabelBinarizer()
    features = mlb.fit_transform(symptom_samples)

    x_train, x_test, y_train, y_test = train_test_split(
        features,
        labels,
        test_size=0.2,
        random_state=42,
        stratify=labels,
    )

    model = RandomForestClassifier(
        n_estimators=300,
        random_state=42,
        class_weight="balanced",
    )
    model.fit(x_train, y_train)

    predictions = model.predict(x_test)
    accuracy = accuracy_score(y_test, predictions)

    with MODEL_OUTPUT_PATH.open("wb") as model_file:
        pickle.dump(model, model_file)

    with MLB_OUTPUT_PATH.open("wb") as mlb_file:
        pickle.dump(mlb, mlb_file)

    print(f"Accuracy: {accuracy:.4f}")


if __name__ == "__main__":
    main()
