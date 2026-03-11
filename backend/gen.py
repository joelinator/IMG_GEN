# aProject/backend/app.py
import fal_client
import os

from dotenv import load_dotenv


load_dotenv()

log_path="./logs/rec.txt"

api_url=os.getenv("fal_url")
def func(update):
    if isinstance(update, fal_client.InProgress):
        logs=[]
        for log in update.logs:
            logs.append(log["message"])
            #print(log["message"])
        with open(log_path, "w") as f:
            f.write("\n".join(logs))
default_n = os.getenv("n_images", 2)
def generateImage(prompt, n_images=default_n):
    result =  fal_client.subscribe(
        api_url, arguments = {
            "prompt":prompt,
            "image_size":"landscape_4_3",
            "num_images":n_images,
            "enable_safety_checker": True,
            "output_format":"jpeg",
            "safety_tolerance":"2"},
        with_logs = True,
        on_queue_update = func
        )
    # print(type(result))
    image_urls = [el['url'] for el in result['images']]
    return {"data": image_urls} 


