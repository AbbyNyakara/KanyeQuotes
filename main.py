import requests
from tkinter import *

# Retrieve the data from the kanye API
# Functions
def generate_quote():
    """Retrieves quote from Kanye Api and prints to canvas"""
    response = requests.get("https://api.kanye.rest")
    data = response.json()  # Change to json format - like a dictionary
    quote = data["quote"]
    # print(quote)
    canvas.itemconfig(quote_text, text=quote)


# Use Tkinter to put that quote into a GUI
window = Tk()
window.config(padx=20, pady=20)
window.title("Kanye Quotes")

canvas = Canvas(width=300, height=414)
image = PhotoImage(file="background.png")
canvas.create_image(150, 215, image=image)
quote_text = canvas.create_text(150, 180, width=280, text="Click button \n to Generate Quote",
                                font=("Helvetica", 20, "bold"))
canvas.grid(column=0, row=0)

button_image = PhotoImage(file="kanye.png")
kanye_button = Button(image=button_image, command=generate_quote)
kanye_button.grid(column=0, row=1)

window.mainloop()
# Debugging: Make the text to fit in the canvas
