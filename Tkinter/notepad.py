import tkinter as tk
from tkinter import ttk, filedialog, messagebox, font
class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Untitled - Python Notepad")
        self.root.geometry("800x600")
        self.current_file = None
        self.create_menu()
        self.create_toolbar()
        self.create_editor()
        self.create_statusbar()
        self.bind_shortcuts()
    def create_menu(self):
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
        file_menu.add_command(label="Open...", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_command(label="Save As...", command=self.save_as_file, accelerator="Ctrl+Shift+S")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Undo", command=lambda: self.text_area.event_generate("<<Undo>>"), accelerator="Ctrl+Z")
        edit_menu.add_command(label="Redo", command=lambda: self.text_area.event_generate("<<Redo>>"), accelerator="Ctrl+Y")
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=lambda: self.text_area.event_generate("<<Cut>>"), accelerator="Ctrl+X")
        edit_menu.add_command(label="Copy", command=lambda: self.text_area.event_generate("<<Copy>>"), accelerator="Ctrl+C")
        edit_menu.add_command(label="Paste", command=lambda: self.text_area.event_generate("<<Paste>>"), accelerator="Ctrl+V")
        edit_menu.add_separator()
        edit_menu.add_command(label="Select All", command=self.select_all, accelerator="Ctrl+A")
        menubar.add_cascade(label="Edit", menu=edit_menu)
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About Notepad", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)
        self.root.config(menu=menubar)
    def create_toolbar(self):
        toolbar = ttk.Frame(self.root, padding=3)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        self.font_family = tk.StringVar(value="Segoe UI")
        fonts = sorted(list(font.families()))
        font_box = ttk.Combobox(toolbar, textvariable=self.font_family, values=fonts, state="readonly", width=18)
        font_box.pack(side=tk.LEFT, padx=2)
        font_box.bind("<<ComboboxSelected>>", self.update_font)
        self.font_size = tk.IntVar(value=12)
        size_box = ttk.Combobox(toolbar, textvariable=self.font_size, values=list(range(8, 40, 2)), state="readonly", width=5)
        size_box.pack(side=tk.LEFT, padx=2)
        size_box.bind("<<ComboboxSelected>>", self.update_font)
        ttk.Button(toolbar, text="New", command=self.new_file, width=6).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="Open", command=self.open_file, width=6).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="Save", command=self.save_file, width=6).pack(side=tk.LEFT, padx=2)
    def create_editor(self):
        editor_frame = ttk.Frame(self.root)
        editor_frame.pack(fill=tk.BOTH, expand=True)
        scrollbar = ttk.Scrollbar(editor_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_area = tk.Text(
            editor_frame,
            undo=True,
            wrap="word",
            yscrollcommand=scrollbar.set,
            padx=10,
            pady=10,
            font=("Segoe UI", 12)
        )
        self.text_area.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.text_area.yview)
        self.text_area.bind("<<Modified>>", self.update_status)
        self.text_area.bind("<KeyRelease>", self.update_status)
        self.text_area.bind("<ButtonRelease-1>", self.update_status)
    def create_statusbar(self):
        self.status_bar = ttk.Label(self.root, text="Line 1, Column 1 | 0 characters", anchor="e", padding=4)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    def bind_shortcuts(self):
        self.root.bind("<Control-n>", lambda e: self.new_file())
        self.root.bind("<Control-o>", lambda e: self.open_file())
        self.root.bind("<Control-s>", lambda e: self.save_file())
        self.root.bind("<Control-S>", lambda e: self.save_as_file())
        self.root.bind("<Control-a>", lambda e: self.select_all())
    def new_file(self):
        self.text_area.delete("1.0", tk.END)
        self.current_file = None
        self.root.title("Untitled - Python Notepad")
    def open_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert("1.0", content)
            self.current_file = file_path
            self.root.title(f"{file_path} - Python Notepad")
    def save_file(self):
        if self.current_file:
            with open(self.current_file, "w", encoding="utf-8") as f:
                f.write(self.text_area.get("1.0", tk.END + "-1c"))
        else:
            self.save_as_file()
    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(self.text_area.get("1.0", tk.END + "-1c"))
            self.current_file = file_path
            self.root.title(f"{file_path} - Python Notepad")
    def select_all(self):
        self.text_area.tag_add("sel", "1.0", "end")
        return "break"
    def update_font(self, event=None):
        new_font = (self.font_family.get(), self.font_size.get())
        self.text_area.config(font=new_font)
    def update_status(self, event=None):
        cursor_pos = self.text_area.index(tk.INSERT)
        line, col = cursor_pos.split('.')
        text = self.text_area.get("1.0", tk.END + "-1c")
        char_count = len(text)
        self.status_bar.config(text=f"Line {line}, Column {int(col) + 1} | {char_count} characters")
    def show_about(self):
        messagebox.showinfo("About Notepad", "Simple Python Notepad built using Tkinter.")
if __name__ == "__main__":
    root = tk.Tk()
    app = Notepad(root)
    root.mainloop()