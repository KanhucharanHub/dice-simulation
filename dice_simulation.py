import tkinter as tk
from PIL import Image, ImageTk
import random
from tkinter import filedialog, messagebox

class DiceSimulation:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Simulation by Karan")
        self.root.geometry("600x600")
        self.root.configure(bg='#282c34')

        self.image_size = (100, 100)  # Set the desired size for dice images
        self.dice_images = [f'dice{i}.png' for i in range(1, 7)]
        self.current_image = None

        self.label = tk.Label(self.root, text="Roll the Dice!", font=("Helvetica", 24), fg='white', bg='#282c34')
        self.label.pack(pady=20)

        self.dice_label = tk.Label(self.root, bg='#282c34')
        self.dice_label.pack(pady=20)

        self.roll_button = tk.Button(self.root, text="Roll Dice", command=self.roll_dice, font=("Helvetica", 16), bg='#61dafb', fg='black')
        self.roll_button.pack(pady=20)

        self.history = []
        self.history_label = tk.Label(self.root, text="Roll History:", font=("Helvetica", 14), fg='white', bg='#282c34')
        self.history_label.pack(pady=10)
        self.history_text = tk.Text(self.root, height=5, width=50, bg='#282c34', fg='white')
        self.history_text.pack(pady=10)

        self.stats_label = tk.Label(self.root, text="Roll Statistics:", font=("Helvetica", 14), fg='white', bg='#282c34')
        self.stats_label.pack(pady=10)
        self.stats_text = tk.Text(self.root, height=5, width=50, bg='#282c34', fg='white')
        self.stats_text.pack(pady=10)

    def roll_dice(self):
        for _ in range(10):  # Simulate rolling animation
            dice_number = random.randint(1, 6)
            dice_image_path = self.dice_images[dice_number - 1]
            img = Image.open(dice_image_path).resize(self.image_size, Image.LANCZOS)
            self.current_image = ImageTk.PhotoImage(img)
            self.dice_label.config(image=self.current_image)
            self.root.update_idletasks()
            self.root.after(100)  # Delay to create animation effect

        final_number = random.randint(1, 6)
        dice_image_path = self.dice_images[final_number - 1]
        img = Image.open(dice_image_path).resize(self.image_size, Image.LANCZOS)
        self.current_image = ImageTk.PhotoImage(img)
        self.dice_label.config(image=self.current_image)
        self.history.append(final_number)
        self.update_history()
        self.update_statistics()

    def update_history(self):
        self.history_text.delete(1.0, tk.END)
        self.history_text.insert(tk.END, ', '.join(map(str, self.history)))

    def update_statistics(self):
        roll_count = len(self.history)
        if roll_count > 0:
            stats = {i: self.history.count(i) for i in range(1, 7)}
            stats_text = "\n".join([f"{i}: {count} times ({count/roll_count:.2%})" for i, count in stats.items()])
            self.stats_text.delete(1.0, tk.END)
            self.stats_text.insert(tk.END, stats_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = DiceSimulation(root)
    root.mainloop()
