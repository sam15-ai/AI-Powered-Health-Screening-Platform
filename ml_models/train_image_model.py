import math
import ssl
from pathlib import Path

import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset, random_split
from torchvision import models


PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODEL_OUTPUT_PATH = PROJECT_ROOT / "ml_models" / "skin_model.pt"
IMAGE_SIZE = 224
SAMPLES_PER_CLASS = 50
EPOCHS = 5
BATCH_SIZE = 16
LEARNING_RATE = 1e-3

CLASS_NAMES = [
    "Eczema",
    "Psoriasis",
    "Melanoma Risk",
    "Acne",
    "Normal Skin",
]

CLASS_TINTS = {
    "Eczema": torch.tensor([0.85, 0.55, 0.50]).view(3, 1, 1),
    "Psoriasis": torch.tensor([0.90, 0.75, 0.75]).view(3, 1, 1),
    "Melanoma Risk": torch.tensor([0.35, 0.25, 0.20]).view(3, 1, 1),
    "Acne": torch.tensor([0.95, 0.65, 0.60]).view(3, 1, 1),
    "Normal Skin": torch.tensor([0.80, 0.72, 0.65]).view(3, 1, 1),
}


def build_synthetic_dataset():
    images = []
    labels = []

    for class_index, class_name in enumerate(CLASS_NAMES):
        tint = CLASS_TINTS[class_name]
        for _ in range(SAMPLES_PER_CLASS):
            base = torch.rand(3, IMAGE_SIZE, IMAGE_SIZE) * 0.35
            patterned_noise = torch.sin(torch.linspace(0, math.pi * 4, IMAGE_SIZE)).view(1, 1, IMAGE_SIZE)
            patterned_noise = patterned_noise.repeat(3, IMAGE_SIZE, 1) * 0.05
            image = torch.clamp(base + tint + patterned_noise, 0.0, 1.0)
            images.append(image)
            labels.append(class_index)

    return torch.stack(images), torch.tensor(labels, dtype=torch.long)


def build_model():
    # Replace with real dermatology dataset (e.g. ISIC) for production use
    ssl._create_default_https_context = ssl._create_unverified_context
    weights = models.ResNet18_Weights.DEFAULT
    model = models.resnet18(weights=weights)
    model.fc = nn.Linear(model.fc.in_features, len(CLASS_NAMES))
    return model


def main():
    images, labels = build_synthetic_dataset()
    dataset = TensorDataset(images, labels)

    train_size = int(0.8 * len(dataset))
    val_size = len(dataset) - train_size
    train_dataset, val_dataset = random_split(
        dataset,
        [train_size, val_size],
        generator=torch.Generator().manual_seed(42),
    )

    train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE)

    model = build_model()
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=LEARNING_RATE)

    for epoch in range(EPOCHS):
        model.train()
        running_loss = 0.0

        for batch_images, batch_labels in train_loader:
            optimizer.zero_grad()
            outputs = model(batch_images)
            loss = criterion(outputs, batch_labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()

        model.eval()
        correct = 0
        total = 0
        with torch.no_grad():
            for batch_images, batch_labels in val_loader:
                outputs = model(batch_images)
                predictions = torch.argmax(outputs, dim=1)
                total += batch_labels.size(0)
                correct += (predictions == batch_labels).sum().item()

        accuracy = correct / total if total else 0.0
        avg_loss = running_loss / max(len(train_loader), 1)
        print(f"Epoch {epoch + 1}/{EPOCHS} - loss: {avg_loss:.4f} - val_acc: {accuracy:.4f}")

    MODEL_OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    torch.save(model.state_dict(), MODEL_OUTPUT_PATH)
    print(f"Saved model to {MODEL_OUTPUT_PATH}")


if __name__ == "__main__":
    main()
