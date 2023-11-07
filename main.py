import tkinter
import tkinter.messagebox
import customtkinter
from CTkTable import *

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("EMT MANAGER")
        self.geometry(f"{1100}x{580}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((0,2), weight=0)
        self.grid_rowconfigure((1), weight=1)

        # Side Bar

        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=2, sticky="nsew")
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="EMT MANAGER", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.report_button = customtkinter.CTkButton(self.sidebar_frame, text="Report", command=self.sidebar_button_event)
        self.report_button.grid(row=1, column=0, padx=20, pady=10)
        self.settings_button = customtkinter.CTkButton(self.sidebar_frame, text="Settings", command=self.sidebar_button_event)
        self.settings_button.grid(row=2, column=0, padx=20, pady=10)

        # Search Bar

        self.search_frame = customtkinter.CTkFrame(self, height=35, corner_radius=0)
        self.search_frame.grid(row=0, column=1, rowspan=1, padx=10, pady=(10,0), sticky="nsew")
        self.search_entry = customtkinter.CTkEntry(self, placeholder_text="Description")
        self.search_entry.grid(row=0, column=1, padx=10, pady=(10,0), sticky="nsew")
        self.search_button = customtkinter.CTkButton(master=self, text="Search", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.search_button.grid(row=0, column=2, padx=(0,10), pady=(10,0), sticky="nsew")

        # Table Data

        self.data_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.data_frame.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.emt_table = CTkTable(master=self.data_frame, corner_radius=0, row=5, column=5, values=[["Name","Amount","Memo","Date","Ref_ID"]])
        self.emt_table.grid(row=2, column=1, columnspan=2, sticky="nsew")

    def sidebar_button_event(self):
        print("sidebar_button click")

    def search_button_event(self):
        print("sidebar_button click")

if __name__ == "__main__":
    app = App()
    app.mainloop()