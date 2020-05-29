from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date
from controller import Controller
from tkcalendar import DateEntry, Calendar

global cashier_frame

controller = Controller()

"""
#====================================================================================================================#
#-----------------------            LOGIN  CLASS                                              -----------------------#
#====================================================================================================================#
"""

class Login:
    trans_start = False
    customer_reg_open = False
    cust_id_current = None
    cust_find_next = 0
    customer_list = []
    customer_prev_id = 0
    custfname = ""
    custlname = ""
    cust_all_list = []
    
    def __init__(self):
        global if_no_suki_ask
        if_no_suki_ask = None

    def show(self):
        global ROOT, LOGIN_WIDTH, LOGIN_HEIGHT
        LOGIN_WIDTH = 650
        LOGIN_HEIGHT = 600

        ROOT = Tk()
        config = self.window_config(ROOT, LOGIN_WIDTH, LOGIN_HEIGHT)

        FRAME_TOP_LOGIN = Frame(ROOT, bg="blue")
        FRAME_TOP_LOGIN.place(relx=0, rely=0, relwidth=1, relheight=0.11)

        FRAME_LOGIN_INNER = Frame(ROOT, bg="#5cb7d8")
        FRAME_LOGIN_INNER.place(relx=0, rely=0, relwidth=1, relheight=0.10)

        global LOGIN_BACKGROUND
        LOGIN_BACKGROUND = PhotoImage(file="icon/system_logo.png")
        LABEL_LOGIN_BACKGROUND = Label(FRAME_LOGIN_INNER, image=LOGIN_BACKGROUND, bg="#5cb7d8")
        LABEL_LOGIN_BACKGROUND.place(x=100, y=0)

        LABEL_LOGIN_TITLE = Label(FRAME_LOGIN_INNER, text="STORE INVENTORY SYSTEM", bg="#5cb7d8", font=("algerian", 20))
        LABEL_LOGIN_TITLE.grid(row=0, column=1, padx=160, ipady=11)

        FRAME_CENTER_LOGIN = Frame(ROOT, bg="#5cb7d8")
        FRAME_CENTER_LOGIN.place(relx=0.15, rely=0.18, relwidth=0.70, relheight=0.70)

        FRAME_CENTER_LOGIN_IMAGE = Frame(ROOT, bg="white")
        FRAME_CENTER_LOGIN_IMAGE.place(relx=0.16, rely=0.19, relwidth=0.68, relheight=0.68)

        global ICON_LOCK_LOGIN
        ICON_LOCK_LOGIN = PhotoImage(file="icon/locker.png")
        LABEL_LOCK_LOGIN = Label(FRAME_CENTER_LOGIN_IMAGE, image=ICON_LOCK_LOGIN, bg="white")
        LABEL_LOCK_LOGIN.grid(row=0, column=0, ipady=11, padx=10)

        LABEL_FORM_LOGIN = Label(FRAME_CENTER_LOGIN_IMAGE, text="Login form: ", font=("algerian", 18), bg="white")
        LABEL_FORM_LOGIN.grid(row=0, column=1, pady=2)

        global LOGO_LOGIN
        LOGO_LOGIN = PhotoImage(file="icon/user.png")
        LABEL_LOGO_LOGIN = Label(FRAME_CENTER_LOGIN_IMAGE, image=LOGO_LOGIN, bg="white")
        LABEL_LOGO_LOGIN.place(x=166, y=60)

        FRAME_FORM_LOGIN = Frame(FRAME_CENTER_LOGIN_IMAGE, bg="white")
        FRAME_FORM_LOGIN.place(x=55, y=180)

        global LABEL_USERNAME_LOGIN
        LABEL_USERNAME_LOGIN = Label(FRAME_FORM_LOGIN, text="Username: ", font=("arial", 13), bg="white")
        LABEL_USERNAME_LOGIN.grid(row=3, column=0, sticky="w")

        global username_login_var, ENTRY_USERNAME_LOGIN
        username_login_var = StringVar()
        ENTRY_USERNAME_LOGIN = Entry(FRAME_FORM_LOGIN, textvariable=username_login_var, font=("arial", 13), bg="#ddd",
                                     width=36, bd=2,
                                     relief=GROOVE)
        ENTRY_USERNAME_LOGIN.grid(row=4, column=0, ipady=5, padx=5)
        ENTRY_USERNAME_LOGIN.focus_set()

        LABEL_SPACING_LOGIN = Label(FRAME_FORM_LOGIN, font=("arial", 13), bg="white")
        LABEL_SPACING_LOGIN.grid(row=5, column=0, sticky="w")

        LABEL_PASSWORD_LOGIN = Label(FRAME_FORM_LOGIN, text="Password: ", font=("arial", 13), bg="white")
        LABEL_PASSWORD_LOGIN.grid(row=6, column=0, sticky="w")

        global password_login_var, ENTRY_PASSWORD_LOGIN
        password_login_var = StringVar()
        ENTRY_PASSWORD_LOGIN = Entry(FRAME_FORM_LOGIN, textvariable=password_login_var, font=("arial", 13), bg="#ddd",
                                     width=36, bd=2,
                                     relief=GROOVE, show="*")
        ENTRY_PASSWORD_LOGIN.grid(row=7, column=0, ipady=5)

        FRAME_BUTTON_LOGIN = Frame(FRAME_CENTER_LOGIN_IMAGE, bg="white")
        FRAME_BUTTON_LOGIN.place(x=100, y=335)

        BUTTON_CANCEL_LOGIN = Button(FRAME_BUTTON_LOGIN, text="CANCEL", width=10, bg='red', fg="white",
                                     font=("arial", 11), relief=GROOVE, command=login_cancel)
        BUTTON_CANCEL_LOGIN.pack(side=LEFT, pady=15, padx=10, ipady=2)

        BUTTON_SUBMIT_LOGIN = Button(FRAME_BUTTON_LOGIN, text="LOGIN", width=10, bg="blue", fg="white",
                                     font=("arial", 11),
                                     relief=GROOVE, command=login_submit)
        BUTTON_SUBMIT_LOGIN.pack(side=LEFT, padx=10, ipady=2)

        FRAME_BOTTOM_LOGIN = Frame(ROOT, bg="white")
        FRAME_BOTTOM_LOGIN.place(relx=0, rely=0.96, relwidth=1, relheight=0.04)

        LABEL_COPYRIGHT_LOGIN = Label(FRAME_BOTTOM_LOGIN, text="Copyright @ 2019 || SIS. All rights reserved.",
                                      bg="white")
        LABEL_COPYRIGHT_LOGIN.pack()

        LABEL_VERSION_LOGIN = Label(FRAME_BOTTOM_LOGIN, text="Version: 1.0.", bg="white")
        LABEL_VERSION_LOGIN.place(x=550, y=0)

        ROOT.geometry('%dx%d+%d+%d' % (config['WIDTH'], config['HEIGHT'], config['x'], config['y']))
        ROOT.bind("<Return>", login_enter)
        ROOT.mainloop()

    def display(self):
        pass

    def window_config(self, frame, WIDTH, HEIGHT):
        frame.title("STORE INVENTORY SYSTEM")
        ws = frame.winfo_screenwidth()
        hs = frame.winfo_screenheight()
        x = (ws / 2) - (WIDTH / 2)
        y = (hs / 2) - (HEIGHT / 2)
        frame.resizable(False, False)
        frame.iconbitmap('icon/inventory_logo.ico')
        frame.config(bg="#ddd")

        return {
            "WIDTH": WIDTH,
            "HEIGHT":
                HEIGHT,
            "x": x,

            "y": y
        }


"""
#====================================================================================================================#
#-----------------------            LOGIN FUNCTIONALITY AREA                                  -----------------------#
#====================================================================================================================#
"""


def login_submit():
    login_function()


def login_cancel():
    username_login_var.set("")
    password_login_var.set("")
    ENTRY_USERNAME_LOGIN.focus_set()


def login_enter(event):
    login_function()


def login_validate():
    errors = []
    if username_login_var.get() == "":
        errors.append("Username is required.")

    if password_login_var.get() == "":
        errors.append("Password is required.")

    return errors


def login_function():
    errors = login_validate()

    if len(errors) == 0:
        uname = username_login_var.get()
        upass = password_login_var.get()
        resp = controller.user_login(uname, upass)

        if len(resp) > 0:
            if resp[0]['user_password'] == upass and resp[0]['user_position'] == 0:
                if resp[0]['user_status'] == 0:
                    messagebox.showwarning("Warning", "Your account was Deactivate by the admin.", parent=ROOT)
                    return False

                files = open("_session.txt", 'w')
                files.write("{}: {}\n".format("username", resp[0]['user_username']))
                files.write("{}: {}\n".format("password", resp[0]['user_password']))
                files.write("{}: {}\n".format("userid", resp[0]['user_id']))
                files.close()
                messagebox.showinfo("Information message", "Login successfully.", parent=ROOT)
                ROOT.withdraw()
                cashier.main()

            else:
                messagebox.showerror("Error message", "Incorrect username or password", parent=ROOT)
        else:
            messagebox.showerror("Error message", "Account not Exist", parent=ROOT)
            login_cancel()
    else:
        ENTRY_USERNAME_LOGIN.focus()
        message = ""
        for error in errors:
            message += error + "\n"

        messagebox.showerror("Error message", message, parent=ROOT)


