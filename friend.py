import tkinter as tk

class FriendshipDayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Friendship Day Greeting")

        # Create a frame for the content
        self.frame = tk.Frame(self.root, padx=20, pady=20)
        self.frame.pack(padx=10, pady=10)

        # Create a label to display the visual
        self.label = tk.Label(self.frame, text=self.get_text_visual(), font=("Courier", 12), justify=tk.LEFT)
        self.label.pack()

        # Create a button to exit the application
        self.exit_button = tk.Button(self.frame, text="Exit", command=self.root.quit)
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

def main():
    root = tk.Tk()
    app = FriendshipDayApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
