import base64
from pathlib import Path
from typing import Dict, Any


def encode_image(image_path: Path) -> str:
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def get_image_media_type(image_path: Path) -> str:
    extension = image_path.suffix
    return f'image/{extension}'


def system_message(content: str) -> Dict[str, Any]:
    return {
        "role": "system",
        "content": [
            {"type": "text", "text": content}
        ]
    }


def user_message(content: str) -> Dict[str, Any]:
    return {
        "role": "user",
        "content": [
            {"type": "text", "text": content}
        ]
    }


def user_message_with_image(content: str, image_file: Path) -> Dict[str, Any]:
    base64_image = encode_image(image_file)
    image_media_type = get_image_media_type(image_file)
    return {
        "role": "user",
        "content": [
            {"type": "text", "text": content},
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:{image_media_type};base64,{base64_image}"
                }
            }
        ]
    }