"""
#====================================================================================================================#
#-----------------------            CASHIER  CLASS                                            -----------------------#
#====================================================================================================================#
"""


class Cashier:
    def __init__(self):
        pass

    def main(self):
        global cashier_frame
        cashier_frame = Toplevel()
        config = self.window_config(cashier_frame, 1000, 800)

        # ---- HEADER FRAME ----#
        FRAME_TOP = Frame(cashier_frame, bg="green")
        FRAME_TOP.place(relx=0, rely=0, relwidth=1, relheight=0.09)

        FRAME_INNER = Frame(cashier_frame, bg="#7fdb98")
        FRAME_INNER.place(relx=0, rely=0, relwidth=1, relheight=0.08)

        ICON_INVENTORY = PhotoImage(file="icon/system_logo.png")
        LABEL_ICON_INVENTORY = Label(FRAME_INNER, image=ICON_INVENTORY, bg="#7fdb98")
        LABEL_ICON_INVENTORY.place(x=20, y=0)

        LABEL_TITLE = Label(FRAME_INNER, text="STORE INVENTORY SYSTEM", bg="#7fdb98", font=("algerian", 20))
        LABEL_TITLE.grid(row=0, column=0, padx=85, ipady=11)

        ICON_LOGOUT = PhotoImage(file="icon/button_logout.png")
        BUTTON_ICON_LOGOUT = Button(FRAME_INNER, image=ICON_LOGOUT, bg="#7fdb98", bd=2, command=self.logout)
        BUTTON_ICON_LOGOUT.place(relx=0.80, rely=0.06)

        # ---- BOTTOM FRAME ----#
        self.gui_footer(cashier_frame)

        # ---- MAIN FRAME ----#
        FRAME_MAIN = Frame(cashier_frame, bg="#4caf50")
        FRAME_MAIN.place(relx=0.06, rely=0.11, relwidth=0.89, relheight=0.83)

        FRAME_MAIN_INNER = Frame(FRAME_MAIN, bg="white")
        FRAME_MAIN_INNER.place(relx=0.003, rely=0.004, relwidth=0.994, relheight=0.993)

        # ---- MAIN TOP FRAME ----#
        FRAME_MAIN_TOP = Frame(FRAME_MAIN_INNER, bg="#4caf50")
        FRAME_MAIN_TOP.place(relx=0, rely=0, relwidth=1, relheight=0.06)

        ICON_PRODUCT = PhotoImage(file="icon/register.png")
        LABEL_ICON_PRODUCT = Label(FRAME_MAIN_TOP, image=ICON_PRODUCT, bg="#4caf50")
        LABEL_ICON_PRODUCT.place(relx=0.01, rely=0)

        label_form = Label(FRAME_MAIN_TOP, text="Customer order: ", font=("algerian", 14), bg="#4caf50")
        label_form.grid(row=0, column=0, padx=40, pady=5)

        # ---- ORDER SUMMARY    ---#
        LABEL_ORDER_TITLE = Label(FRAME_MAIN_INNER, text="ORDER SUMMARY", font=("arial", 12, "bold"))
        LABEL_ORDER_TITLE.grid(row=0, column=0, pady=60, padx=25, ipadx=15, sticky="w")

        # ---- TABLE FRAME ----#
        FRAME_ORDERLIST = Frame(FRAME_MAIN_INNER)
        FRAME_ORDERLIST.place(relx=0.03, rely=0.14, relwidth=0.95, relheight=0.34)

        global TREE_ORDERLIST
        TREE_ORDERLIST = ttk.Treeview(FRAME_ORDERLIST, selectmode='browse')
        STYLE = ttk.Style()
        STYLE.configure("Treeview.Heading", font=("arial", 13, "bold"))
        STYLE.configure('Treeview', rowheight=30)

        vsb = ttk.Scrollbar(TREE_ORDERLIST, orient="vertical", command=TREE_ORDERLIST.yview)
        vsb.pack(side='right', fill='y')
        TREE_ORDERLIST.configure(yscrollcommand=vsb.set)

        TREE_ORDERLIST["columns"] = ("one", "two", "three")
        TREE_ORDERLIST.column("#0", width=120)
        TREE_ORDERLIST.column("one", width=10)
        TREE_ORDERLIST.column("two", width=20)
        TREE_ORDERLIST.column("three", width=20)

        TREE_ORDERLIST.heading("#0", text="Product name", anchor="w")
        TREE_ORDERLIST.heading("one", text="Price", anchor="w")
        TREE_ORDERLIST.heading("two", text="Quantity", anchor="w")
        TREE_ORDERLIST.heading("three", text="Amount", anchor="w")

        # TREE_ORDERLIST.insert('', 'end', text="Apple Phone", values=["2", "10000", "20000"])
        TREE_ORDERLIST.insert('', 'end', text="No Record", values=["---", "---", "---", ""])

        TREE_ORDERLIST.tag_configure('T', font='Arial 30 bold')
        TREE_ORDERLIST.place(relx=0, rely=0, relwidth=1, relheight=1)
        TREE_ORDERLIST.bind("<Double-1>", cashier.modal_updateqty)
        TREE_ORDERLIST.bind("<Return>", cashier.modal_updateqty)

        # ---- TABLE FRAME ----#
        FRAME_FORM = Frame(FRAME_MAIN_INNER, bg="#ddd")
        FRAME_FORM.place(relx=0.03, rely=0.49, relwidth=0.95, relheight=0.37)

        FRAME_FORM_INNER = Frame(FRAME_FORM, bg="white")
        FRAME_FORM_INNER.place(relx=0.002, rely=0.011, relwidth=0.9955, relheight=0.974)

        # ---- SEARCH FRAME FORM ----#
        FRAME_SEARCH_FORM = Frame(FRAME_FORM, bg="white")
        FRAME_SEARCH_FORM.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.9)

        # ---- SEARCH PRODUCT CODE ----#
        LABEL_SALE_PRODUCTCODE = Label(FRAME_SEARCH_FORM, text="SEARCH PRODUCT:", font=("arial", 12, "bold"),
                                       bg="white")
        LABEL_SALE_PRODUCTCODE.grid(row=0, column=0, padx=60, sticky="w")

        global ENTRY_SALE_PRODUCTCODE, sale_productcode
        sale_productcode = StringVar()
        sale_productcode.set("To start transaction PRESS <F1>")
        ENTRY_SALE_PRODUCTCODE = Entry(FRAME_SEARCH_FORM, textvariable=sale_productcode, bg="#d0e9ec",
                                       font=("arial", 20, "bold"), bd=2, relief=GROOVE, width=50)
        ENTRY_SALE_PRODUCTCODE.place(relx=0.076, rely=0.16, relwidth=0.85, relheight=0.25)
        ENTRY_SALE_PRODUCTCODE.bind("<Return>", check_stock_code_clicked)
        ENTRY_SALE_PRODUCTCODE.bind("<KeyRelease>", check_stock_code)
        ENTRY_SALE_PRODUCTCODE.config(state="readonly")

        # ---- SEARCH FORM INNER FRAME ---#
        FRAME_SEARCH_FORM_INNER = Frame(FRAME_SEARCH_FORM, bg="white")
        FRAME_SEARCH_FORM_INNER.place(relx=0.06, rely=0.55, relwidth=0.415, relheight=0.6)

        # ---- PRODUCT ---#
        LABEL_SALE_PRODUCT = Label(FRAME_SEARCH_FORM_INNER, text="PRODUCT:", font=("arial", 9, "bold"), bg="white")
        LABEL_SALE_PRODUCT.grid(row=3, column=0, padx=12, sticky="w")

        global sale_product_var
        sale_product_var = StringVar()
        sale_product_var.set("-----")
        ENTRY_SALE_PRODUCT = Entry(FRAME_SEARCH_FORM_INNER, textvariable=sale_product_var, bg="#d0e9ec",
                                   font=("arial", 10, "bold"), state="readonly", bd=2, relief=GROOVE, width=26)
        ENTRY_SALE_PRODUCT.grid(row=3, column=1, ipady=2, sticky="w")

        # ---- DESCRIPTION ---#
        LABEL_SALE_DESCRIPTION = Label(FRAME_SEARCH_FORM_INNER, text="DESCRIPTION:", font=("arial", 9, "bold"),
                                       bg="white")
        LABEL_SALE_DESCRIPTION.grid(row=4, column=0, padx=12, sticky="w")

        global sale_description_var
        sale_description_var = StringVar()
        sale_description_var.set("-----")
        ENTRY_SALE_DESCRIPTION = Entry(FRAME_SEARCH_FORM_INNER, textvariable=sale_description_var, bg="#d0e9ec",
                                       font=("arial", 10, "bold"), state="readonly", bd=2, relief=GROOVE, width=26)
        ENTRY_SALE_DESCRIPTION.grid(row=4, column=1, ipady=2, pady=1)

        # ---- PRICE ---#
        LABEL_SALE_PRICE = Label(FRAME_SEARCH_FORM_INNER, text="PRICE:", font=("arial", 9, "bold"), bg="white")
        LABEL_SALE_PRICE.grid(row=5, column=0, padx=12, sticky="w")

        global sale_price_var
        sale_price_var = StringVar()
        sale_price_var.set("0.00")
        ENTRY_SALE_PRICE = Entry(FRAME_SEARCH_FORM_INNER, textvariable=sale_price_var, bg="#d0e9ec",
                                 font=("arial", 10, "bold"), state="readonly", bd=2, relief=GROOVE, width=26)
        ENTRY_SALE_PRICE.grid(row=5, column=1, ipady=2, pady=1)

        # ---- BILL FORM FRAME ---#
        FRAME_BILL_FORM = Frame(FRAME_SEARCH_FORM, bg="white")
        FRAME_BILL_FORM.place(relx=0.56, rely=0.55, relwidth=0.43, relheight=0.65)

        # ---- TOTAL AMOUNT ---#
        LABEL_SALE_TOTALAMOUNT = Label(FRAME_BILL_FORM, text="TOTAL AMOUNT:", font=("arial", 9, "bold"), bg="white")
        LABEL_SALE_TOTALAMOUNT.grid(row=0, column=0, sticky="w")

        global sale_totalaamount_var
        sale_totalaamount_var = StringVar()
        sale_totalaamount_var.set("0.00")
        ENTRY_SALE_TOTALAMOUNT = Entry(FRAME_BILL_FORM, textvariable=sale_totalaamount_var, bg="#d0e9ec",
                                       font=("arial", 10, "bold"), state="readonly", bd=2, relief=GROOVE, width=26)
        ENTRY_SALE_TOTALAMOUNT.grid(row=0, column=1, padx=10, ipady=2, pady=1)

        # ----AMOUNT PAID ---#
        LABEL_SALE_AMOUNTPAID = Label(FRAME_BILL_FORM, text="CASH:", font=("arial", 9, "bold"), bg="white")
        LABEL_SALE_AMOUNTPAID.grid(row=1, column=0, sticky="w")

        global sale_amountpaid_var
        sale_amountpaid_var = StringVar()
        sale_amountpaid_var.set("0.00")
        ENTRY_SALE_AMOUNTPAID = Entry(FRAME_BILL_FORM, textvariable=sale_amountpaid_var, bg="#d0e9ec",
                                      font=("arial", 10, "bold"), state="readonly", bd=2, relief=GROOVE, width=26)
        ENTRY_SALE_AMOUNTPAID.grid(row=1, column=1, padx=10, ipady=2, pady=1)

        # ----AMOUNT PAID ---#
        LABEL_SALE_BALANCE = Label(FRAME_BILL_FORM, text="CHANGE:", font=("arial", 9, "bold"), bg="white")
        LABEL_SALE_BALANCE.grid(row=2, column=0, sticky="w")

        global sale_balance_var
        sale_balance_var = StringVar()
        sale_balance_var.set("0.00")
        ENTRY_SALE_BALANCE = Entry(FRAME_BILL_FORM, textvariable=sale_balance_var, bg="#d0e9ec",
                                   font=("arial", 10, "bold"), state="readonly", bd=2, relief=GROOVE, width=26)
        ENTRY_SALE_BALANCE.grid(row=2, column=1, padx=10, ipady=2, pady=1)

        # ---- F1 ---#
        FRAME_F1 = Frame(FRAME_MAIN_INNER, bg="#b3b3b3")
        FRAME_F1.place(relx=0.03, rely=0.889, relwidth=0.1, relheight=0.105)

        FRAME_F1_INNER = Frame(FRAME_F1, bg="white")
        FRAME_F1_INNER.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

        LABEL_F1 = Label(FRAME_F1_INNER, text="F1", font=("algerian", 20, "normal"), bg="white")
        LABEL_F1.place(relx=0, rely=0.2, relwidth=1, relheight=0.3)

        LABEL_F1_TITLE1 = Label(FRAME_F1_INNER, text="Take order", font=("arial", 10, "normal"), bg="white")
        LABEL_F1_TITLE1.place(relx=0, rely=0.6, relwidth=1, relheight=0.3)

        # ---- F2 ---#
        FRAME_F2 = Frame(FRAME_MAIN_INNER, bg="#b3b3b3")
        FRAME_F2.place(relx=0.14, rely=0.889, relwidth=0.1, relheight=0.105)

        FRAME_F2_INNER = Frame(FRAME_F2, bg="white")
        FRAME_F2_INNER.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

        LABEL_F2 = Label(FRAME_F2_INNER, text="F2", font=("algerian", 20, "normal"), bg="white")
        LABEL_F2.place(relx=0, rely=0.2, relwidth=1, relheight=0.3)

        LABEL_F2_TITLE1 = Label(FRAME_F2_INNER, text="Add item", font=("arial", 10, "normal"), bg="white")
        LABEL_F2_TITLE1.place(relx=0, rely=0.6, relwidth=1, relheight=0.3)

        # ---- F3 ---#
        FRAME_F3 = Frame(FRAME_MAIN_INNER, bg="#b3b3b3")
        FRAME_F3.place(relx=0.25, rely=0.889, relwidth=0.1, relheight=0.105)

        FRAME_F3_INNER = Frame(FRAME_F3, bg="white")
        FRAME_F3_INNER.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

        LABEL_F3 = Label(FRAME_F3_INNER, text="F3", font=("algerian", 20, "normal"), bg="white")
        LABEL_F3.place(relx=0, rely=0.2, relwidth=1, relheight=0.3)

        LABEL_F3_TITLE1 = Label(FRAME_F3_INNER, text="Update qty", font=("arial", 10, "normal"), bg="white")
        LABEL_F3_TITLE1.place(relx=0, rely=0.6, relwidth=1, relheight=0.3)

        # ---- F4 ---#
        FRAME_F4 = Frame(FRAME_MAIN_INNER, bg="#b3b3b3")
        FRAME_F4.place(relx=0.36, rely=0.889, relwidth=0.1, relheight=0.105)

        FRAME_F4_INNER = Frame(FRAME_F4, bg="white")
        FRAME_F4_INNER.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

        LABEL_F4 = Label(FRAME_F4_INNER, text="F4", font=("algerian", 20, "normal"), bg="white")
        LABEL_F4.place(relx=0, rely=0.2, relwidth=1, relheight=0.3)

        LABEL_F4_TITLE1 = Label(FRAME_F4_INNER, text="Paid", font=("arial", 10, "normal"), bg="white")
        LABEL_F4_TITLE1.place(relx=0, rely=0.6, relwidth=1, relheight=0.3)

        # ---- F5 ---#
        FRAME_F5 = Frame(FRAME_MAIN_INNER, bg="#b3b3b3")
        FRAME_F5.place(relx=0.47, rely=0.889, relwidth=0.1, relheight=0.105)

        FRAME_F5_INNER = Frame(FRAME_F5, bg="white")
        FRAME_F5_INNER.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

        LABEL_F5 = Label(FRAME_F5_INNER, text="F5", font=("algerian", 20, "normal"), bg="white")
        LABEL_F5.place(relx=0, rely=0.2, relwidth=1, relheight=0.3)

        LABEL_F5_TITLE1 = Label(FRAME_F5_INNER, text="Save", font=("arial", 10, "normal"), bg="white")
        LABEL_F5_TITLE1.place(relx=0, rely=0.6, relwidth=1, relheight=0.3)

        # ---- F6 ---#
        FRAME_F6 = Frame(FRAME_MAIN_INNER, bg="#b3b3b3")
        FRAME_F6.place(relx=0.58, rely=0.889, relwidth=0.1, relheight=0.105)

        FRAME_F6_INNER = Frame(FRAME_F6, bg="white")
        FRAME_F6_INNER.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

        LABEL_F6 = Label(FRAME_F6_INNER, text="F6", font=("algerian", 20, "normal"), bg="white")
        LABEL_F6.place(relx=0, rely=0.2, relwidth=1, relheight=0.3)

        LABEL_F6_TITLE1 = Label(FRAME_F6_INNER, text="Customer", font=("arial", 10, "normal"), bg="white")
        LABEL_F6_TITLE1.place(relx=0, rely=0.6, relwidth=1, relheight=0.3)

        cashier_frame.focus_force()
        ENTRY_SALE_PRODUCTCODE.focus_force()
        cashier_frame.bind("<KeyPress>", sales_f_function)
        cashier_frame.geometry('%dx%d+%d+%d' % (config['WIDTH'], config['HEIGHT'], config['x'], config['y']))
        cashier_frame.wm_protocol("WM_DELETE_WINDOW", self.attemp_close_frame)
        cashier_frame.mainloop()

    def attemp_close_frame(self):
        if messagebox.askyesno("Confirmation message", "Are you sure you want to close this app?", parent=cashier_frame) == True:
            cashier_frame.destroy()
            ROOT.destroy()

    def modal_takeorder(self):
        global MODAL_TAKEORDER
        MODAL_TAKEORDER = Toplevel()
        config = self.window_config(MODAL_TAKEORDER, 500, 300)

        FRAME_TAKE_ORDER = Frame(MODAL_TAKEORDER, bg="white")
        FRAME_TAKE_ORDER.place(relx=0, rely=0, relheight=1, relwidth=2)

        global con_sukicard, icon_sukicard
        icon_sukicard = PhotoImage(file="icon/card.png")
        LABEL_SUKICARD = Label(MODAL_TAKEORDER, image=icon_sukicard, bg="white")
        LABEL_SUKICARD.place(relx=0.28, rely=0, relheight=0.4, relwidth=0.4)

        FRAME_QUISTION = Frame(FRAME_TAKE_ORDER, bg="#ddd")
        FRAME_QUISTION.place(relx=0, rely=0.4, relheight=0.4, relwidth=1)

        LABEL_SPACE = Label(FRAME_QUISTION, text="", font=("arial", 10), bg="#ddd")
        LABEL_SPACE.grid(row=0, column=0, padx=50)

        LABEL_QUISTION = Label(FRAME_QUISTION, text="DO YOU HAVE A SUKI CARD?", font=("arial", 20), bg="#ddd")
        LABEL_QUISTION.grid(row=1, column=0, padx=50)

        LABEL_QUISTION_RESPONSE = Label(FRAME_QUISTION, text="Press(Y/N).", font=("arial", 14), bg="#ddd")
        LABEL_QUISTION_RESPONSE.grid(row=2, column=0, padx=50)

        MODAL_TAKEORDER.grab_set()
        MODAL_TAKEORDER.bind("<KeyPress>", sales_yn_quistion)
        MODAL_TAKEORDER.focus_set()
        MODAL_TAKEORDER.bind_all('<Escape>', close_modal_customer_yesno)
        MODAL_TAKEORDER.geometry('%dx%d+%d+%d' % (config['WIDTH'], config['HEIGHT'], config['x'], config['y']))
        MODAL_TAKEORDER.protocol("WM_DELETE_WINDOW", onclose_modal_customer_yesno)

    def modal_cardno(self):
        global MODAL_CUSTOMER_VERIFY
        MODAL_CUSTOMER_VERIFY = Toplevel(cashier_frame)
        config = self.window_config(MODAL_CUSTOMER_VERIFY, 600, 400)

        # ----  MODAL USER TOP --- #
        FRAME_MODAL_CUSTOMER_VERIFY_TOP = Frame(MODAL_CUSTOMER_VERIFY, bg="#7fdb98")
        FRAME_MODAL_CUSTOMER_VERIFY_TOP.place(relx=0, rely=0, relwidth=1, relheight=0.12)

        ICON_CUSTOMER_VERIFY = PhotoImage(file="icon/register.png")
        LABEL_ICON_CUSTOMER_VERIFY = Label(FRAME_MODAL_CUSTOMER_VERIFY_TOP, image=ICON_CUSTOMER_VERIFY,
                                           bg="#7fdb98")
        LABEL_ICON_CUSTOMER_VERIFY.place(relx=0.21, rely=0.01, relwidth=0.08, relheight=1)

        LABEL_TOP_TITLE = Label(FRAME_MODAL_CUSTOMER_VERIFY_TOP, text="CUSTOMER VERIFICATION",
                                font=("algerian", 18), bg="#7fdb98")
        LABEL_TOP_TITLE.place(relx=0.28, rely=0.5, relwidth=0.48, relheight=1, anchor="w")

        # ---- MODAL USER BODY ---- #
        FRAME_MODAL_CUSTOMER_VERIFY_BODY = Frame(MODAL_CUSTOMER_VERIFY, bg="white")
        FRAME_MODAL_CUSTOMER_VERIFY_BODY.place(relx=0.106, rely=0.18, relwidth=0.8, relheight=0.72)

        global icon_sukicard
        icon_sukicard = PhotoImage(file="icon/card.png")
        LABEL_SUKICARD = Label(MODAL_CUSTOMER_VERIFY, image=icon_sukicard, bg="white")
        LABEL_SUKICARD.place(relx=0.3, rely=0.18, relheight=0.3, relwidth=0.4)

        FRAME_CUSTOMER_VERIFY_FORM = Frame(FRAME_MODAL_CUSTOMER_VERIFY_BODY, bg="white")
        FRAME_CUSTOMER_VERIFY_FORM.place(relx=0.1, rely=0.43, relwidth=1)

        LABEL_CARDNO = Label(FRAME_CUSTOMER_VERIFY_FORM, text="CARD NO:", font=("arial", 13, "bold"), bg="white")
        LABEL_CARDNO.grid(row=0, column=0, sticky="W")

        global customer_verify_cardno, ENTRY_CUSTOMER_VERIFY_CARDNO
        customer_verify_cardno = StringVar()
        ENTRY_CUSTOMER_VERIFY_CARDNO = Entry(FRAME_CUSTOMER_VERIFY_FORM, textvariable=customer_verify_cardno,
                                             bg="#d0e9ec", font=("arial", 13), width=42, bd=2, relief=GROOVE)
        ENTRY_CUSTOMER_VERIFY_CARDNO.grid(row=1, column=0, ipady=10, padx=4, pady=5)
        ENTRY_CUSTOMER_VERIFY_CARDNO.bind("<Return>", suki_no_inputted)

        ENTRY_CUSTOMER_VERIFY_CARDNO.focus_set()
        MODAL_TAKEORDER.grab_release()

        MODAL_CUSTOMER_VERIFY.grab_set()
        MODAL_CUSTOMER_VERIFY.bind_all("<Escape>", close_modal_customer_verify)
        MODAL_CUSTOMER_VERIFY.geometry(
            '%dx%d+%d+%d' % (config['WIDTH'], config['HEIGHT'], config['x'], config['y']))
        MODAL_CUSTOMER_VERIFY.protocol("WM_DELETE_WINDOW", onclose_modal_customer_verify)

    def modal_customer_registration(self):
        global MODAL_CUSTOMER_REGISTER
        MODAL_CUSTOMER_REGISTER = Toplevel()
        config = self.window_config(MODAL_CUSTOMER_REGISTER, 600, 600)

        # ----  MODAL USER TOP --- #
        global FRAME_MODAL_CUSTOMER_REGISTER_TOP
        FRAME_MODAL_CUSTOMER_REGISTER_TOP = Frame(MODAL_CUSTOMER_REGISTER, bg="#7fdb98")
        FRAME_MODAL_CUSTOMER_REGISTER_TOP.place(relx=0, rely=0, relwidth=1, relheight=0.12)

        global ICON_CUSTOMER_VERIFY
        ICON_CUSTOMER_VERIFY = PhotoImage(file="icon/register.png")
        LABEL_ICON_CUSTOMER_VERIFY = Label(FRAME_MODAL_CUSTOMER_REGISTER_TOP, image=ICON_CUSTOMER_VERIFY, bg="#7fdb98")
        LABEL_ICON_CUSTOMER_VERIFY.place(relx=0.21, rely=0.01, relwidth=0.08, relheight=1)

        LABEL_TOP_TITLE = Label(FRAME_MODAL_CUSTOMER_REGISTER_TOP, text="CUSTOMER REGISTRATION", font=("algerian", 18),
                                bg="#7fdb98")
        LABEL_TOP_TITLE.place(relx=0.28, rely=0.5, relwidth=0.48, relheight=1, anchor="w")

        # ---- MODAL USER BODY ---- #
        FRAME_MODAL_CUSTOMER_VERIFY_BODY = Frame(MODAL_CUSTOMER_REGISTER, bg="white")
        FRAME_MODAL_CUSTOMER_VERIFY_BODY.place(relx=0.106, rely=0.16, relwidth=0.8, relheight=0.8)

        FRAME_CUSTOMER_VERIFY_FORM = Frame(FRAME_MODAL_CUSTOMER_VERIFY_BODY, bg="white")
        FRAME_CUSTOMER_VERIFY_FORM.place(relx=0.1, rely=0.05, relwidth=1)

        # ---- CUSTOMER SUKI CARDNO ----- #
        global LABEL_CUSTOMER_CARDNO
        LABEL_CUSTOMER_CARDNO = Label(FRAME_CUSTOMER_VERIFY_FORM, text="Card no: ", font=("arial", 10, "bold"),
                                        bg="white")
        LABEL_CUSTOMER_CARDNO.grid(row=0, column=0, sticky="W")

        global customer_cardno_var, ENTRY_CUSTOMER_CARDNO
        customer_cardno_var = StringVar()
        ENTRY_CUSTOMER_CARDNO = Entry(FRAME_CUSTOMER_VERIFY_FORM, textvariable=customer_cardno_var,
                                        font=("arial", 10), width=38,
                                        bd=2, relief=GROOVE)
        ENTRY_CUSTOMER_CARDNO.grid(row=0, column=1, ipady=3, pady=5)
        ENTRY_CUSTOMER_CARDNO.bind("<FocusOut>", onkeypress_cardno)
        ENTRY_CUSTOMER_CARDNO.focus_force()

        global suki_reg_var, suki_reg
        suki_reg_var = IntVar()
        suki_reg_var.set(1)
        suki_reg = Checkbutton(FRAME_CUSTOMER_VERIFY_FORM, variable=suki_reg_var, bg="white", command=if_register_withsuki)
        suki_reg.grid(row=0, column=2, ipady=3, pady=5)

        # ---- CUSTOMER FIRSTNAME ----- #
        LABEL_CUSTOMER_FISTNAME = Label(FRAME_CUSTOMER_VERIFY_FORM, text="First name: * ", font=("arial", 10, "bold"),
                                        bg="white")
        LABEL_CUSTOMER_FISTNAME.grid(row=1, column=0, sticky="W")

        global customer_firstname_var, ENTRY_CUSTOMER_FISTNAME
        customer_firstname_var = StringVar()
        ENTRY_CUSTOMER_FISTNAME = Entry(FRAME_CUSTOMER_VERIFY_FORM, textvariable=customer_firstname_var,
                                        font=("arial", 10), width=38,
                                        bd=2, relief=GROOVE)
        ENTRY_CUSTOMER_FISTNAME.grid(row=1, column=1, ipady=3, pady=5)
        ENTRY_CUSTOMER_FISTNAME.bind("<Return>", checking_customer_ifexist)
        ENTRY_CUSTOMER_FISTNAME.bind("<KeyRelease>", onkeypress_custname)

        # ---- CUSTOMER MIDDLENAME ----- #
        LABEL_CUSTOMER_MIDDLENAME = Label(FRAME_CUSTOMER_VERIFY_FORM, text="Middle name: ", font=("arial", 10, "bold"),
                                          bg="white")
        LABEL_CUSTOMER_MIDDLENAME.grid(row=2, column=0, sticky="W")

        global customer_middlename_var, ENTRY_CUSTOMER_MIDDLENAME
        customer_middlename_var = StringVar()
        ENTRY_CUSTOMER_MIDDLENAME = Entry(FRAME_CUSTOMER_VERIFY_FORM, textvariable=customer_middlename_var,
                                          font=("arial", 10), width=38, bd=2, relief=GROOVE)
        ENTRY_CUSTOMER_MIDDLENAME.grid(row=2, column=1, ipady=3, pady=5)

        # ---- CUSTOMER LASTNAME ----- #
        LABEL_CUSTOMER_LASTNAME = Label(FRAME_CUSTOMER_VERIFY_FORM, text="Last name: * ", font=("arial", 10, "bold"),
                                        bg="white")
        LABEL_CUSTOMER_LASTNAME.grid(row=3, column=0, sticky="W")

        global customer_lastname_var, ENTRY_CUSTOMER_LASTNAME
        customer_lastname_var = StringVar()
        ENTRY_CUSTOMER_LASTNAME = Entry(FRAME_CUSTOMER_VERIFY_FORM, textvariable=customer_lastname_var,
                                        font=("arial", 10), width=38,
                                        bd=2,
                                        relief=GROOVE)
        ENTRY_CUSTOMER_LASTNAME.grid(row=3, column=1, ipady=3, pady=5)
        ENTRY_CUSTOMER_LASTNAME.bind("<Return>", checking_customer_ifexist)
        ENTRY_CUSTOMER_FISTNAME.bind("<KeyRelease>", onkeypress_custname)

        # ---- CUSTOMER ADDRESS ----- #
        LABEL_CUSTOMER_ADDRESS = Label(FRAME_CUSTOMER_VERIFY_FORM, text="Address: ", font=("arial", 10, "bold"),
                                       bg="white")
        LABEL_CUSTOMER_ADDRESS.grid(row=4, column=0, sticky="W")

        global customer_address_var, ENTRY_CUSTOMER_ADDRESS
        customer_address_var = StringVar()
        ENTRY_CUSTOMER_ADDRESS = Entry(FRAME_CUSTOMER_VERIFY_FORM, textvariable=customer_address_var,
                                       font=("arial", 10), width=38, bd=2, relief=GROOVE)
        ENTRY_CUSTOMER_ADDRESS.grid(row=4, column=1, ipady=3, pady=5)

        # ---- CUSTOMER GENDER ----- #
        LABEL_CUSTOMER_GENDER = Label(FRAME_CUSTOMER_VERIFY_FORM, text="Gender:", font=("arial", 10, "bold"),
                                      bg="white")
        LABEL_CUSTOMER_GENDER.grid(row=5, column=0, sticky="W")

        global customer_gender_var, COMBOBOX_CUSTOMER_GENDER
        customer_gender_var = StringVar()
        gender_list = ["MALE", "FEMALE"]
        customer_gender_var.set(gender_list[0])
        COMBOBOX_CUSTOMER_GENDER = ttk.Combobox(FRAME_CUSTOMER_VERIFY_FORM, textvariable=customer_gender_var,
                                                state="readonly", font=("arial", 10), width=35)
        COMBOBOX_CUSTOMER_GENDER['values'] = gender_list
        COMBOBOX_CUSTOMER_GENDER.grid(row=5, column=1, ipady=3, pady=5)

        # ---- CUSTOMER BIRTHDAY ----- #
        LABEL_CUSTOMER_BIRTHDAY = Label(FRAME_CUSTOMER_VERIFY_FORM, text="Birthday: ", font=("arial", 10, "bold"),
                                        bg="white")
        LABEL_CUSTOMER_BIRTHDAY.grid(row=6, column=0, sticky="W")

        global customer_birthday_var, ENTRY_CUSTOMER_BIRTHDAY
        customer_birthday_var = StringVar()
        ENTRY_CUSTOMER_BIRTHDAY = DateEntry(FRAME_CUSTOMER_VERIFY_FORM, textvariable=customer_birthday_var,
                                            font=("arial", 10), width=35, bd=2, relief=GROOVE, state="readonly", locale='en_US', date_pattern='y-mm-dd')
        ENTRY_CUSTOMER_BIRTHDAY.grid(row=6, column=1, ipady=3, pady=5)


        # ---- CUSTOMER CONTACT ----- #
        LABEL_CUSTOMER_CONTACT = Label(FRAME_CUSTOMER_VERIFY_FORM, text="Contact No:", font=("arial", 10, "bold"),
                                       bg="white")
        LABEL_CUSTOMER_CONTACT.grid(row=7, column=0, sticky="W")

        global customer_contact_var, ENTRY_CUSTOMER_CONTACT
        customer_contact_var = StringVar()
        ENTRY_CUSTOMER_CONTACT = Entry(FRAME_CUSTOMER_VERIFY_FORM, textvariable=customer_contact_var,
                                       font=("arial", 10), width=38, bd=2, relief=GROOVE)
        ENTRY_CUSTOMER_CONTACT.grid(row=7, column=1, ipady=3, pady=5)

        # ---- CUSTOMER WORK ----- #
        LABEL_CUSTOMER_WORK = Label(FRAME_CUSTOMER_VERIFY_FORM, text="Work:", font=("arial", 10, "bold"),
                                    bg="white")
        LABEL_CUSTOMER_WORK.grid(row=8, column=0, sticky="W")

        global customer_work_var, ENTRY_CUSTOMER_WORK
        customer_work_var = StringVar()
        ENTRY_CUSTOMER_WORK = Entry(FRAME_CUSTOMER_VERIFY_FORM, textvariable=customer_work_var,
                                    font=("arial", 10), width=38, bd=2, relief=GROOVE)
        ENTRY_CUSTOMER_WORK.grid(row=8, column=1, ipady=3, pady=5)

        # ---- CUSTOMER EMAIL ----- #
        LABEL_CUSTOMER_EMAIL = Label(FRAME_CUSTOMER_VERIFY_FORM, text="Email:", font=("arial", 10, "bold"),
                                     bg="white")
        LABEL_CUSTOMER_EMAIL.grid(row=9, column=0, sticky="W")

        global customer_email_var, ENTRY_CUSTOMER_EMAIL
        customer_email_var = StringVar()
        ENTRY_CUSTOMER_EMAIL = Entry(FRAME_CUSTOMER_VERIFY_FORM, textvariable=customer_email_var,
                                     font=("arial", 10), width=38, bd=2, relief=GROOVE)
        ENTRY_CUSTOMER_EMAIL.grid(row=9, column=1, ipady=3, pady=5)

        # ---- FRAME CANCEL AND SUBMIT -----#
        global FRAME_CUSTOMER_BUTTONS
        FRAME_CUSTOMER_BUTTONS = Frame(MODAL_CUSTOMER_REGISTER, bg="white")
        FRAME_CUSTOMER_BUTTONS.place(relx=0.15, rely=0.84)

        # cancel button
        global btn_prev, btn_next
        btn_prev = Button(FRAME_CUSTOMER_BUTTONS, text="< prev", width=7, bg='lightblue', fg="Black",
                          font=("arial", 10), relief=GROOVE, command=lambda: find_prev_customer(self))
        btn_prev.pack(side=LEFT, pady=15, padx=8, ipady=2)
        btn_prev.bind("<Return>", find_prev_customer)

        btn_next = Button(FRAME_CUSTOMER_BUTTONS, text="Next >", width=7, bg='lightblue', fg="Black",
                          font=("arial", 10), relief=GROOVE, command=lambda: find_next_customer(self))
        btn_next.pack(side=LEFT, pady=15, padx=8, ipady=2)
        btn_next.bind("<Return>", find_next_customer)

        btn_prev.config(state="disable")
        btn_next.config(state="disable")

        global USER_BUTTON_CANCEL
        USER_BUTTON_CANCEL = Button(FRAME_CUSTOMER_BUTTONS, text="CANCEL", width=10, bg='red', fg="white",
                                    font=("arial", 11), relief=GROOVE)
        USER_BUTTON_CANCEL.pack(side=LEFT, pady=15, padx=10, ipady=2)
        USER_BUTTON_CANCEL.bind("<Button-1>", customer_cancel)
        USER_BUTTON_CANCEL.bind("<Return>", customer_cancel)

        # submit button
        global USER_BUTTON_SAVE
        USER_BUTTON_SAVE = Button(FRAME_CUSTOMER_BUTTONS, text="SUBMIT", width=10, bg="blue", fg="white",
                                  font=("arial", 11), relief=GROOVE)
        USER_BUTTON_SAVE.pack(side=LEFT, padx=10, ipady=2)
        USER_BUTTON_SAVE.bind("<Button-1>", customer_submit)
        USER_BUTTON_SAVE.bind("<Return>", customer_submit)

        MODAL_CUSTOMER_REGISTER.grab_set()
        MODAL_CUSTOMER_REGISTER.bind_all("<Escape>", close_modal_customer_info)
        MODAL_CUSTOMER_REGISTER.geometry('%dx%d+%d+%d' % (config['WIDTH'], config['HEIGHT'], config['x'], config['y']))
        MODAL_CUSTOMER_REGISTER.protocol("WM_DELETE_WINDOW", onclose_modal_customer_info)

    def modal_updateqty(self, event):
        if TREE_ORDERLIST.item(TREE_ORDERLIST.get_children()[0])['values'][3] == "":
            return False

        item = TREE_ORDERLIST.selection()
        product_id = TREE_ORDERLIST.item(item)['values'][3]

        global MODAL_UPDATEQTY
        MODAL_UPDATEQTY = Toplevel()
        config = self.window_config(MODAL_UPDATEQTY, 500, 300)

        FRAME_UPDATEQTY = Frame(MODAL_UPDATEQTY, bg="white")
        FRAME_UPDATEQTY.place(relx=0, rely=0, relheight=1, relwidth=2)

        global icon_qty
        icon_qty = PhotoImage(file="icon/qty_cart.png")
        LABEL_ICON__QTY = Label(MODAL_UPDATEQTY, image=icon_qty, bg="white")
        LABEL_ICON__QTY.place(relx=0.29, rely=0, relheight=0.4, relwidth=0.4)

        FRAME_QTY = Frame(FRAME_UPDATEQTY, bg="#ddd")
        FRAME_QTY.place(relx=0, rely=0.4, relheight=0.4, relwidth=1)

        LABEL_SPACE = Label(FRAME_QTY, text="", font=("arial", 10), bg="#ddd")
        LABEL_SPACE.grid(row=0, column=0, padx=36)

        LABEL_QTY = Label(FRAME_QTY, text="QUANTITY:", font=("arial", 20), bg="#ddd")
        LABEL_QTY.grid(row=1, column=0, padx=36, sticky="w")

        global qty_var, ENTRY_QTY
        qty_var = StringVar()
        ENTRY_QTY = Entry(FRAME_QTY, textvariable=qty_var, font=("arial", 20), justify="center", width=28, bg="#d0e9ec")
        ENTRY_QTY.grid(row=2, column=0, ipady=3, padx=38)
        ENTRY_QTY.bind("<KeyRelease>", sales_qty_validation)
        ENTRY_QTY.bind("<Return>", lambda event: update_qty_enter(event, item))
        ENTRY_QTY.focus_set()

        FRAME_UPDATEQTY.grab_set()
        FRAME_UPDATEQTY.bind_all("<Escape>", hide_modal_updateqty)
        MODAL_UPDATEQTY.geometry('%dx%d+%d+%d' % (config['WIDTH'], config['HEIGHT'], config['x'], config['y']))

    def modal_cashinput(self):
        global MODAL_CASH
        MODAL_CASH = Toplevel()
        config = self.window_config(MODAL_CASH, 500, 300)

        FRAME_CASH = Frame(MODAL_CASH, bg="white")
        FRAME_CASH.place(relx=0, rely=0, relheight=1, relwidth=2)

        global icon_qty
        icon_qty = PhotoImage(file="icon/cash.png")
        LABEL_ICON__CASH = Label(MODAL_CASH, image=icon_qty, bg="white")
        LABEL_ICON__CASH.place(relx=0.29, rely=0, relheight=0.4, relwidth=0.4)

        FRAME_CASH_BODY = Frame(FRAME_CASH, bg="#ddd")
        FRAME_CASH_BODY.place(relx=0, rely=0.4, relheight=0.4, relwidth=1)

        LABEL_SPACE = Label(FRAME_CASH_BODY, text="", font=("arial", 10), bg="#ddd")
        LABEL_SPACE.grid(row=0, column=0, padx=36)

        LABEL_CASH_ENTRY = Label(FRAME_CASH_BODY, text="Input cash:", font=("arial", 20), bg="#ddd")
        LABEL_CASH_ENTRY.grid(row=1, column=0, padx=36, sticky="w")

        global input_cash_var
        input_cash_var = StringVar()
        ENTRY_CASH = Entry(FRAME_CASH_BODY, textvariable=input_cash_var, font=("arial", 20), justify="center", width=28,
                           bg="#d0e9ec")
        ENTRY_CASH.grid(row=2, column=0, ipady=3, padx=38)
        ENTRY_CASH.bind("<Return>", cash_inputted)
        ENTRY_CASH.focus_set()

        FRAME_CASH.grab_set()
        MODAL_CASH.geometry('%dx%d+%d+%d' % (config['WIDTH'], config['HEIGHT'], config['x'], config['y']))
        MODAL_CASH.bind_all("<Escape>", hide_modal_cashinput)

    def window_config(self, frame, WIDTH, HEIGHT):
        frame.title("STORE INVENTORY SYSTEM")
        ws = frame.winfo_screenwidth()
        hs = frame.winfo_screenheight()
        x = (ws / 2) - (WIDTH / 2)
        y = (hs / 2) - (HEIGHT / 2)
        frame.resizable(False, False)
        frame.iconbitmap('icon/system_logo.ico')
        frame.config(bg="#ddd")

        return {
            "WIDTH": WIDTH,
            "HEIGHT":
                HEIGHT,
            "x": x,

            "y": y
        }

    def gui_footer(self, frame):
        frame_bottom = Frame(frame, bg="white")
        frame_bottom.place(relx=0, rely=0.96, relwidth=1, relheight=0.04)

        label_author = Label(frame_bottom, text="Copyright @ 2019 || SIS. All rights reserved.", bg="white")
        label_author.pack()

        label_version = Label(frame_bottom, text="Version: 1.0.", bg="white")
        label_version.place(relx=0.91, y=0)

    def logout(self):
        choice = messagebox.askquestion("Confirmation message", "Are you sure you want to logout?", icon='warning',
                                        parent=cashier_frame)
        if choice == "yes":
            cashier_frame.destroy()
            ROOT.update()
            ROOT.deiconify()
            login_cancel()


