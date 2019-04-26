from tkinter import *
import tkinter.font
import datetime
import threading
from certification import new_window
from route import assign_static_ip


class Settings(Frame):

    def __init__(self, master=None, main=None, data=None, board_close_callback=None, save_callback=None):
        Frame.__init__(self, master)
        self.pack(fill='both', expand=1)
        self.root = master
        self.main = main

        # Header Fame
        header = Frame(self, relief='flat', bd=2)
        header.pack(side='top', fill='both', padx=5, pady=5)

        main_button = Button(header, overrelief='solid', height=1, width=5, text='메인', command=self.main_callback)
        main_button.pack(side='left', anchor='w')
        setting_button = Button(header, overrelief='solid', height=1, width=5, text='설정')
        setting_button.pack(side='left', anchor='e')
        font = tkinter.font.Font(family='맑은 고딕', size=20)
        title_frame = Frame(header, relief='flat', bd=2)
        title_frame.pack(side='top', anchor='center', fill=None)
        title_label = Label(title_frame, text='AQS Client', font=font)
        title_label.pack(side='bottom', anchor='center')
        s = datetime.datetime.now()
        s = str(s).split('.')[0]

        inform_frame = Frame(header, relief='flat', bd=2)
        inform_frame.pack(side='right', fill='both', anchor='center')
        self.datetime_label = Label(inform_frame, text=s)
        self.datetime_label.pack(side='top', anchor='n')
        ver_label = Label(inform_frame, text='Ver: 1.1')
        ver_label.pack(side='bottom', anchor='se')

        # Setting Frame
        setting_frame = Frame(self, relief='solid', bd=2)
        setting_frame.pack(side='top', anchor='center', fill='both')

        # Server Setting Frame
        server_frame = Frame(setting_frame, relief='flat', bd=2)
        server_frame.pack(side='left', anchor='center', padx=5, pady=5)
        desc_label = Label(server_frame, text='서버 설정')
        desc_label.pack(side='top', anchor='center', padx=5, pady=5)

        # IP Frame
        ip_frame = Frame(server_frame, relief='flat', bd=2)
        ip_frame.pack(side='top', anchor='s')

        desc_label = Label(ip_frame, text='IP : ')
        desc_label.pack(side='left', anchor='w')

        self.ip_var = StringVar()

        ip_entry = Entry(ip_frame, width=12, textvariable=self.ip_var)
        ip_entry.pack(side='left', anchor='w', padx=5)

        desc_label = Label(ip_frame, text='PORT : ')
        desc_label.pack(side='left', anchor='w')

        self.server_port_var = StringVar()

        port_entry = Entry(ip_frame, width=5, textvariable=self.server_port_var)
        port_entry.pack(side='left', anchor='w')

        # Client ID Frame
        id_entry_frame = Frame(server_frame, relief='flat', bd=2)
        id_entry_frame.pack(side='top', anchor='s')

        desc_label = Label(id_entry_frame, text='클라이언트ID : ')
        desc_label.pack(side='left', anchor='w')

        self.first_var = StringVar()
        self.second_var = StringVar()
        self.third_var = StringVar()

        first_entry = Entry(id_entry_frame, width=3, textvariable=self.first_var)
        first_entry.pack(side='left', anchor='w')
        desc_label = Label(id_entry_frame, text='-')
        desc_label.pack(side='left', anchor='w')
        second_entry = Entry(id_entry_frame, width=4, textvariable=self.second_var)
        second_entry.pack(side='left', anchor='w')
        desc_label = Label(id_entry_frame, text='-')
        desc_label.pack(side='left', anchor='w')
        third_entry = Entry(id_entry_frame, width=4, textvariable=self.third_var)
        third_entry.pack(side='left', anchor='w')

        # Server Frequency Frame
        server_frequency_frame = Frame(server_frame, relief='flat', bd=2)
        server_frequency_frame.pack(side='top', anchor='s')

        desc_label = Label(server_frequency_frame, text='통신주기 : ')
        desc_label.pack(side='left', anchor='w')

        self.server_frequency = StringVar()

        frequency_entry = Entry(server_frequency_frame, width=19, textvariable=self.server_frequency)
        frequency_entry.pack(side='left', anchor='w')

        # Communication Method Frame
        method_frame = Frame(server_frame, relief='flat', bd=2)
        method_frame.pack(side='top', anchor='s', fill='both')

        desc_label = Label(method_frame, text='통신방식 : ')
        desc_label.pack(side='left', anchor='w')

        self.method_var = StringVar()
        method_choice = ['유선랜', '무선CDMA(SKT)']
        self.method_var.set('유선랜')

        method_dropbox = OptionMenu(method_frame, self.method_var, *method_choice)
        method_dropbox.pack(side='left', anchor='w')

        # Outer Board Frame
        board_frame = Frame(setting_frame, relief='flat', bd=2)
        board_frame.pack(side='left', anchor='n', padx=200, pady=10)
        desc_label = Label(board_frame, text='외부보드 설정')
        desc_label.pack(side='top', anchor='n')

        # Port Setting Frame
        port_frame = Frame(board_frame, relief='flat', bd=2)
        port_frame.pack(side='top', anchor='s', fill='both')

        desc_label = Label(port_frame, text='COM포트 : ')
        desc_label.pack(side='left', anchor='w')

        self.port_var = StringVar()
        port_choice = []
        for i in range(0, 20):
            port_choice.append('/dev/ttyUSB' + str(i))
        self.port_var.set('/dev/ttyUSB0')

        port_dropbox = OptionMenu(port_frame, self.port_var, *port_choice)
        port_dropbox.pack(side='left', anchor='w')

        # Board Rate Frame
        rate_frame = Frame(board_frame, relief='flat', bd=2)
        rate_frame.pack(side='top', anchor='s', fill='both')

        desc_label = Label(rate_frame, text='포트 속도 : ')
        desc_label.pack(side='left', anchor='w')

        self.rate_var = StringVar()
        rate_choice = ['110', '300', '1200', '2400', '4800', '9600', '19200', '38400', '57600', '115200', '230400',
                       '460800', '921600']
        self.rate_var.set('9600')

        rate_dropbox = OptionMenu(rate_frame, self.rate_var, *rate_choice)
        rate_dropbox.pack(side='left', anchor='w')

        # Board Frequency Frame
        board_frequency_frame = Frame(board_frame, relief='flat', bd=2)
        board_frequency_frame.pack(side='top', anchor='s', fill='both')

        desc_label = Label(board_frequency_frame, text='통신 주기 : ')
        desc_label.pack(side='left', anchor='w')

        self.board_frequency_var = StringVar()

        board_frequency_entry = Entry(board_frequency_frame, textvariable=self.board_frequency_var)
        board_frequency_entry.pack(side='left', anchor='w')

        # Client Frame
        client_frame = Frame(setting_frame, relief='flat', bd=2)
        client_frame.pack(side='left', anchor='n', padx=50, pady=10)
        desc_label = Label(client_frame, text='클라이언트 설정')
        desc_label.pack(side='top', anchor='n')

        # IP Address Assign
        ip_address_frame = Frame(client_frame, relief='flat', bd=2)
        ip_address_frame.pack(side='top', anchor='s', fill='both')

        desc_label = Label(ip_address_frame, text='IP 주소 : ')
        desc_label.pack(side='left', anchor='w')

        self.ip_address_var = StringVar()

        ip_address_entry = Entry(ip_address_frame, textvariable=self.ip_address_var)
        ip_address_entry.pack(side='left', anchor='w')

        # SubnetMask Assign
        subnetmask_frame = Frame(client_frame, relief='flat', bd=2)
        subnetmask_frame.pack(side='top', anchor='s', fill='both', padx=2)

        desc_label = Label(subnetmask_frame, text="서브넷 : ")
        desc_label.pack(side='left', anchor='w')

        self.subnetmask_var = StringVar()

        subnetmask_entry = Entry(subnetmask_frame, textvariable=self.subnetmask_var)
        subnetmask_entry.pack(side='left', anchor='w')

        # Gateway Assign
        gateway_frame = Frame(client_frame, relief='flat', bd=2)
        gateway_frame.pack(side='top', anchor='s', fill='both')

        desc_label = Label(gateway_frame, text="게이트 : ")
        desc_label.pack(side='left', anchor='w', padx=1)

        self.gateway_var = StringVar()

        gateway_entry = Entry(gateway_frame, textvariable=self.gateway_var)
        gateway_entry.pack(side='top', anchor='s', fill='both')

        # IP Address Assgin Button
        ip_address_button_frame = Frame(client_frame, relief='flat', bd=2)
        ip_address_button_frame.pack(side='top', anchor='s', fill='both')

        ip_address_button = Button(ip_address_button_frame, text='변경', command=self.ip_address_assign)
        ip_address_button.pack(side='left', anchor='w', padx=60)

        # Start Timer
        self.start_timer()

        # Setting Button
        setting_button.config(state=DISABLED)

        # Button Frame
        button_frame = Frame(self, relief='flat', bd=2)
        button_frame.pack(side='bottom', anchor='center', pady=10)

        # Change Button
        change_button = Button(button_frame, text='변경/시작', command=self.change)
        change_button.pack(side='left', anchor='center', padx=5)

        # Certification Button
        cert_button = Button(button_frame, text='인증', command=self.cert_command)
        cert_button.pack(side='left', anchor='center', padx=5)

        # Stop Button
        stop_button = Button(button_frame, text='중지', command=self.stop)
        stop_button.pack(side='left', anchor='center', padx=5)

        # Init Value
        self.new_window_token = False
        self.cert = False
        self.data = data
        self.board_close_callback = board_close_callback
        self.save_callback = save_callback

        if data['client_id'] is not None:
            self.first_var.set(data['client_id'][:3])
            self.second_var.set(data['client_id'][3:7])
            self.third_var.set(data['client_id'][7:])

        if data['server_frequency'] != 0:
            self.server_frequency.set(data['server_frequency'])
        if data['server_method'] is not None:
            self.method_var.set(data['server_method'])
        if data['port_name'] is not None:
            self.port_var.set(data['port_name'])
        if data['port_rate'] is not None:
            self.rate_var.set(data['port_rate'])
        if data['port_frequency'] != 0:
            self.board_frequency_var.set(data['port_frequency'])
        if data['ip'] is not None:
            self.ip_var.set(data['ip'])
        if data['port'] is not None:
            self.server_port_var.set(data['port'])

        if data['ip'] is None:
            self.ip_var.set('121.179.45.130')
        if data['port'] is None:
            self.server_port_var.set('15300')

    def stop(self):
        self.data['running'] = False
        self.board_close_callback()

    def ip_address_assign(self):
        assign_static_ip(self.ip_address_var.get(), self.subnetmask_var.get(), self.gateway_var.get())

    def change(self):
        client_id = self.first_var.get() + self.second_var.get() + self.third_var.get()
        server_frequency = int(self.server_frequency.get())
        server_method = self.method_var.get()
        port_name = self.port_var.get()
        port_rate = self.rate_var.get()
        port_frequency = int(self.board_frequency_var.get())
        ip = self.ip_var.get()
        port = self.server_port_var.get()

        if client_id != '':
            self.data['client_id'] = client_id
        if ip != '':
            self.data['ip'] = ip
        if port != '':
            self.data['port'] = port
        if server_frequency is not None:
            self.data['server_frequency'] = server_frequency
        if server_method != '':
            self.data['server_method'] = server_method
        if port_name != '':
            self.data['port_name'] = port_name
        if port_rate != '':
            self.data['port_rate'] = port_rate
        if port_frequency is not None:
            self.data['port_frequency'] = port_frequency
        self.data['running'] = True

        self.save_callback()

    def cert_command(self):
        if self.new_window_token is True:
            return
        new_window(self, self.cert_callback, self.window_update, self.cert)

    def cert_callback(self):
        self.cert = True
        self.data['cert'] = True

    def window_update(self):
        self.new_window_token = not self.new_window_token

    def start_timer(self):
        timer = threading.Timer(1, self.start_timer)
        timer.start()

        s = datetime.datetime.now()
        s = str(s).split('.')[0]
        try:
            self.datetime_label['text'] = s
        except RuntimeError:
            timer.cancel()

    def main_callback(self):
        self.pack_forget()
        self.main()


if __name__ == "__main__":
    window = Tk()
    window.geometry("1150x500+100+100")
    window.resizable(False, False)
    app = Settings(window)
    app.mainloop()
