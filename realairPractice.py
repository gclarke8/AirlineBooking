import tkinter as tk
from tkinter import END

adminUser = False

seatReservation = {}

totalRating = 0.0
totalPersonRated = 0

winSize = "600x650"


def saveSeat(button):
    gi = button.grid_info()
    x = gi['row']
    y = gi['column']
    print(x, y)
    index = x * 6 + y
    if index in seatReservation.keys():
        return
    seatReservation[index] = True
    button.configure(bg="red", state="disabled")
    # button.grid_forget()


def addDropdown(toWindow, optionList):
    vr = tk.StringVar(toWindow)
    vr.set(optionList[0])
    opt = tk.OptionMenu(toWindow, vr, *optionList)
    opt.config(width=90, font=('Helvetica', 12))
    opt.pack()


def displayRows():
    global b
    new_win = tk.Tk()
    new_win.geometry(winSize)
    new_win.configure(bg='light blue')

    seat_counter = 1
    for x in range(20):
        for y in range(6):
            # print('creating seat %d' % seat_counter)

            b = tk.Button(new_win, text='Seat: %d' % seat_counter,
                          name='seat: %d' % seat_counter, width=8, height=1)

            index = seat_counter - 1
            if index not in seatReservation.keys() or not seatReservation[index]:
                b.configure(command=lambda button=b: saveSeat(button))
            else:
                b.configure(command=lambda button=b: saveSeat(button), bg='red')

            # doesn't matter that the columns won't line up
            b.grid(row=x, column=y)
            seat_counter += 1

    global adminUser
    if adminUser:
        avg = 0
        if totalPersonRated > 0:
            avg = round(totalRating / totalPersonRated, 1)
        w = tk.Label(new_win, text="Avg Rating: %d" % avg, bg='green')
        w.grid(row=20, column=1)

    center(new_win)


def addRating():
    global totalRating
    global totalPersonRated
    rating = vr1.get()
    ratingList = ["5 star", "4 star", "3 star", "2 star", "1 star"]
    indexOf = ratingList.index(rating)
    ratingValue = 5 - indexOf
    print(ratingValue)
    totalRating += ratingValue
    totalPersonRated += 1


class MyOptionMenu(tk.OptionMenu):
    def __init__(self, master, status, *options):
        self.var = tk.StringVar(master)
        self.var.set(status)
        tk.OptionMenu.__init__(self, master, self.var, *options)
        self.config(font=('calibri',(10)),bg='white',width=12)
        self['menu'].config(font=('calibri',(10)),bg='white')


def guestUser():
    # win.destroy()
    guestUserWin = tk.Tk()
    guestUserWin.geometry(winSize)

    OptionList = ["Business Select", "Business (Regular)", "Family(1 Child)", "Family(2 Children)",
                  "Family(3 Children)", "Tourist"]
    vr = tk.StringVar(guestUserWin)
    vr.set(OptionList[0])
    opt = tk.OptionMenu(guestUserWin, vr, *OptionList)
    opt.config(width=90, font=('Helvetica', 12))
    opt.pack(side="top")

    confirm_btn = tk.Button(guestUserWin, text="Confirm", command=displayRows)
    confirm_btn.pack()

    ratingList = ["5 star", "4 star", "3 star", "2 star", "1 star"]
    global vr1
    vr1 = tk.StringVar(guestUserWin)
    vr1.set(ratingList[0])
    opt = tk.OptionMenu(guestUserWin, vr1, *ratingList)
    opt.config(width=90, font=('Helvetica', 12))
    opt.pack()

    rating_btn = tk.Button(guestUserWin, text="Add Rating", command=addRating)
    rating_btn.pack()
    center(guestUserWin)

    # mymenu1 = MyOptionMenu(guestUserWin, "Business Select", "Business (Regular)", "Family(1 Child)", "Family(2 Children)",
    #               "Family(3 Children)", "Tourist")
    # mymenu1.pack()
    # confirm_btn = tk.Button(guestUserWin, text="Confirm", command=displayRows)
    # confirm_btn.pack()
    # mymenu2 = MyOptionMenu(guestUserWin, "5 star", "4 star", "3 star", "2 star", "1 star")
    # mymenu2.pack()

    # addRating_btn = tk.Button(guestUserWin, text="Add Rating", command=addRating)
    # addRating_btn.pack()
    # center(guestUserWin)


def admin():
    global admin_win, w1, w2, e1, e2
    # win.destroy()
    admin_win = tk.Tk()
    admin_win.title("Admin Login")
    admin_win.geometry(winSize)
    admin_win.configure(bg='light blue')

    w = tk.Label(admin_win, text="LiftServer(Sign-in)")
    w.pack()

    e = tk.Label(admin_win, text="******************************")
    e.pack()

    w1 = tk.Label(admin_win, text="Username")
    w1.pack()

    e1 = tk.Entry(admin_win, justify='center')
    e1.pack()

    w2 = tk.Label(admin_win, text="Password")
    w2.pack()

    e2 = tk.Entry(admin_win, justify='center', show = "*")
    e2.pack()

    loginButton = tk.Button(admin_win, text='Login')
    # loginButton.configure(command=lambda button=b: validateLogin(e1, e2, admin_win))
    loginButton.configure(command=validateLogin)
    loginButton.pack()
    center(admin_win)


def validateLogin():
    global errorlbl
    global adminUser
    if e1.get() == "Noah" and e2.get() == "Password":
        adminUser = True
        displayRows()
    else:
        errorlbl = tk.Label(admin_win, text="Login error", bg='red')
        errorlbl.pack()
        errorlbl.after(5000, deleteErrorLbl)
    e2.delete(0, END)
    e2.insert(0, '')


def deleteErrorLbl():
    errorlbl.destroy()


# def center(win):
#     """
#     centers a tkinter window
#     :param win: the main window or Toplevel window to center
#     """
#     win.update_idletasks()
#     width = win.winfo_width()
#     frm_width = win.winfo_rootx() - win.winfo_x()
#     win_width = width + 2 * frm_width
#     height = win.winfo_height()
#     titlebar_height = win.winfo_rooty() - win.winfo_y()
#     win_height = height + titlebar_height + frm_width
#     x = win.winfo_screenwidth() // 2 - win_width // 2
#     y = win.winfo_screenheight() // 2 - win_height // 2
#     win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
#     win.deiconify()


def center(root):
    # Gets the requested values of the height and width.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    print("Width", windowWidth, "Height", windowHeight)

    # Gets both half the screen width/height and window width/height
    s = root.winfo_screenwidth()
    a = root.winfo_screenheight()
    positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))


win = tk.Tk()

win.geometry(winSize)
win.configure(bg='light blue')
introLbl = tk.Label(text="Are you an administrator or a guest user?")
adminButton = tk.Button(win, text="Admin", command=admin)
guestUserButton = tk.Button(win, text="Guest User", command=guestUser)
introLbl.pack()
adminButton.place(x=200, y=100)
guestUserButton.place(x=300, y=100)
center(win)
win.mainloop()