"""
#====================================================================================================================#
#-----------------------            CASHIER FUNCTIONALITY AREA                                -----------------------#
#====================================================================================================================#
"""


# -------- YES OR NO SUKI CARD -------- #
def sales_yn_quistion(event):
    global MODAL_TAKEORDER, ENTRY_SALE_PRODUCTCODE

    if event.keysym.lower() == "y":
        login.if_no_suki_ask = False
        MODAL_TAKEORDER.destroy()
        cashier.modal_cardno()

    elif event.keysym.lower() == "n":
        login.if_no_suki_ask = False
        MODAL_TAKEORDER.destroy()
        cashier.modal_customer_registration()
        ENTRY_CUSTOMER_CARDNO.grid_forget()
        LABEL_CUSTOMER_CARDNO.grid_forget()
        suki_reg.grid_forget()


# -------- CUSTOMER -------- #
def customer_cancel(event):
    customer_firstname_var.set("")
    customer_middlename_var.set("")
    customer_lastname_var.set("")
    customer_gender_var.set("Male")
    customer_address_var.set("")
    customer_birthday_var.set("")
    customer_contact_var.set("")
    customer_work_var.set("")
    customer_email_var.set("")
    login.customer_reg_open = False
    MODAL_CUSTOMER_REGISTER.destroy()


