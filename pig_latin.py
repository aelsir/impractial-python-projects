"Change English names to Spanish names"

import random
english_names = (
    'Apple', 'Banana', 'Carrot', 'Dog', 'Elephant', 'Fish', 'Giraffe', 'Horse', 'Ice Cream', 'Jacket',
    'Kangaroo', 'Lemon', 'Monkey', 'Noodles', 'Orange', 'Penguin', 'Quilt', 'Rabbit', 'Strawberry', 'Tiger',
    'Umbrella', 'Violin', 'Watermelon', 'Xylophone', 'Yogurt', 'Zebra', 'Ant', 'Bear', 'Cat', 'Dolphin',
    'Eagle', 'Flower', 'Guitar', 'Hamburger', 'Igloo', 'Jellyfish', 'Kite', 'Lion', 'Mango', 'Nest',
    'Owl', 'Pineapple', 'Queen', 'Rose', 'Sun', 'Tree', 'Unicorn', 'Vegetable', 'Whale', 'X-ray',
    'Yo-yo', 'Zoo'
)

english_name = random.choice(english_names)

def spanishized(name_to_spanish):
    "Accepting english name and spanishing it using Pig Latin method"
    vowels =  ('a', 'e', 'u', 'o', 'i')
    if name_to_spanish[0].lower() not in vowels:
        spanishized_name = name_to_spanish[1:] + name_to_spanish[0] + 'ay'
        spanishized_name = spanishized_name.capitalize()

    else:
        spanishized_name = name_to_spanish + 'way'

    return spanishized_name

print(f"{english_name} is converted to:")
print(f"\033[91m{spanishized(english_name)}\033[0m")
