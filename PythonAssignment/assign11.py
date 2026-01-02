import tkinter as tk

def submit_form():
    selected_option = option_var.get()
    
    if selected_option == "Instagram Ads":
        # Redirect to FAQ page for Instagram Ads
        print("Redirecting to FAQ page for Instagram Ads")
    elif selected_option == "YouTube Ads":
        # Redirect to FAQ page for YouTube Ads
        print("Redirecting to FAQ page for YouTube Ads")
    else:
        # Handle other options here
        pass

# Create the main window
window = tk.Tk()

# Set window title
window.title("Course Inquiry Form")

# Create a label for the question
question_label = tk.Label(window, text="Where did you hear about this course?")
question_label.pack()

# Create a variable to store the selected option
option_var = tk.StringVar()

# Create radio buttons for different options
instagram_ads_radio = tk.Radiobutton(window, text="Instagram Ads", variable=option_var, value="Instagram Ads")
instagram_ads_radio.pack()

youtube_ads_radio = tk.Radiobutton(window, text="YouTube Ads", variable=option_var, value="YouTube Ads")
youtube_ads_radio.pack()

# Create a button to submit the form
submit_button = tk.Button(window, text="Submit", command=submit_form)
submit_button.pack()

# Start the main window's event loop
window.mainloop()