def customer_submit(event):
    email = customer_email_var.get()
    work = customer_work_var.get()
    contact = customer_contact_var.get()
    bday = customer_birthday_var.get()
    address = customer_address_var.get()
    gender = customer_gender_var.get()
    lname = customer_lastname_var.get()
    mname = customer_middlename_var.get()
    fname = customer_firstname_var.get()

    error = ""
    if fname == "" or lname == "":
        if fname == "":
            error += "First Name Required!\n"

        if lname == "":
            error += "Last Name Required!\n"

        messagebox.showwarning("Required", error, parent=cashier_frame)
        return False

    lastid, resp = controller.add_customer(fname, mname, lname, gender, address, bday, contact, work, email)

    if resp > 0:
        customer_cancel(event)
        MODAL_CUSTOMER_REGISTER.destroy()
        messagebox.showinfo("Success message", "New customer added!.", parent=cashier_frame)
        get_user_info(lastid)
        login.customer_reg_open = False

    else:
        messagebox.showerror("Error message", "Failed to add customer", parent=cashier_frame)

    check_if_trans_start(False)



# -------- get user info using id -------------#
def get_user_info(lastid):
    if login.if_no_suki_ask == False:
        login.cust_id_current = lastid

def if_register_withsuki():
    if suki_reg_var.get() == 0:
        customer_cardno_var.set("")
        ENTRY_CUSTOMER_CARDNO.config(state='disable')
    else:
        ENTRY_CUSTOMER_CARDNO.config(state='normal')
        ENTRY_CUSTOMER_CARDNO.focus_force()

