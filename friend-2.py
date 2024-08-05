import tkinter as tk
from tkinter import messagebox

class FriendshipDayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Friendship Day Greeting")

        # Set the background color
        self.root.configure(bg="#FFDDC1")

        # Create a frame for the content
        self.frame = tk.Frame(self.root, padx=20, pady=20, bg="#FFDDC1")
        self.frame.pack(padx=10, pady=10)

        # Create a label to display the visual
        self.label = tk.Label(
            self.frame,
            text=self.get_text_visual(),
            font=("Courier", 12, "bold"),
            justify=tk.LEFT,
            bg="#FFDDC1",
            fg="#FF69B4"
        )
        self.label.pack()

        # Create a button to show the pop-up message
        self.popup_button = tk.Button(
            self.frame,
            text="Show Friendship Day Message",
            command=self.show_message,
            bg="#FF69B4",
            fg="white",
            font=("Arial", 12, "bold")
        )
        self.popup_button.pack(pady=10)

        # Create a button to exit the application
        self.exit_button = tk.Button(
            self.frame,
            text="Exit",
            command=self.root.quit,
            bg="#FF69B4",
            fg="white",
            font=("Arial", 12, "bold")
        )
        self.exit_button.pack(pady=10)

    def get_text_visual(self):
        # Define the visual text for Friendship Day
        visual = """
        ******************************************
        *                                        *
        *     🌟 Happy Friendship Day! 🌟         *
        *                                        *
        *  🌼 Friends are the family we choose. 🌼 *
        *                                        *
        *   🎉 Celebrate the joy of friendship! 🎉  *
        *                                        *
        ******************************************
        """
        return visual

    def show_message(self):
        # Show a pop-up message
        messagebox.showinfo("Friendship Day", "🌟 Happy Friendship Day! 🌟\n\nThank you for being a wonderful friend! 🎉")

def main():
    root = tk.Tk()
    app = FriendshipDayApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
