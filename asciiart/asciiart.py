import requests
import random

# Function that gets ascii art from the endpoint using the requested text and font
def getASCII(text, font):
    # If font is empty use default else use given font
    if font == "":
        r = requests.get(f'http://artii.herokuapp.com/make?text={text}')
    else:
        r = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}')
    # Displat font
    print("Font:", font)
    # Display Art
    print(r.text)

# Get user input for text
text = input('ASCII Art Text > ')
# Get user input for the font
font = input('ASCII Art Font > ')

# Check if font is set to random or not
if font.lower() != 'random':
  getASCII(text, font)
elif font == "random":
  # Get fonts from endpoing
  data = requests.get('http://artii.herokuapp.com/fonts_list')
  # Split fonts by newline
  fontsArray = data.text.split('\n')

  for i in range(3):
      font = random.choice(fontsArray)
      getASCII(text, font)
