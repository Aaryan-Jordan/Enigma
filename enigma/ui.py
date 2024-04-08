import tkinter as tk
import json
import time
import threading

def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
def update_text_widget(text_widget, file_path):
    while True:
        text_widget.delete('1.0', tk.END)
        content = load_json_file(file_path)
        text_widget.insert(tk.END, json.dumps(content, indent=4))
        time.sleep(1)
window = tk.Tk()
window.aspect(16, 10, 16, 10)
text_widget = tk.Text(window)
text_widget.config(bg='black')
text_widget.config(fg='white')
text_widget.config(font=('Courier', 12))
text_widget.pack()
threading.Thread(target=update_text_widget, args=(text_widget, 'history.json')).start()
window.mainloop()