def onkeypress_cardno(event):
    if suki_reg_var.get() == 0:
        return False

    cardno = customer_cardno_var.get()
    result = controller.check_cust_cardno(cardno)


    if len(result) > 0 and result[0]['customer_id'] != None:
        messagebox.showwarning("Warning", "Suki card is not available!", parent=MODAL_CUSTOMER_REGISTER)
        ENTRY_CUSTOMER_CARDNO.focus_force()
        ENTRY_CUSTOMER_CARDNO.select_range(0, END)
        return False

    elif len(result) == 0:
        messagebox.showwarning("Warning", "Invalid suki card!", parent=MODAL_CUSTOMER_REGISTER)
        ENTRY_CUSTOMER_CARDNO.focus_force()
        ENTRY_CUSTOMER_CARDNO.select_range(0, END)
        return False


def onkeypress_custname(event):
    btn_prev.config(state="disable")
    btn_next.config(state="disable")

def checking_customer_ifexist(event):
    login.customer_prev_id = 0
    login.lname = customer_lastname_var.get()
    login.fname = customer_firstname_var.get()
    login.cust_all_list = controller.checking_customer_ifexist(login.fname, login.lname)

    if len(login.cust_all_list) <= 0:
        customer_birthday_var.set(date.today())
        customer_address_var.set("")
        customer_email_var.set("")
        customer_work_var.set("")
        customer_contact_var.set("")
        customer_gender_var.set("MALE")
        customer_middlename_var.set("")
        messagebox.showwarning("Empty", "No records found!", parent=MODAL_CUSTOMER_REGISTER)

        return False

    find_next_customer(event)
    btn_next.focus_force()
    btn_prev.config(state="normal")
    btn_next.config(state="normal")



