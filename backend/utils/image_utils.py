from pathlib import Path

from PIL import Image
from torchvision import transforms


IMAGENET_MEAN = [0.485, 0.456, 0.406]
IMAGENET_STD = [0.229, 0.224, 0.225]

IMAGE_TRANSFORM = transforms.Compose(
    [
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=IMAGENET_MEAN, std=IMAGENET_STD),
    ]
)


def save_upload_file(upload_file, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("wb") as output_file:
        while True:
            chunk = upload_file.file.read(1024 * 1024)
            if not chunk:
                break
            output_file.write(chunk)


def preprocess_image(image_path: Path):
    image = Image.open(image_path).convert("RGB")
    tensor = IMAGE_TRANSFORM(image)
    return tensor.unsqueeze(0)
