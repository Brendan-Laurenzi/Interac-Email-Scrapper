import tkinter
import tkinter.messagebox
import customtkinter
import database as db
import scrape
from CTkTable import *

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

def get_table_data():
    table_data = db.Database.get_all_emt_data()
    table_data.insert(0, ["Name","Amount","Memo","Date","Ref_ID"])
    return table_data

class App(customtkinter.CTk):

    table_data = get_table_data()

    def __init__(self):
        super().__init__()

        self.title("EMT MANAGER")
        self.geometry(f"{920}x{580}")

        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure((0,1,4), weight=0)
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

        self.update_button = customtkinter.CTkButton(self, text="UPDATE", width=70, command=self.update_button_event)
        self.update_button.grid(row=0, column=1, padx=(10,0), pady=(10,0))

        self.search_entry = customtkinter.CTkEntry(self, placeholder_text="Description")
        self.search_entry.grid(row=0, column=2, padx=10, pady=(10,0), sticky="nsew")
        self.search_button = customtkinter.CTkButton(master=self, text="Search", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.search_button.grid(row=0, column=3, padx=(0,10), pady=(10,0), sticky="nsew")

        # Table Data

        self.data_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.data_frame.grid(row=1, column=1, columnspan=3, padx=10, pady=10, sticky="nsew")

        self.emt_table = CTkTable(master=self.data_frame, corner_radius=0, row=25, column=5, values=App.table_data)
        self.emt_table.grid(row=2, column=1, columnspan=3, sticky="nsew")

    def sidebar_button_event(self):
        print("sidebar_button click")

    def search_button_event(self):
        print("sidebar_button click")

    def update_button_event(self):
        db.Database.insert_data_list(scrape.emtEmail.get_email_data())
        App.table_data = get_table_data()
        self.emt_table.update_values = App.table_data

if __name__ == "__main__":
    app = App()
    app.mainloop()