prev_list = {}
def find_next_customer(event):
    lists = controller.checking_customer_ifexist_next(login.fname, login.lname, login.customer_prev_id)

    if len(lists) <= 0:
        messagebox.showwarning("Last", "This is the last Records", parent=MODAL_CUSTOMER_REGISTER)
        return False

    login.customer_prev_id += 1 # lists[0]['customer_id']
    finding_customer(lists)

def find_prev_customer(event):
    lists = controller.checking_customer_ifexist_prev(login.fname, login.lname, login.customer_prev_id)

    if len(lists) <= 0:
        messagebox.showwarning("First", "This is the first Records", parent=MODAL_CUSTOMER_REGISTER)
        return False

    login.customer_prev_id -= 1 # lists[0]['customer_id']
    finding_customer(lists)

def finding_customer(lists):
    if len(lists) > 0:
        data = lists[0]
        customer_lastname_var.set(data['customer_lname'])
        customer_firstname_var.set(data['customer_fname'])
        customer_birthday_var.set(data['customer_birthday'])
        customer_address_var.set(data['customer_address'])
        customer_email_var.set(data['customer_email'])
        customer_work_var.set(data['customer_work'])
        customer_contact_var.set(data['customer_contact'])
        customer_gender_var.set(data['customer_gender'])
        customer_middlename_var.set(data['customer_mname'])
    else:
        customer_birthday_var.set(date.today())
        customer_address_var.set("")
        customer_email_var.set("")
        customer_work_var.set("")
        customer_contact_var.set("")
        customer_gender_var.set("MALE")
        customer_middlename_var.set("")



