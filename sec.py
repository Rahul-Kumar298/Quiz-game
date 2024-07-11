import tkinter as tk
from tkinter import messagebox

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.name = None
        self.score = 0
        self.current_question = 0
        self.selected_language = None

        self.languages = ["Python", "Java", "C++", "C", "JavaScript", "Ruby", "PHP", "HTML", "CSS", "SQL"]
        self.quiz_modules = {
            "python": "python",
            "java": "java",
            "cpp": "cpp",
            "c": "c",
            "javascript": "js",
            "ruby": "ruby",
            "php": "php",
            "html": "html",
            "css": "css",
            "sql": "sql"
        }

        self.create_widgets()

    def create_widgets(self):
        self.name_label = tk.Label(self.root, text="Enter your name:")
        self.name_label.pack()        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()
        self.name_button = tk.Button(self.root, text="Submit", command=self.get_name)
        self.name_button.pack()

    def get_name(self):
        self.name = self.name_entry.get()
        if not self.name:
            messagebox.showwarning("Warning", "Please enter your name")
            return
        self.name_label.pack_forget()
        self.name_entry.pack_forget()
        self.name_button.pack_forget()
        self.show_language_options()

    def show_language_options(self):
        self.lang_label = tk.Label(self.root, text="Select the language you want to play quiz on it:")
        self.lang_label.pack()
        self.lang_var = tk.StringVar(value="1")
        for i, lang in enumerate(self.languages, 1):
            rb = tk.Radiobutton(self.root, text=lang, variable=self.lang_var, value=str(i))
            rb.pack(anchor=tk.W)
        self.lang_button = tk.Button(self.root, text="Submit", command=self.select_language)
        self.lang_button.pack()

    def select_language(self):
        lang_index = int(self.lang_var.get()) - 1
        self.selected_language = self.languages[lang_index].lower()
        if self.selected_language not in self.quiz_modules:
            messagebox.showerror("Error", "Selected language not supported.")
            return

        self.lang_label.pack_forget()
        self.lang_button.pack_forget()

        quiz_module = self.quiz_modules[self.selected_language]
        self.quiz_data = getattr(__import__(quiz_module), quiz_module)

        self.show_question()

    def show_question(self):
        if self.current_question < len(self.quiz_data):
            question = self.quiz_data[self.current_question]
            self.question_label = tk.Label(self.root, text=question["question"])
            self.question_label.pack()

            self.answer_var = tk.StringVar(value="")
            for option, text in question["options"].items():
                rb = tk.Radiobutton(self.root, text=text, variable=self.answer_var, value=option)
                rb.pack(anchor=tk.W)
            self.answer_button = tk.Button(self.root, text="Submit", command=self.check_answer)
            self.answer_button.pack()
        else:
            self.show_result()

    def check_answer(self):
        selected_answer = self.answer_var.get()
        correct_answer = self.quiz_data[self.current_question]["answer"]

        if selected_answer == correct_answer:
            self.score += 1

        self.current_question += 1
        self.question_label.pack_forget()
        self.answer_button.pack_forget()
        for widget in self.root.pack_slaves():
            if isinstance(widget, tk.Radiobutton):
                widget.pack_forget()

        self.show_question()

    def show_result(self):
        result_text = f"{self.name}, your total score is {self.score}/{len(self.quiz_data)}. Well done!"
        self.result_label = tk.Label(self.root, text=result_text)
        self.result_label.pack()

if __name__ == "__main__":
    import python  # replace with actual import statements for each language
    import java
    import cpp
    import c
    import js
    import ruby
    import php
    import html
    import css
    import sql

    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()
