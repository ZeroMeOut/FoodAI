import os
import openai
import random
from clarifaicheck import *
from foodnotfoodcheck import *
from keys import keys

os.environ["http_proxy"] = "127.0.0.1:7890"  # you may need to change this according to ya proxy
os.environ["https_proxy"] = "127.0.0.1:7890"  # same with this
openai.api_key = keys['Open_api']

image_path = "img3.jpg"

check1 = foodnotfood(image_path)

personalities = ["a gen-z person", "Gordon ramsay", "a playful anime girl", "a drunk american"]
random_number = random.randint(0, 3)

if check1 == "not_food":
    completion1 = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are speaking like {personalities[random_number]}."},
            {"role": "user", "content": "I just sent you a picture that is not a food. Come up with a playful jab "
                                        "that what I sent you isn't a food and I should do better"}
        ]
    )

    print(f"{personalities[random_number]} \n{completion1.choices[0].message.content}")
else:
    check2 = clarifai(image_path)
    completion2 = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are speaking like {personalities[random_number]}. "
                                          f"Guess the food based of the user input then speak on it. Be like I guess "
                                          f"what I'm seeing is blabla based on your input and then give more details "
                                          f"with about a hundred words"},
            {"role": "user", "content": check2}
        ]
    )

    print(f"{personalities[random_number]} \n{completion2.choices[0].message.content}")
