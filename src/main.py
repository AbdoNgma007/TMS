from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from __image__.__img__ import get_images
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from scripts.database import DB
import customtkinter as ctk
import matplotlib.pyplot as plt
import os

class Application:
    colorActiveTab = "#4D63FB"
    colorInActiveTab = "SystemButtonFace"
    fontTab = ("raleway normal", 16)

    def __init__(self, master):
        self.master = master
        self.master.attributes("-fullscreen", True)
        self.master.configure(fg_color="SystemButtonFace")

        self.style = ttk.Style(self.master)
        self.style.layout("custom.TNotebook", [])
        self.style.layout("custom.TNotebook.Tab", [])

        self.main_notebook = ttk.Notebook(self.master, style="custom.TNotebook")
        self.main_notebook.pack(fill=BOTH, expand=True)

        self.main_tab_login = Frame(self.main_notebook)
        self.main_tab_body = Frame(self.main_notebook)

        self.main_notebook.add(self.main_tab_login)
        self.main_notebook.add(self.main_tab_body)

        self.frame_header = Frame(self.main_tab_body, padx=40)
        self.frame_header.pack(fill=X, pady=25)

        # images
        self.images = get_images()
        self.img_logo = self.photoImage(self.images["logo"], (57, 23))
        self.img_tickets = self.photoImage(self.images["tickets"], (25, 25))
        self.img_trains = self.photoImage(self.images["trains"], (25, 25))
        self.img_users = self.photoImage(self.images["users"], (25, 25))
        self.img_companies = self.photoImage(self.images["companies"], (25, 25))
        self.img_reports = self.photoImage(self.images["reports"], (25, 25))
        self.img_dollar = self.photoImage(self.images["dollar"], (25, 25))

        self.frame_login = Frame(self.main_tab_login)
        self.frame_login.pack(expand=True)

        self.lbl_logo_login = Label(self.frame_login, bg=self.frame_login["bg"], image=self.img_logo)
        self.lbl_logo_login.pack(pady=(0, 25))

        self.ent_username = ctk.CTkEntry(self.frame_login, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                         text_color="#000", corner_radius=0, placeholder_text="username",
                                         width=300, height=35, font=("tajawal", 16))
        self.ent_username.pack(pady=(0, 15))

        self.ent_password = ctk.CTkEntry(self.frame_login, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                         text_color="#000", corner_radius=0, placeholder_text="password",
                                         width=300, height=35, font=("tajawal", 16), show="*")
        self.ent_password.pack(pady=(0, 15))

        self.btn_login = Button(self.frame_login, text="login", pady=3, bg="#4D63FB", activebackground="#4D63FB"
                                  , activeforeground="#fff", fg="#fff", bd=0,
                                  font=("tajawal", 13), command=self.login)
        self.btn_login.pack(fill=X)

        # menubar
        self.lbl_logo = Label(self.frame_header, bg=self.frame_header["bg"], image=self.img_logo)
        self.lbl_logo.pack(side=LEFT, expand=True, fill=X)

        self.frame_menu = Frame(self.frame_header, bg=self.frame_header["bg"])
        self.frame_menu.pack(side=LEFT, expand=True, fill=X)
        self.frame_center = Frame(self.frame_menu, bg=self.frame_header["bg"])
        self.frame_center.pack()

        self.btn_tab_dashboard = ctk.CTkButton(self.frame_center, fg_color=self.colorActiveTab, border_width=0,
                                               font=self.fontTab, corner_radius=100, text="Dashboard",
                                               text_color="#fff", hover=False, width=100, height=27,
                                               command=lambda: self.selectTab(0, self.btn_tab_dashboard))
        self.btn_tab_dashboard.pack(side=LEFT, padx=(0, 15))

        self.btn_tab_ticket = ctk.CTkButton(self.frame_center, fg_color=self.colorInActiveTab, border_width=0,
                                               font=self.fontTab, corner_radius=100, text="Tickets",
                                               text_color="#000", hover=False, height=27, width=100,
                                               command=lambda: self.selectTab(1, self.btn_tab_ticket))
        self.btn_tab_ticket.pack(side=LEFT, padx=(0, 15))

        self.btn_tab_train = ctk.CTkButton(self.frame_center, fg_color=self.colorInActiveTab, border_width=0,
                                            font=self.fontTab, corner_radius=100, text="Trains",
                                            text_color="#000", hover=False, height=27, width=100,
                                               command=lambda: self.selectTab(2, self.btn_tab_train))
        self.btn_tab_train.pack(side=LEFT, padx=(0, 15))

        self.btn_tab_employee = ctk.CTkButton(self.frame_center, fg_color=self.colorInActiveTab, border_width=0,
                                            font=self.fontTab, corner_radius=100, text="Employees",
                                            text_color="#000", hover=False, height=27, width=100,
                                               command=lambda: self.selectTab(3, self.btn_tab_employee))
        self.btn_tab_employee.pack(side=LEFT, padx=(0, 15))

        self.btn_tab_company = ctk.CTkButton(self.frame_center, fg_color=self.colorInActiveTab, border_width=0,
                                            font=self.fontTab, corner_radius=100, text="Companies",
                                            text_color="#000", hover=False, height=27, width=100,
                                               command=lambda: self.selectTab(4, self.btn_tab_company))
        self.btn_tab_company.pack(side=LEFT, padx=(0, 15))

        self.btn_tab_report = ctk.CTkButton(self.frame_center, fg_color=self.colorInActiveTab, border_width=0,
                                            font=self.fontTab, corner_radius=100, text="Reports",
                                            text_color="#000", hover=False, height=27, width=100,
                                               command=lambda: self.selectTab(5, self.btn_tab_report))
        self.btn_tab_report.pack(side=LEFT, padx=(0, 15))


        self.btn_exit = Button(self.frame_header, bd=0, text="exit", fg="#f00", font=("tajawal", 15),
                               activeforeground="#f00", command=self.master.destroy)
        self.btn_exit.pack(expand=True, fill=X, side=LEFT)

        self.notebook = ttk.Notebook(self.main_tab_body, style="custom.TNotebook")
        self.notebook.pack(fill=BOTH, expand=True)
        self.tab_dashboard = Frame(self.notebook, padx=100, bg="#F0F0F0")
        self.tab_ticket = Frame(self.notebook, padx=50)
        self.tab_train = Frame(self.notebook, padx=50)
        self.tab_employee = Frame(self.notebook, padx=50)
        self.tab_company = Frame(self.notebook, padx=50)
        self.tab_report = Frame(self.notebook)
        self.notebook.add(self.tab_dashboard)
        self.notebook.add(self.tab_ticket)
        self.notebook.add(self.tab_train)
        self.notebook.add(self.tab_employee)
        self.notebook.add(self.tab_company)
        self.notebook.add(self.tab_report)


        # tab dashboard
        self.frame_ds_one = Frame(self.tab_dashboard, bg=self.tab_dashboard["bg"])
        self.frame_ds_one.pack(pady=(35, 0))

        self.lbl_title_count_tickets = Label(self.frame_ds_one, text="Tickets", font=("tajawal medium", 25),
                                             fg="#fff", bg="#4D63FB", padx=10, image=self.img_tickets, compound=LEFT)
        self.lbl_title_count_tickets.grid(row=0, column=0, padx=(0, 35))
        self.lbl_count_tickets = Label(self.frame_ds_one, text="35", font=("tajawal", 20), fg="#212121")
        self.lbl_count_tickets.grid(row=1, column=0, padx=(0, 35))

        self.lbl_title_earning = Label(self.frame_ds_one, text="Earnings", font=("tajawal medium", 25),
                                             fg="#fff", bg="#4D63FB", padx=10, image=self.img_dollar, compound=LEFT)
        self.lbl_title_earning.grid(row=0, column=1, padx=(0, 35))
        self.lbl_count_earning = Label(self.frame_ds_one, text="$ 356,152,21", font=("tajawal", 20), fg="#212121")
        self.lbl_count_earning.grid(row=1, column=1, padx=(0, 35))

        self.lbl_title_trains = Label(self.frame_ds_one, text="Trains", font=("tajawal medium", 25),
                                       fg="#fff", bg="#4D63FB", padx=10, image=self.img_trains, compound=LEFT)
        self.lbl_title_trains.grid(row=0, column=2, padx=(0, 35))
        self.lbl_count_trains = Label(self.frame_ds_one, text="1,200", font=("tajawal", 20),
                                       fg="#212121")
        self.lbl_count_trains.grid(row=1, column=2, padx=(0, 35))

        self.lbl_title_users = Label(self.frame_ds_one, text="Users", font=("tajawal medium", 25),
                                      fg="#fff", bg="#4D63FB", padx=10, image=self.img_users, compound=LEFT)
        self.lbl_title_users.grid(row=0, column=3, padx=(0, 35))
        self.lbl_count_users = Label(self.frame_ds_one, text="23", font=("tajawal", 20),
                                      fg="#212121")
        self.lbl_count_users.grid(row=1, column=3, padx=(0, 35))

        self.lbl_title_companies = Label(self.frame_ds_one, text="Companies", font=("tajawal medium", 25),
                                     fg="#fff", bg="#4D63FB", padx=10, image=self.img_companies, compound=LEFT)
        self.lbl_title_companies.grid(row=0, column=4, padx=(0, 35))
        self.lbl_count_companies = Label(self.frame_ds_one, text="4", font=("tajawal", 20),
                                     fg="#212121")
        self.lbl_count_companies.grid(row=1, column=4, padx=(0, 35))

        self.lbl_title_reports = Label(self.frame_ds_one, text="Reports", font=("tajawal medium", 25),
                                         fg="#fff", bg="#4D63FB", padx=10, image=self.img_reports, compound=LEFT)
        self.lbl_title_reports.grid(row=0, column=5, padx=(0, 35))
        self.lbl_count_reports = Label(self.frame_ds_one, text="61", font=("tajawal", 20),
                                         fg="#212121")
        self.lbl_count_reports.grid(row=1, column=5, padx=(0, 35))

        self.frame_ti = Frame(self.tab_ticket)
        self.frame_ti.pack(pady=(35, 0))

        self.cbx_train = ctk.CTkComboBox(self.frame_ti, fg_color="#fff", border_width=0, corner_radius=0,
                                         button_color="#fff", button_hover_color="#fff", dropdown_fg_color="#fff",
                                         dropdown_text_color="#000", dropdown_hover_color="#aaa",
                                         font=("tajawal", 15), width=200, text_color="#000", state="readonly",
                                         command=self.selectTrain)
        self.cbx_train.pack(side=LEFT, padx=(0, 25))

        self.value_pnr = StringVar()
        self.ent_ti_pnr = ctk.CTkEntry(self.frame_ti, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                       text_color="#000", corner_radius=0, width=50, justify=CENTER, state="readonly",
                                       textvariable=self.value_pnr)
        self.ent_ti_pnr.pack(side=LEFT, padx=(0, 25))

        self.value_price = StringVar()
        self.ent_ti_price = ctk.CTkEntry(self.frame_ti, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                       text_color="#000", corner_radius=0, justify=CENTER, state="readonly",
                                         textvariable=self.value_price)
        self.ent_ti_price.pack(side=LEFT, padx=(0, 25))

        self.btn_ti_save = Button(self.frame_ti, text="Save", width=16, pady=3, bg="#4D63FB", activebackground="#4D63FB"
                                  , activeforeground="#fff", fg="#fff", bd=0, command=self.insertTicket)
        self.btn_ti_save.pack(side=LEFT,)

        self.frame_ti_table = ctk.CTkFrame(self.tab_ticket, fg_color="#fff", border_width=0, corner_radius=50)
        self.frame_ti_table.place(x=0, y=100, relwidth=1.0, relheight=0.9)

        self.style.layout("custom.Treeview", [])
        self.style.configure("custom.Treeview", borderwidth=0)
        self.style.configure("custom.Treeview.Heading", font=(None, 13))
        self.style.map("custom.Treeview", background=[("selected", "#4D63FB")])

        self.table_ti = ttk.Treeview(self.frame_ti_table, columns=('1','2','3','4','5'), show="headings", style="custom.Treeview")
        self.table_ti.pack(fill=BOTH, expand=True, padx=40, pady=(10, 25))
        self.table_ti.column('1', anchor=N, stretch=False, width=250)
        self.table_ti.column('2', anchor=N)
        self.table_ti.column('3', anchor=N)
        self.table_ti.column('4', anchor=N)
        self.table_ti.column('5', anchor=N)
        self.table_ti.heading('1', text="pnr", anchor=N)
        self.table_ti.heading('2', text="train", anchor=N)
        self.table_ti.heading('3', text="journey date", anchor=N)
        self.table_ti.heading('4', text="departure time", anchor=N)
        self.table_ti.heading('5', text="day availability", anchor=N)

        self.frame_tr_left = Frame(self.tab_train,)
        self.frame_tr_left.pack(side=LEFT, pady=(25, 0), fill=Y)

        self.ent_tr_name = ctk.CTkEntry(self.frame_tr_left, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                         text_color="#000", corner_radius=0, placeholder_text="train name",
                                         width=250, height=35, font=("tajawal", 20))
        self.ent_tr_name.pack(pady=(0, 15))

        self.ent_tr_class = ctk.CTkEntry(self.frame_tr_left, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                        text_color="#000", corner_radius=0, placeholder_text="class",
                                        width=250, height=35, font=("tajawal", 20))
        self.ent_tr_class.pack(pady=(0, 15))

        self.ent_tr_source = ctk.CTkEntry(self.frame_tr_left, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                        text_color="#000", corner_radius=0, placeholder_text="source",
                                        width=250, height=35, font=("tajawal", 20))
        self.ent_tr_source.pack(pady=(0, 15))

        self.ent_tr_destination = ctk.CTkEntry(self.frame_tr_left, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                               text_color="#000", corner_radius=0, placeholder_text="destination",
                                               width=250, height=35, font=("tajawal", 20))
        self.ent_tr_destination.pack(pady=(0, 15))

        self.ent_tr_travel_time = ctk.CTkEntry(self.frame_tr_left, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                        text_color="#000", corner_radius=0, placeholder_text="travel time",
                                        width=250, height=35, font=("tajawal", 20))
        self.ent_tr_travel_time.pack(pady=(0, 15))

        self.ent_tr_arrival_time = ctk.CTkEntry(self.frame_tr_left, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                         text_color="#000", corner_radius=0, placeholder_text="arrival time",
                                         width=250, height=35, font=("tajawal", 20))
        self.ent_tr_arrival_time.pack(pady=(0, 15))

        self.ent_tr_journey_date = ctk.CTkEntry(self.frame_tr_left, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                        text_color="#000", corner_radius=0, placeholder_text="journey date",
                                        width=250, height=35, font=("tajawal", 20))
        self.ent_tr_journey_date.pack(pady=(0, 15))

        self.ent_tr_departure_time = ctk.CTkEntry(self.frame_tr_left, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                         text_color="#000", corner_radius=0, placeholder_text="departure time",
                                         width=250, height=35, font=("tajawal", 20))
        self.ent_tr_departure_time.pack(pady=(0, 15))

        self.ent_tr_day_availability = ctk.CTkEntry(self.frame_tr_left, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                        text_color="#000", corner_radius=0, placeholder_text="day availability",
                                        width=250, height=35, font=("tajawal", 20))
        self.ent_tr_day_availability.pack(pady=(0, 15))

        self.ent_tr_available_seats = ctk.CTkEntry(self.frame_tr_left, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                         text_color="#000", corner_radius=0, placeholder_text="available seats",
                                         width=250, height=35, font=("tajawal", 20))
        self.ent_tr_available_seats.pack(pady=(0, 15))

        self.ent_tr_price = ctk.CTkEntry(self.frame_tr_left, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                         text_color="#000", corner_radius=0, placeholder_text="price",
                                         width=250, height=35, font=("tajawal", 20))
        self.ent_tr_price.pack(pady=(0, 15))

        self.cbx_tr_active = ctk.CTkComboBox(self.frame_tr_left, fg_color="#fff", border_width=0, corner_radius=0,
                                         button_color="#fff", button_hover_color="#fff", dropdown_fg_color="#fff",
                                         dropdown_text_color="#000", dropdown_hover_color="#aaa",
                                         font=("tajawal", 13), width=250, height=35, text_color="#000",
                                         
                                         state="readonly", values=["true", "false"])
        self.cbx_tr_active.pack(pady=(0, 15))


        self.btn_tr_save = Button(self.frame_tr_left, text="Save", pady=3, bg="#4D63FB", activebackground="#4D63FB"
                                  , activeforeground="#fff", fg="#fff", bd=0, command=self.insertTrain,
                                  font=("tajawal", 13))
        self.btn_tr_save.pack(fill=X)

        self.frame_tr_right = Frame(self.tab_train, )
        self.frame_tr_right.pack(side=LEFT, fill=BOTH, expand=True, pady=(25, 0))

        self.table_tr = ttk.Treeview(self.frame_tr_right, columns=('1', '2', '3', '4', '5',
                                                                   '6', '7', '8', '9', '10',
                                                                   '11', '12', '13'
                                                                   ), show="headings",
                                     style="custom.Treeview")
        self.table_tr.pack(fill=BOTH, expand=True, padx=40)
        self.table_tr.column('1', anchor=N, stretch=False, width=50)
        self.table_tr.column('2', anchor=N, stretch=False, width=120)
        self.table_tr.column('3', anchor=N, stretch=False, width=120)
        self.table_tr.column('4', anchor=N, stretch=False, width=120)
        self.table_tr.column('5', anchor=N, stretch=False, width=120)
        self.table_tr.column('6', anchor=N, stretch=False, width=120)
        self.table_tr.column('7', anchor=N, stretch=False, width=120)
        self.table_tr.column('8', anchor=N, stretch=False, width=120)
        self.table_tr.column('9', anchor=N, stretch=False, width=120)
        self.table_tr.column('10', anchor=N, stretch=False, width=120)
        self.table_tr.column('11', anchor=N, stretch=False, width=120)
        self.table_tr.column('12', anchor=N, stretch=False, width=100)
        self.table_tr.column('13', anchor=N, stretch=False, width=80)
        self.table_tr.heading('1', text="ID", anchor=N)
        self.table_tr.heading('2', text="train", anchor=N)
        self.table_tr.heading('3', text="class", anchor=N)
        self.table_tr.heading('4', text="source", anchor=N)
        self.table_tr.heading('5', text="destination", anchor=N)
        self.table_tr.heading('6', text="travel time", anchor=N)
        self.table_tr.heading('7', text="arrival time", anchor=N)
        self.table_tr.heading('8', text="journey date", anchor=N)
        self.table_tr.heading('9', text="departure time", anchor=N)
        self.table_tr.heading('10', text="day", anchor=N)
        self.table_tr.heading('11', text="seats", anchor=N)
        self.table_tr.heading('12', text="price", anchor=N)
        self.table_tr.heading('13', text="active", anchor=N)


        self.frame_emp = Frame(self.tab_employee)
        self.frame_emp.pack(expand=True)

        self.ent_emp_fname = ctk.CTkEntry(self.frame_emp, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                         text_color="#000", corner_radius=0, placeholder_text="first name",
                                         width=250, height=35, font=("tajawal", 20), )
        self.ent_emp_fname.grid(row=0, column=0, padx=(0, 35), pady=(0, 25))

        self.ent_emp_lname = ctk.CTkEntry(self.frame_emp, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                          text_color="#000", corner_radius=0, placeholder_text="last name",
                                          width=250, height=35, font=("tajawal", 20),)
        self.ent_emp_lname.grid(row=0, column=1, padx=(0, 35), pady=(0, 25))

        self.ent_emp_nname = ctk.CTkEntry(self.frame_emp, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                          text_color="#000", corner_radius=0, placeholder_text="nickname",
                                          width=250, height=35, font=("tajawal", 20),)
        self.ent_emp_nname.grid(row=0, column=2, pady=(0, 25))

        self.ent_emp_birthday = ctk.CTkEntry(self.frame_emp, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                          text_color="#000", corner_radius=0, placeholder_text="birthday",
                                          width=250, height=35, font=("tajawal", 20),)
        self.ent_emp_birthday.grid(row=1, column=0, padx=(0, 35), pady=(0, 25))

        self.cbx_emp_gander = ctk.CTkComboBox(self.frame_emp, fg_color="#fff", border_width=0, corner_radius=0,
                                         button_color="#fff", button_hover_color="#fff", dropdown_fg_color="#fff",
                                         dropdown_text_color="#000", dropdown_hover_color="#aaa",
                                         font=("tajawal", 20), width=250, height=35, text_color="#000",
                                         
                                         state="readonly", values=["male", "female"])
        self.cbx_emp_gander.grid(row=1, column=1, padx=(0, 35), pady=(0, 25))

        self.ent_emp_governorate = ctk.CTkEntry(self.frame_emp, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                          text_color="#000", corner_radius=0, placeholder_text="governorate",
                                          width=250, height=35, font=("tajawal", 20),)
        self.ent_emp_governorate.grid(row=1, column=2, pady=(0, 25))

        self.ent_emp_city = ctk.CTkEntry(self.frame_emp, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                          text_color="#000", corner_radius=0, placeholder_text="city",
                                          width=250, height=35, font=("tajawal", 20),)
        self.ent_emp_city.grid(row=2, column=0, padx=(0, 35), pady=(0, 25))

        self.ent_emp_st_ar = ctk.CTkEntry(self.frame_emp, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                                text_color="#000", corner_radius=0, placeholder_text="street / area",
                                                width=250, height=35, font=("tajawal", 20),)
        self.ent_emp_st_ar.grid(row=2, column=1, padx=(0, 35), pady=(0, 25))

        self.ent_emp_home_no = ctk.CTkEntry(self.frame_emp, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                         text_color="#000", corner_radius=0, placeholder_text="home no",
                                         width=250, height=35, font=("tajawal", 20),)
        self.ent_emp_home_no.grid(row=2, column=2, pady=(0, 25))

        self.ent_emp_floor = ctk.CTkEntry(self.frame_emp, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                         text_color="#000", corner_radius=0, placeholder_text="floor",
                                         width=250, height=35, font=("tajawal", 20),)
        self.ent_emp_floor.grid(row=3, column=0, padx=(0, 35), pady=(0, 25))

        self.ent_emp_university = ctk.CTkEntry(self.frame_emp, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                          text_color="#000", corner_radius=0, placeholder_text="university",
                                          width=250, height=35, font=("tajawal", 20),)
        self.ent_emp_university.grid(row=3, column=1, padx=(0, 35), pady=(0, 25))

        self.ent_emp_certificate = ctk.CTkEntry(self.frame_emp, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                            text_color="#000", corner_radius=0, placeholder_text="certificate",
                                            width=250, height=35, font=("tajawal", 20),)
        self.ent_emp_certificate.grid(row=3, column=2, pady=(0, 25))

        self.ent_emp_degree = ctk.CTkEntry(self.frame_emp, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                          text_color="#000", corner_radius=0, placeholder_text="degree",
                                          width=250, height=35, font=("tajawal", 20),)
        self.ent_emp_degree.grid(row=4, column=0, padx=(0, 35), pady=(0, 25))

        self.ent_emp_work = ctk.CTkEntry(self.frame_emp, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                               text_color="#000", corner_radius=0, placeholder_text="work",
                                               width=250, height=35, font=("tajawal", 20),)
        self.ent_emp_work.grid(row=4, column=1, padx=(0, 35), pady=(0, 25))

        self.ent_emp_note = ctk.CTkEntry(self.frame_emp, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                                text_color="#000", corner_radius=0, placeholder_text="note",
                                                width=250, height=35, font=("tajawal", 20),)
        self.ent_emp_note.grid(row=4, column=2, pady=(0, 25))

        self.ent_emp_salary = ctk.CTkEntry(self.frame_emp, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                           text_color="#000", corner_radius=0, placeholder_text="salary",
                                           width=250, height=35, font=("tajawal", 20),)
        self.ent_emp_salary.grid(row=5, column=0, padx=(0, 35), pady=(0, 25))

        self.ent_emp_username = ctk.CTkEntry(self.frame_emp, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                         text_color="#000", corner_radius=0, placeholder_text="username",
                                         width=250, height=35, font=("tajawal", 20),)
        self.ent_emp_username.grid(row=5, column=1, padx=(0, 35), pady=(0, 25))

        self.ent_emp_password = ctk.CTkEntry(self.frame_emp, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                         text_color="#000", corner_radius=0, placeholder_text="password",
                                         width=250, height=35, font=("tajawal", 20),)
        self.ent_emp_password.grid(row=5, column=2, pady=(0, 25))

        self.frame_emp.columnconfigure(0, weight=2)
        self.btn_emp_save = Button(self.frame_emp, text="Save", pady=3, bg="#4D63FB", activebackground="#4D63FB"
                                  , activeforeground="#fff", fg="#fff", bd=0, command=self.insertEmployee,
                                   font=("tajawal", 13),)
        self.btn_emp_save.grid(row=6, column=0, columnspan=3, sticky="news", pady=(0, 25))

        self.frame_com = Frame(self.tab_company)
        self.frame_com.pack(expand=True)

        self.ent_com_name = ctk.CTkEntry(self.frame_com, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                          text_color="#000", corner_radius=0, placeholder_text="name",
                                          width=250, height=35, font=("tajawal", 20), )
        self.ent_com_name.grid(row=0, column=0, padx=(0, 35), pady=(0, 25))

        self.ent_com_type_company = ctk.CTkEntry(self.frame_com, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                          text_color="#000", corner_radius=0, placeholder_text="type company",
                                          width=250, height=35, font=("tajawal", 20), )
        self.ent_com_type_company.grid(row=0, column=1, padx=(0, 35), pady=(0, 25))

        self.ent_com_country = ctk.CTkEntry(self.frame_com, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                          text_color="#000", corner_radius=0, placeholder_text="country",
                                          width=250, height=35, font=("tajawal", 20), )
        self.ent_com_country.grid(row=0, column=2, pady=(0, 25))

        self.ent_com_address = ctk.CTkEntry(self.frame_com, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                             text_color="#000", corner_radius=0, placeholder_text="address",
                                             width=250, height=35, font=("tajawal", 20), )
        self.ent_com_address.grid(row=1, column=0, padx=(0, 35), pady=(0, 25))

        self.ent_com_fix_number = ctk.CTkEntry(self.frame_com, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                             text_color="#000", corner_radius=0, placeholder_text="fix number",
                                             width=250, height=35, font=("tajawal", 20), )
        self.ent_com_fix_number.grid(row=1, column=1, padx=(0, 35), pady=(0, 25))

        self.ent_com_email = ctk.CTkEntry(self.frame_com, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                                text_color="#000", corner_radius=0, placeholder_text="email",
                                                width=250, height=35, font=("tajawal", 20), )
        self.ent_com_email.grid(row=1, column=2, pady=(0, 25))

        self.frame_com.columnconfigure(0, weight=2)
        self.btn_com_save = Button(self.frame_com, text="Save", pady=3, bg="#4D63FB", activebackground="#4D63FB"
                                   , activeforeground="#fff", fg="#fff", bd=0, command=self.insertCompany,
                                   font=("tajawal", 13), )
        self.btn_com_save.grid(row=2, column=0, columnspan=3, sticky="news", pady=(0, 25))


        self.ctknotebook = ctk.CTkTabview(self.tab_report, fg_color=self.colorInActiveTab,
                                          segmented_button_fg_color=self.colorInActiveTab,
                                          corner_radius=100, segmented_button_selected_color=self.colorActiveTab,
                                          )
        self.ctknotebook.pack(fill=BOTH, expand=True)
        self.ctknotebook.add("Problem")
        self.ctknotebook.add("Solve")

        self.frame_rep = Frame(self.ctknotebook.tab("Problem"))
        self.frame_rep.pack(anchor=N)

        self.cbx_rep_train = ctk.CTkComboBox(self.frame_rep, fg_color="#fff", border_width=0, corner_radius=0,
                                               button_color="#fff", button_hover_color="#fff",
                                               dropdown_fg_color="#fff",
                                               dropdown_text_color="#000", dropdown_hover_color="#aaa",
                                               font=("tajawal", 20), width=250, height=35, text_color="#000",
                                               state="readonly")
        self.cbx_rep_train.grid(row=0, column=0, padx=(0, 35), pady=(0, 25))

        self.cbx_rep_employee = ctk.CTkComboBox(self.frame_rep, fg_color="#fff", border_width=0, corner_radius=0,
                                              button_color="#fff", button_hover_color="#fff", dropdown_fg_color="#fff",
                                              dropdown_text_color="#000", dropdown_hover_color="#aaa",
                                              font=("tajawal", 20), width=250, height=35, text_color="#000",
                                              state="readonly")
        self.cbx_rep_employee.grid(row=0, column=1, padx=(0, 35), pady=(0, 25))

        self.cbx_rep_company = ctk.CTkComboBox(self.frame_rep, fg_color="#fff", border_width=0, corner_radius=0,
                                                button_color="#fff", button_hover_color="#fff",
                                                dropdown_fg_color="#fff",
                                                dropdown_text_color="#000", dropdown_hover_color="#aaa",
                                                font=("tajawal", 20), width=250, height=35, text_color="#000",
                                                state="readonly")
        self.cbx_rep_company.grid(row=0, column=2, pady=(0, 25))

        self.ent_rep_title_problem = ctk.CTkEntry(self.frame_rep, fg_color="#fff", border_width=1, border_color="#DFDFDF",
                                          text_color="#000", corner_radius=0, placeholder_text="title problem",
                                          width=250, height=35, font=("tajawal", 20), )
        self.ent_rep_title_problem.grid(row=1, column=0, padx=(0, 35), pady=(0, 25))

        self.ent_rep_type_problem = ctk.CTkEntry(self.frame_rep, fg_color="#fff", border_width=1,
                                                  border_color="#DFDFDF",
                                                  text_color="#000", corner_radius=0, placeholder_text="type problem",
                                                  width=250, height=35, font=("tajawal", 20), )
        self.ent_rep_type_problem.grid(row=1, column=1, padx=(0, 35), pady=(0, 25))

        self.ent_rep_bidget = ctk.CTkEntry(self.frame_rep, fg_color="#fff", border_width=1,
                                                 border_color="#DFDFDF",
                                                 text_color="#000", corner_radius=0, placeholder_text="bidget",
                                                 width=250, height=35, font=("tajawal", 20), )
        self.ent_rep_bidget.grid(row=1, column=2, pady=(0, 25))

        self.frame_rep.columnconfigure(0, weight=2)
        self.description_problem = ctk.CTkTextbox(self.frame_rep, fg_color="#fff", border_width=1,
                                                  border_color="#DFDFDF", corner_radius=0, text_color="#000",
                                                  height=300)
        self.description_problem.grid(row=2, column=0, columnspan=3, sticky="news", pady=(0, 25))

        self.btn_rep_save = Button(self.frame_rep, text="Save", pady=3, bg="#4D63FB", activebackground="#4D63FB"
                                   , activeforeground="#fff", fg="#fff", bd=0, command=self.insertReportProblem,
                                   font=("tajawal", 13), )
        self.btn_rep_save.grid(row=3, column=0, columnspan=3, sticky="news")

        self.frame_reps_solve = Frame(self.ctknotebook.tab("Solve"))
        self.frame_reps_solve.pack(anchor=N)

        self.cbx_reps_train = ctk.CTkComboBox(self.frame_reps_solve, fg_color="#fff", border_width=0, corner_radius=0,
                                             button_color="#fff", button_hover_color="#fff",
                                             dropdown_fg_color="#fff",
                                             dropdown_text_color="#000", dropdown_hover_color="#aaa",
                                             font=("tajawal", 20), width=250, height=35, text_color="#000",
                                             state="readonly")
        self.cbx_reps_train.grid(row=0, column=0, padx=(0, 35), pady=(0, 25))

        self.cbx_reps_employee = ctk.CTkComboBox(self.frame_reps_solve, fg_color="#fff", border_width=0, corner_radius=0,
                                                button_color="#fff", button_hover_color="#fff",
                                                dropdown_fg_color="#fff",
                                                dropdown_text_color="#000", dropdown_hover_color="#aaa",
                                                font=("tajawal", 20), width=250, height=35, text_color="#000",
                                                state="readonly")
        self.cbx_reps_employee.grid(row=0, column=1, padx=(0, 35), pady=(0, 25))

        self.cbx_reps_company = ctk.CTkComboBox(self.frame_reps_solve, fg_color="#fff", border_width=0, corner_radius=0,
                                               button_color="#fff", button_hover_color="#fff",
                                               dropdown_fg_color="#fff",
                                               dropdown_text_color="#000", dropdown_hover_color="#aaa",
                                               font=("tajawal", 20), width=250, height=35, text_color="#000",
                                               state="readonly")
        self.cbx_reps_company.grid(row=0, column=2, pady=(0, 25))

        self.ent_reps_title_solve = ctk.CTkEntry(self.frame_reps_solve, fg_color="#fff", border_width=1,
                                                  border_color="#DFDFDF",
                                                  text_color="#000", corner_radius=0, placeholder_text="title solve",
                                                  width=250, height=35, font=("tajawal", 20), )
        self.ent_reps_title_solve.grid(row=1, column=0, padx=(0, 35), pady=(0, 25))

        self.ent_reps_type_solve = ctk.CTkEntry(self.frame_reps_solve, fg_color="#fff", border_width=1,
                                                 border_color="#DFDFDF",
                                                 text_color="#000", corner_radius=0, placeholder_text="type solve",
                                                 width=250, height=35, font=("tajawal", 20), )
        self.ent_reps_type_solve.grid(row=1, column=1, padx=(0, 35), pady=(0, 25))

        self.ent_reps_bidget = ctk.CTkEntry(self.frame_reps_solve, fg_color="#fff", border_width=1,
                                           border_color="#DFDFDF",
                                           text_color="#000", corner_radius=0, placeholder_text="bidget",
                                           width=250, height=35, font=("tajawal", 20), )
        self.ent_reps_bidget.grid(row=1, column=2, pady=(0, 25))

        self.frame_reps_solve.columnconfigure(0, weight=2)
        self.description_solve = ctk.CTkTextbox(self.frame_reps_solve, fg_color="#fff", border_width=1,
                                                  border_color="#DFDFDF", corner_radius=0, text_color="#000",
                                                  height=300)
        self.description_solve.grid(row=2, column=0, columnspan=3, sticky="news", pady=(0, 25))

        self.btn_reps_save = Button(self.frame_reps_solve, text="Save", pady=3, bg="#4D63FB", activebackground="#4D63FB"
                                   , activeforeground="#fff", fg="#fff", bd=0, command=self.insertReportSolve,
                                   font=("tajawal", 13), )
        self.btn_reps_save.grid(row=3, column=0, columnspan=3, sticky="news")

        # variables
        self.active_tab = self.btn_tab_dashboard
        self.value_price_db = StringVar()
        self.value_description_problem = StringVar()
        self.value_description_solve = StringVar()
        self.database = DB()
        self.refreshTable()
        self.refreshCombobox()


        self.frame_chart = Frame(self.tab_dashboard)
        self.frame_chart.pack(fill=BOTH, expand=True)

        # plot
        self.fig, self.ax = plt.subplots(facecolor="#f0f0f0")
        self.ax.set_xlabel("Trains")
        self.ax.set_ylabel("Earnings")

        self.canvas = FigureCanvasTkAgg(self.fig, self.frame_chart)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=BOTH, expand=True)

        self.toolbarFrame = Frame(self.tab_dashboard)
        self.toolbarFrame.pack(pady=(0, 35))
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.toolbarFrame)

        self.checkDatabase()

        self.refreshDashboard()

    def checkDatabase(self):
        if not os.path.exists(f"{self.database.__path__()}\\database.db"):
            self.database.insert("employee",(
                "abdulrahman","ayman","araf",
                "2000-11-01", "male", "giza", "imbaba", "qowmey", 32, 1,
                "future academy", "bms", 100, 3000, "admin", 123456
            ))

    def login(self):
        username = self.ent_username.get()
        password = self.ent_password.get()
        checkfields = self.checkFields((self.ent_username, self.ent_password))
        if checkfields:
            check_user = self.database.customSelect(
                f"SELECT id FROM employee WHERE username=\"{username}\" and password=\"{password}\"")
            if check_user:
                self.main_notebook.select(1)
            else:
                messagebox.showerror("Login", "user not found !")

    def photoImage(self, src: str, size: tuple[int, int]=None):
        img = Image.open(src)
        if size:
            img = img.resize(size)
        img = ImageTk.PhotoImage(img)
        return img

    def selectTab(self, index: int, button):
        self.active_tab.configure(text_color="#000", fg_color=self.colorInActiveTab)
        self.active_tab = button
        button.configure(text_color="#fff", fg_color=self.colorActiveTab)
        self.notebook.select(index)

    def clearTable(self, table: tuple):
        for tb in table:
            for item in tb.get_children():
                tb.delete(item)

    def insertTable(self, table: tuple):
        for i, tb in enumerate(table[0]):
            select_table = tb
            for data in table[1][i]:
                select_table.insert('', END, values=data)

    def refreshTable(self):
        # data
        data_ticket = self.database.select("ticket")
        data_train = self.database.select("train")
        data = (data_train, data_ticket,)
        # tables
        tables = (self.table_tr, self.table_ti, )
        # clear
        self.clearTable(tables)
        # add data
        self.insertTable((tables, data))

    def refreshCombobox(self):
        # data
        data_train = [name[0] for name in self.database.customSelect("SELECT name FROM train")]
        data_employee = [name[0] for name in self.database.select("employees")]
        data_company = [name[0] for name in self.database.customSelect("SELECT name FROM company")]
        # Combobox
        self.cbx_train.configure(values=data_train)
        self.cbx_rep_train.configure(values=data_train)
        self.cbx_rep_employee.configure(values=data_employee)
        self.cbx_rep_company.configure(values=data_company)

        self.cbx_reps_train.configure(values=data_train)
        self.cbx_reps_employee.configure(values=data_employee)
        self.cbx_reps_company.configure(values=data_company)

    def refreshDashboard(self):
        count_tickets = self.database.customSelect("SELECT count(id) FROM ticket")[0][0]
        count_trains = self.database.customSelect("SELECT count(id) FROM train")[0][0]
        count_employees = self.database.customSelect("SELECT count(id) FROM employee")[0][0]
        count_company = self.database.customSelect("SELECT count(id) FROM company")[0][0]
        count_report_problem = self.database.customSelect("SELECT count(id) FROM report_problem")[0][0]
        count_report_solve = self.database.customSelect("SELECT count(id) FROM report_solve")[0][0]
        count_earning = self.database.customSelect("SELECT SUM(price) FROM ticket")[0][0]
        trains = [train[0] for train in self.database.customSelect("SELECT name FROM train")]
        earnings = [earning[0] for earning in self.database.customSelect("""
        SELECT SUM(ti.price) as SumAm 
        FROM ticket ti
        INNER JOIN train tr ON ti.train_id = tr.id
        WHERE tr.name IN (SELECT name FROM train)
        group by name;
        """)]
        count_reports = count_report_problem + count_report_solve
        self.lbl_count_tickets["text"] = str(count_tickets)
        self.lbl_count_trains["text"] = str(count_trains)
        self.lbl_count_users["text"] = str(count_employees)
        self.lbl_count_companies["text"] = str(count_company)
        self.lbl_count_reports["text"] = str(count_reports)
        self.lbl_count_earning["text"] = f"${count_earning}" if count_earning else f"$0"

        self.ax.clear()
        self.ax.bar(trains, earnings)
        self.canvas.draw()
        #self.ax.fmt_ydata(earnings)
        #self.ax.set_xdata(trains)



    def checkFields(self, *fields) -> bool:
        check = True
        for field in fields[0]:
            if not field.get():
                check = False
                if field.__class__.__name__ == "CTkEntry":
                    messagebox.showerror("Error", f"field '{field.cget('placeholder_text')}' is empty", icon="error")
                    field.focus()
                else:
                    messagebox.showerror("Error", "fields empty", icon="error")
                break
        return check

    def clearFields(self, fields):
        for field in fields:
            if field.__class__.__name__ == "CTkEntry":
                field.delete(0, END)
                continue
            field.set('')
        fields[0].focus()

    def selectTrain(self, event):
        train = self.cbx_train.get()
        data_train = self.database.customSelect(f"SELECT id, available_seats, price FROM train WHERE name=\"{train}\"")
        data_ticket = self.database.customSelect("SELECT pnr_number FROM ticket WHERE train_id=%d" % data_train[0][0])
        if data_train:
            pnr = int(data_train[0][1])
            if data_ticket:
                for i in data_ticket:
                    pnr -= 1
            if not pnr:
                messagebox.showwarning("warning", "not available seats !")
                return
            self.ent_ti_pnr.configure(state="normal")
            self.ent_ti_price.configure(state="normal")
            self.ent_ti_pnr.delete(0, END)
            self.ent_ti_price.delete(0, END)
            self.ent_ti_pnr.insert(0, pnr)
            self.ent_ti_price.insert(0, f"${data_train[0][2]}")
            self.ent_ti_pnr.configure(state="readonly")
            self.ent_ti_price.configure(state="readonly")

    def insertData(self, table_database: str, *fields):
        data = [field.get() for field in fields]
        checkfields = self.checkFields(fields)
        if checkfields:
            unique = self.database.insert(table_database, data)
            if unique == "unique":
                messagebox.showerror("Unique", "train already exists")
            else:
                self.clearFields(fields)
                self.refreshTable()
                self.refreshCombobox()
                self.refreshDashboard()

    def insertTrain(self):
        self.insertData("train",
                        self.ent_tr_name,
                        self.ent_tr_class,
                        self.ent_tr_source,
                        self.ent_tr_destination,
                        self.ent_tr_travel_time,
                        self.ent_tr_arrival_time,
                        self.ent_tr_journey_date,
                        self.ent_tr_departure_time,
                        self.ent_tr_day_availability,
                        self.ent_tr_available_seats,
                        self.ent_tr_price,
                        self.cbx_tr_active,
                        )

    def insertTicket(self):
        self.value_price_db.set( self.ent_ti_price.get().replace("$", '') )
        self.insertData("ticket",
                        self.cbx_train,
                        self.value_pnr,
                        self.value_price_db
                        )
        self.value_price.set('')

    def insertEmployee(self):
        self.insertData("employee",
                        self.ent_emp_fname,
                        self.ent_emp_lname,
                        self.ent_emp_nname,
                        self.ent_emp_birthday,
                        self.cbx_emp_gander,
                        self.ent_emp_governorate,
                        self.ent_emp_city,
                        self.ent_emp_st_ar,
                        self.ent_emp_home_no,
                        self.ent_emp_floor,
                        self.ent_emp_university,
                        self.ent_emp_certificate,
                        self.ent_emp_degree,
                        self.ent_emp_work,
                        self.ent_emp_note,
                        self.ent_emp_salary,
                        self.ent_emp_username,
                        self.ent_emp_password,
                        )

    def insertCompany(self):
        self.insertData("company",
                        self.ent_com_name,
                        self.ent_com_type_company,
                        self.ent_com_country,
                        self.ent_com_address,
                        self.ent_com_fix_number,
                        self.ent_com_email,
                        )

    def insertReportProblem(self):
        description = self.description_problem.get("0.1", END)
        if description != '\n':
            self.value_description_problem.set(description)
        self.insertData("report_problem",
                        self.cbx_rep_train,
                        self.cbx_rep_employee,
                        self.cbx_rep_company,
                        self.ent_rep_title_problem,
                        self.ent_rep_type_problem,
                        self.ent_rep_bidget,
                        self.value_description_problem
                        )
        self.description_problem.delete("0.1", END)

    def insertReportSolve(self):
        description = self.description_solve.get("0.1", END)
        self.value_description_solve.set(description)
        self.insertData("report_solve",
                        self.cbx_reps_train,
                        self.cbx_reps_employee,
                        self.cbx_reps_company,
                        self.ent_reps_title_solve,
                        self.ent_reps_type_solve,
                        self.ent_reps_bidget,
                        self.value_description_solve
                        )
        self.description_solve.delete("0.1", END)

if __name__ == '__main__':
    root = ctk.CTk()
    root.after(0, lambda: root.state('zoomed'))
    app = Application(root)
    try:
        root.mainloop()
    except KeyboardInterrupt:
        pass