# -------- RESET CUSTOMER TRANSACTION -------- #
def reset_transaction():
    for row in TREE_ORDERLIST.get_children():
        TREE_ORDERLIST.delete(row)

    TREE_ORDERLIST.insert('', 'end', text="No Record", values=["---", "---", "---", ""])
    product_stock_list.clear()
    sale_product_var.set("-----")
    sale_description_var.set("-----")
    sale_price_var.set("0.00")
    sale_productcode.set("")
    sale_totalaamount_var.set("0.00")
    sale_balance_var.set("0.00")
    sale_amountpaid_var.set("0.00")

    ENTRY_SALE_PRODUCTCODE.config(state="readonly")
    sale_productcode.set("To start transaction PRESS <F1>")


# -------- GET SUKI CARD NO -------- #
def suki_no_inputted(event):
    suki_no = customer_verify_cardno.get()

    result = controller.get_user_info_using_suki(suki_no)
    if len(result) > 0:
        login.cust_id_current = result[0]['customer_id']
        check_if_trans_start(login.cust_id_current)
        close_modal_customer_verify(event)
        check_if_trans_start(False)

    elif len(result) == 0:
        messagebox.showwarning("Warning message", "Suki card not found!", parent=cashier_frame)
        return False

    else:
        messagebox.showerror("Error message", "Something went wrong!", parent=cashier_frame)
        return False


#------ Check if user is attemp to start the transaction by pressing <F1> -------#
def check_if_trans_start(data):
    if login.if_no_suki_ask != None:
        ENTRY_SALE_PRODUCTCODE.config(state="normal")
        ENTRY_SALE_PRODUCTCODE.focus_set()
        sale_productcode.set("")
        login.trans_start = True
    else:
        ENTRY_SALE_PRODUCTCODE.config(state="readonly")
        sale_productcode.set("To Start Transaction PRESS <F1>")

# -------- WHEN ENTER QUANTITY UPDATE -------- #
def update_qty_enter(event, selected_row):
    global qty_var, MODAL_UPDATEQTY
    values = TREE_ORDERLIST.item(selected_row)['values']
    product_id = values[3]
    price = values[0]
    quant = values[1]
    amount = values[2]

    if qty_var.get().isnumeric():
        qty = qty_var.get()
        new_amount = float(qty) * float(price)
        current_total = float(sale_totalaamount_var.get()) - float(amount)

        avail_qty = check_quantity_left(product_id)
        if avail_qty < int(qty):
            ENTRY_QTY.select_range(0, END)
            if avail_qty == 0:
                messagebox.showwarning("Warning message", "Out of stock", parent=cashier_frame)
                ENTRY_QTY.select_range(0, END)
                return False
            messagebox.showwarning("Warning message", "Not enough Stock, Stock Available: ({})".format(avail_qty),
                                   parent=cashier_frame)
            return False

        sale_totalaamount_var.set("{:.2f}".format(current_total + new_amount))
        #sale_balance_var.set("{:.2f}".format(float(sale_amountpaid_var.get()) - (current_total + new_amount)))
        TREE_ORDERLIST.item(selected_row, values=(price, qty, "{:.2f}".format(new_amount), product_id))
        MODAL_UPDATEQTY.destroy()


