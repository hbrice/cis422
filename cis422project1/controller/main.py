__author__ = 'josh'
from view import addressbooksgui
import Tkinter as tk
from model import addressbooks
def main():
    print "Main"

    root = tk.Tk()
    root.geometry("650x500+300+300")
    root.title("AddressBooks")
    app=addressbooksgui.AddressBooksFrame(root)
    root.mainloop()


if __name__ == '__main__':
    main()