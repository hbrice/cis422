__author__ = 'josh'
from view import addressbooksgui
import Tkinter as tk
from model import addressbooks
def main():
    print "Main"
    logic=addressbooks.addressbooks
    root = tk.Tk()
    root.geometry("650x500+300+300")
    app=addressbooksgui.AddressBooksFrame(root,logic)
    root.mainloop()


if __name__ == '__main__':
    main()