# -------- CHECK STOCK CODE IN DATABASE BY ENTER -------- #
product_stock_list = []


def check_stock_code(event):
    code = ENTRY_SALE_PRODUCTCODE.get()
    result = controller.check_stock_no(code)
    product_stock_list.clear()
    if len(result) > 0:
        product_stock_list.append(result)
        sale_product_var.set(result[0]['product_name'])
        sale_description_var.set(result[0]['product_details'])
        sale_price_var.set("{:.2f}".format(result[0]['stock_price']))

    else:
        sale_product_var.set("-----")
        sale_description_var.set("-----")
        sale_price_var.set("0.00")


# -------- CHECK STOCK CODE IN DATABASE BY CLICK -------- #
def check_stock_code_clicked(event):
    if sale_productcode.get() == "To Start Transaction PRESS <F1>":
        return False

    if len(product_stock_list) == 0:
        messagebox.showinfo("Information message", "No product found with this code!", parent=cashier_frame)
        return False

    if_exist = False
    all_total = 0
    name = product_stock_list[0][0]['product_name']
    price = product_stock_list[0][0]['stock_price']
    product_id = product_stock_list[0][0]['product_id']

    # ---- Check if the quantity inputted if lower or equal to stock ----#
    avail_qty = check_quantity_left(product_id)
    if avail_qty == 0:
        messagebox.showwarning("Warning message", "Out of stock", parent=cashier_frame)
        return False

    if TREE_ORDERLIST.item(TREE_ORDERLIST.get_children()[0])['values'][3] == "":
        TREE_ORDERLIST.delete(TREE_ORDERLIST.get_children()[0])

    for row in TREE_ORDERLIST.get_children():
        prodid = TREE_ORDERLIST.item(row)['values'][3]
        quan = TREE_ORDERLIST.item(row)['values'][1]
        qnty = int(quan) + 1
        tot = float(price) * qnty

        if str(prodid) == str(product_id):
            TREE_ORDERLIST.selection_set(row)
            TREE_ORDERLIST.focus(row)

            # ---- Check if the quantity inputted by the user is enough ----#
            if avail_qty < qnty:
                messagebox.showwarning("Warning message", "Not enough Stock, Stock Available: ({})".format(avail_qty),
                                       parent=cashier_frame)
                return False

            TREE_ORDERLIST.item(row, values=(price, qnty, "{:.2f}".format(tot), product_id))
            if_exist = True

        total = TREE_ORDERLIST.item(row)['values'][2]
        all_total += float(total)

    if if_exist == False:
        TREE_ORDERLIST.insert('', 'end', text=name, values=[price, 1, "{:.2f}".format(price), product_id])
        TREE_ORDERLIST.selection_set(TREE_ORDERLIST.get_children()[-1])
        TREE_ORDERLIST.focus(TREE_ORDERLIST.get_children()[-1])
        all_total += float(price)

    sale_totalaamount_var.set("{:.2f}".format(all_total))
    #sale_balance_var.set("{:.2f}".format(float(sale_amountpaid_var.get()) - all_total))


# -------- GET CASH INPUTTED BY ENTER -------- #
def cash_inputted(event):
    try:
        cash = float(input_cash_var.get())
    except ValueError:
        messagebox.showerror("Error message", "Input a valid amount!", parent=cashier_frame)
        return False

    amnt = float(sale_totalaamount_var.get())
    if cash < amnt:
        messagebox.showerror("Error message", "Not enough cash", parent=cashier_frame)
        return False

    sale_amountpaid_var.set("{:.2f}".format(cash))

    remain = cash - amnt
    sale_balance_var.set("{:.2f}".format(remain))
    hide_modal_cashinput(event)


# -------- QUANTITY VALIDATION AND UPDATE -------- #
def sales_qty_validation(event):
    global qty_var
    temp = qty_var.get()
    vv = ""
    for x in temp:
        if x.isnumeric():
            vv += x

    qty_var.set(vv)


# -------- CHECK THE QUANITY IN DATABASE IF ENOUGH TO PURCHASE -------- #
def check_quantity_left(product_id):
    rows, sales = controller.search_inventory(product_id)
    array = {}
    sale_non = 0
    for row in rows:
        array[row['product_id']] = [{
            'qnty': row['total_qty'],
            'sale': 0,
            'qnty_left': row['total_qty']
        }]
        sale_non = row['total_qty']

    for sale in sales:
        left = int(array[sale['product_id']][0]['qnty']) - int(sale['sale_quan'])
        return left

    else:
        return int(sale_non)


def hide_modal_cashinput(event):
    MODAL_CASH.destroy()

def hide_modal_updateqty(event):
    MODAL_UPDATEQTY.destroy()

def close_modal_customer_verify(event):
    MODAL_CUSTOMER_VERIFY.destroy()

def onclose_modal_customer_verify():
    MODAL_CUSTOMER_VERIFY.destroy()

def close_modal_customer_info(event):
    login.customer_reg_open = False
    MODAL_CUSTOMER_REGISTER.destroy()


def onclose_modal_customer_info():
    login.customer_reg_open = False
    MODAL_CUSTOMER_REGISTER.destroy()


def close_modal_customer_yesno(event):
    MODAL_TAKEORDER.destroy()


def onclose_modal_customer_yesno():
    MODAL_TAKEORDER.destroy()


# -------- KEYBOARD F FUNCTION KEY -------- #
def sales_f_function(event):
    if event.keysym == "F1":
        if login.trans_start == True:
            return False

        if login.customer_reg_open == True:
            return False

        if float(sale_amountpaid_var.get()) == 0 and float(sale_totalaamount_var.get()) > 0:
            messagebox.showwarning("Warning", "Please complete the current transaction!", parent=cashier_frame)
            return False

        elif float(sale_amountpaid_var.get()) != 0:
            if messagebox.askyesno("Warning",
                                   "Transaction is not yet done!\n\nWould you like to CANCEL the current transaction?",
                                   parent=cashier_frame):
                reset_transaction()

            else:
                return False

        cashier.modal_takeorder()

    elif event.keysym == "F2":
        if sale_productcode.get() == "To start transaction PRESS <F1>":
            return False

        ENTRY_SALE_PRODUCTCODE.selection_range(0, END)
        ENTRY_SALE_PRODUCTCODE.focus_set()

    elif event.keysym == "F3":
        if sale_productcode.get() == "To start transaction PRESS <F1>":
            return False

        if TREE_ORDERLIST.item(TREE_ORDERLIST.get_children()[0])['values'][3] == "":
            messagebox.showwarning("Warning message", "No item to update", parent=cashier_frame)
            return False

        child_id = TREE_ORDERLIST.get_children()[0]  # for instance the last element in tuple
        TREE_ORDERLIST.selection_set(child_id)
        TREE_ORDERLIST.focus_set()
        TREE_ORDERLIST.focus(child_id)

    elif event.keysym == "F4":
        if sale_productcode.get() == "To start transaction PRESS <F1>":
            return False

        if float(sale_totalaamount_var.get()) == 0:
            messagebox.showwarning("Warning message", "Make a purchase first!", parent=cashier_frame)
            return False
        cashier.modal_cashinput()

    elif event.keysym == "F5":
        tot = sale_totalaamount_var.get()
        cash = sale_amountpaid_var.get()

        if float(tot) > float(cash):
            messagebox.showwarning("Warning message", "Insufficient Cash!", parent=cashier_frame)
            return False

        if sale_productcode.get() == "To Start Transaction PRESS <F1>":
            return False

        if float(sale_totalaamount_var.get()) == 0:
            messagebox.showwarning("Warning message", "Make a purchase first!", parent=cashier_frame)
            return False

        elif float(sale_amountpaid_var.get()) == 0:
            messagebox.showwarning("Warning message", "Press F4: Paid the purchased first!", parent=cashier_frame)
            return False

        else:
            if messagebox.askyesno("Confirmation message", "Are you sure to save this transaction?", parent=cashier_frame) == False:
                return False

        last_id, resp = controller.add_invoice_sale(login.cust_id_current)

        if resp == 0:
            messagebox.showerror("Error message", "This transaction has a problem", parent=cashier_frame)
            return False

        for row in TREE_ORDERLIST.get_children():
            values = TREE_ORDERLIST.item(row)['values']
            prodid = values[3]
            sale_price = values[0]
            sale_qnty = values[1]
            # sale_total = values[2]

            last_sale_id, sale_resp = controller.save_sale_product(prodid, sale_price, sale_qnty, last_id)
        messagebox.showinfo("Success message", "Transaction successfully save.", parent=cashier_frame)
        login.trans_start = False
        reset_transaction()

    elif event.keysym == "F6":
        if login.trans_start == True:
            return False

        login.if_no_suki_ask = None
        login.customer_reg_open = True
        cashier.modal_customer_registration()

    elif event.keysym == "Escape":
        pass


cashier = Cashier()
login = Login()
login.show()
