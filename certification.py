from tkinter import *


def empty():
    pass


callback = empty()
window_callback = empty()


class CertApplication(Frame):

    def __init__(self, master=None, cert=False):
        Frame.__init__(self, master)
        self.pack(fill='both', expand=1)
        self.root = master

        # Frame
        entry_frame = Frame(self, relief='flat', bd=2)
        entry_frame.pack(side='top', anchor='center', fill='both', pady=5)

        button_frame = Frame(self, relief='flat', bd=2)
        button_frame.pack(side='top', anchor='center', fill='both', pady=10)

        label_frame = Frame(self, relief='flat', bd=2)
        label_frame.pack(side='top', anchor='center', fill='both', pady=5)

        # Entry
        self.first_entry_text = StringVar()
        first_entry = Entry(entry_frame, width=10, textvariable=self.first_entry_text)
        first_entry.pack(side='left', anchor='center', fill='both')
        label = Label(entry_frame, text='-')
        label.pack(side='left', anchor='center', fill='both')
        self.second_entry_text = StringVar()
        second_entry = Entry(entry_frame, width=10, textvariable=self.second_entry_text)
        second_entry.pack(side='left', anchor='center', fill='both')

        # Button
        cert_button = Button(button_frame, width=5, text='입력', command=self.certification)
        cert_button.pack(side='top', anchor='center')

        # Label
        desc_label = Label(label_frame, text='인증번호를 입력하세요')
        desc_label.pack(side='top', anchor='center', pady=5)

        self.cert_label = Label(label_frame, text='')
        self.cert_label.pack(side='top', anchor='center', pady=5)

        master.protocol("WM_DELETE_WINDOW", self.closing_event)

        if cert is True:
            self.first_entry_text.set('*****')
            self.second_entry_text.set('****')
            self.cert_label['text'] = '정품인증을 받았습니다.'

    def certification(self):
        res = self.first_entry_text.get() + self.second_entry_text.get()
        if res == "uclab7202":
            self.cert_label['text'] = '정품인증을 받았습니다.'
            callback()
        else:
            self.cert_label['text'] = '정품인증에 실패하였습니다.'

    def closing_event(self):
        window_callback()
        self.destroy()
        self.root.destroy()


def new_window(root, cert_callback, new_window_callback, cert=False):
    new_window_callback()
    global window_callback
    window_callback = new_window_callback
    newwin = Toplevel(root)
    app = CertApplication(newwin, cert)
    app.pack()

    global callback
    callback = cert_callback


if __name__ == "__main__":
    window = Tk()
    window.geometry("160x160+100+100")
    window.resizable(False, False)
    app = CertApplication(window)
    app.mainloop()
