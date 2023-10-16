import time
import tkinter as tk
import subprocess
import threading
import webbrowser


# This is where i can run the server logic code for the table and then when i click on the side bar it will open the 
# webiste that i laoded it at


# ALL CHAT GPT GENREATED NEED TO REDO

def run_script_1():
    run_button_1.config(state=tk.DISABLED)  # Disable the button
    script_file_path = "init.py"
    
    def execute_script():
        try:
            result = subprocess.check_output(["python3", script_file_path], universal_newlines=True)
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, result)
        except subprocess.CalledProcessError as e:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, f"Error: {e}")
        run_button_1.config(state=tk.NORMAL)  # Re-enable the button after execution
   
    script_thread = threading.Thread(target=execute_script)
    script_thread.start()

    time.sleep(1)

    webbrowser.open("http://127.0.0.1:5026")
    
    


app = tk.Tk()
app.title("Script Runner")

script_entry = tk.Entry(app, width=40)
script_entry.pack(pady=5)

run_button_1 = tk.Button(app, text="Open Website", command=run_script_1)
run_button_1.pack(pady=10)

result_text = tk.Text(app, height=10, width=40)
result_text.pack()

app.mainloop()
