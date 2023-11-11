from openai import OpenAI

from gpt4_vision_playground.config import get_openai_key

OPENAI_CLIENT = OpenAI(api_key=get_openai_key())

response = OPENAI_CLIENT.images.generate(
    model="dall-e-3",
    prompt="Przygotuj obraz ulicy po której idą ludzie (max 5 osób).",
    size="1024x1024",
    quality="hd",
    style="natural",
    n=1,
)

image_url = response.data[0].url

print(image_url)
