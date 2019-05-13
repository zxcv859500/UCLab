# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.font
import datetime
import threading
from server_tcp import get_request
import board
import os
from settings import Settings
import pickle
import subprocess
import shlex
import platform


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack(fill='both', expand=1)
        self.root = master

        # Header Frame
        header = Frame(self, relief="flat", bd=2)
        header.pack(side='top', fill='both', padx=5, pady=5)

        main_button = Button(header, overrelief='solid', height=1, width=5, text="메인")
        main_button.pack(side='left', anchor='w')
        setting_button = Button(header, overrelief='solid', height=1, width=5, text="설정", command=self.setting)
        setting_button.pack(side='left', anchor='e')
        font = tkinter.font.Font(family="맑은 고딕", size=20)
        title_frame = Frame(header, relief='flat', bd=2)
        title_frame.pack(side='top', anchor='center', fill=None)
        title_label = Label(title_frame, text="AQS Client", font=font)
        title_label.pack(side='bottom', anchor='center')
        s = datetime.datetime.now()
        s = str(s).split('.')[0]

        inform_frame = Frame(header, relief='flat', bd=2)
        inform_frame.pack(side='right', fill='both', anchor='center')
        self.datetime_label = Label(inform_frame, text=s)
        self.datetime_label.pack(side='top', anchor='n')
        ver_label = Label(inform_frame, text="Ver: 1.1")
        ver_label.pack(side='bottom', anchor='se')

        client_setting_frame = Frame(header, relief='flat', bd=2)
        client_setting_frame.pack(side='left', fill='both', padx=5, pady=5)

        # Reception Data Frame
        reception_data_frame = Frame(self, relief='solid', bd=2)
        reception_data_frame.pack(side='top', anchor='center', fill='both', padx=5, pady=5)
        reception_label = Label(reception_data_frame, text="서버 수신 데이터")
        reception_label.pack(side='top', anchor='w')

        first_line_frame = Frame(reception_data_frame, relief='flat', bd=2)
        first_line_frame.pack(side='top', anchor='center', fill='both', padx=5, pady=5)

        clientId_frame, desc_label, self.clientId_data_label = self.mk_dataframe(first_line_frame,
                                                                   '클라이언트ID',
                                                                   'data')
        clientId_frame.pack(side='left', anchor='sw', fill='both', padx=5, pady=5)
        desc_label.pack(side='top')
        self.clientId_data_label.pack(side='top')

        ver_frame, desc_label, self.ver_data_label = self.mk_dataframe(first_line_frame,
                                                              '버전(VER)',
                                                              'data')
        ver_frame.pack(side='left', anchor='sw', fill='both', padx=5, pady=5)
        desc_label.pack(side='top')
        self.ver_data_label.pack(side='top')

        dust_frame, desc_label, self.dust_data_label = self.mk_dataframe(first_line_frame,
                                                                    '미세먼지(PM10)',
                                                                    'data')
        dust_frame.pack(side='left', anchor='sw', fill='both', padx=5, pady=5)
        desc_label.pack(side='top')
        self.dust_data_label.pack(side='top')

        uldust_frame, desc_label, self.uldust_data_label = self.mk_dataframe(first_line_frame,
                                                                   '초미세먼지(PM2.5)',
                                                                   'data')
        uldust_frame.pack(side='left', anchor='sw', fill='both', padx=5, pady=5)
        desc_label.pack(side='top')
        self.uldust_data_label.pack(side='top')

        o3_frame, desc_label, self.o3_data_label = self.mk_dataframe(first_line_frame,
                                                                '오존(O3)',
                                                                'data')
        o3_frame.pack(side='left', anchor='sw', fill='both', padx=5, pady=5)
        desc_label.pack(side='top')
        self.o3_data_label.pack(side='top')

        no2_frame, desc_label, self.no2_data_label = self.mk_dataframe(first_line_frame,
                                                                  '이산화질소(NO2)',
                                                                  'data')
        no2_frame.pack(side='left', anchor='sw', fill='both', padx=5, pady=5)
        desc_label.pack(side='top')
        self.no2_data_label.pack(side='top')

        co_frame, desc_label, self.co_data_label = self.mk_dataframe(first_line_frame,
                                                               '일산화탄소(CO)',
                                                                'data')
        co_frame.pack(side='left', anchor='sw', fill='both', padx=5, pady=5)
        desc_label.pack(side='top')
        self.co_data_label.pack(side='top')

        so2_frame, desc_label, self.so2_data_label = self.mk_dataframe(first_line_frame,
                                                                  '아황산가스(SO2)',
                                                                  'data')
        so2_frame.pack(side='left', anchor='sw', fill='both', padx=5, pady=5)
        desc_label.pack(side='top')
        self.so2_data_label.pack(side='top')

        second_line_frame = Frame(reception_data_frame, relief='flat', bd=2)
        second_line_frame.pack(side='top', anchor='center', fill='both', padx=5, pady=5)

        mode_frame, desc_label, self.mode_data_label = self.mk_dataframe(second_line_frame,
                                                                    '모드\n(DMODE)',
                                                                    'data')
        mode_frame.pack(side='left', anchor='sw', fill='both', padx=5, pady=5)
        desc_label.pack(side='top')
        self.mode_data_label.pack(side='top')

        brit_frame, desc_label, self.brit_data_label = self.mk_dataframe(second_line_frame,
                                                                    '밝기\n(BRIT)',
                                                                    'data')
        brit_frame.pack(side='left', anchor='sw', fill='both', padx=5, pady=5)
        desc_label.pack(side='top')
        self.brit_data_label.pack(side='top')

        disp_frame, desc_label, self.disp_data_label = self.mk_dataframe(second_line_frame,
                                                                    'DISP\n',
                                                                    'data')
        disp_frame.pack(side='left', anchor='sw', fill='both', padx=5, pady=5)
        desc_label.pack(side='top')
        self.disp_data_label.pack(side='top')

        sky_frame, desc_label, self.sky_data_label = self.mk_dataframe(second_line_frame,
                                                                  '날씨코드\n(SKY)',
                                                                  'data')
        sky_frame.pack(side='left', anchor='sw', fill='both', padx=5, pady=5)
        desc_label.pack(side='top')
        self.sky_data_label.pack(side='top')

        pty_frame, desc_label, self.pty_data_label = self.mk_dataframe(second_line_frame,
                                                                  '강수형태\n(PTY)',
                                                                  'data')
        pty_frame.pack(side='left', anchor='sw', fill='both', padx=5, pady=5)
        desc_label.pack(side='top')
        self.pty_data_label.pack(side='top')

        t1h_frame, desc_label, self.t1h_data_label = self.mk_dataframe(second_line_frame,
                                                                  '온도\n(T1H)',
                                                                  'data')
        t1h_frame.pack(side='left', anchor='sw', fill='both', padx=5, pady=5)
        desc_label.pack(side='top')
        self.t1h_data_label.pack(side='top')

        reh_frame, desc_label, self.reh_data_label = self.mk_dataframe(second_line_frame,
                                                                 '습도\n(REH)',
                                                                 'data')
        reh_frame.pack(side='left', anchor='sw', fill='both', padx=5, pady=5)
        desc_label.pack(side='top')
        self.reh_data_label.pack(side='top')

        rn1_frame, desc_label, self.rn1_data_label = self.mk_dataframe(second_line_frame,
                                                                  '한시간 강수량(RN1)\n',
                                                                  'data')
        rn1_frame.pack(side='left', anchor='sw', fill='both', padx=5, pady=5)
        desc_label.pack(side='top')
        self.rn1_data_label.pack(side='top')

        vec_frame, desc_label, self.vec_data_label = self.mk_dataframe(second_line_frame,
                                                                  '풍향(VEC)\n',
                                                                  'data')
        vec_frame.pack(side='left', anchor='sw', fill='both', padx=5, pady=5)
        desc_label.pack(side='top')
        self.vec_data_label.pack(side='top')

        wsd_frame, desc_label, self.wsd_data_label = self.mk_dataframe(second_line_frame,
                                                                  '풍속(WSD)\n',
                                                                  'data')
        wsd_frame.pack(side='left', anchor='sw', fill='both', padx=5, pady=5)
        desc_label.pack(side='top')
        self.wsd_data_label.pack(side='top')

        # Sever Log Frame
        server_log_frame = Frame(self, relief='solid', bd=2)
        server_log_frame.pack(side='top', fill='both', padx=5, pady=5)

        label = Label(server_log_frame, text='서버 송수신 로그')
        label.pack(side='top', anchor='w')

        server_recv_frame = Frame(server_log_frame, relief='flat', bd=2)
        server_recv_frame.pack(side='top', anchor='w')

        self.server_recv_time_label = Label(server_recv_frame, text='')
        self.server_recv_time_label.pack(side='left', anchor='w', padx=5, pady=5)

        self.server_recv_label = Label(server_recv_frame, text='data')
        self.server_recv_label.config(fg='blue')
        self.server_recv_label.pack(side='left', anchor='w', padx=5, pady=5)

        server_req_frame = Frame(server_log_frame, relief='flat', bd=2)
        server_req_frame.pack(side='top', anchor='w')

        self.server_req_time_label = Label(server_req_frame, text='')
        self.server_req_time_label.pack(side='left', anchor='w', padx=5, pady=5)

        self.server_req_label = Label(server_req_frame, text='data')
        self.server_req_label.config(fg='red')
        self.server_req_label.pack(side='left', anchor='w', padx=5, pady=5)

        # Board Log Frame
        board_log_frame = Frame(self, relief='solid', bd=2)
        board_log_frame.pack(side='top', fill='both', padx=5, pady=5)

        label = Label(board_log_frame, text='외부 보드 송신 로그')
        label.pack(side='top', anchor='w')

        board_req_frame = Frame(board_log_frame, relief='flat', bd=2)
        board_req_frame.pack(side='top', fill='both', padx=5, pady=5)

        self.board_req_time_label = Label(board_req_frame, text='')
        self.board_req_time_label.pack(side='left', anchor='center')

        self.board_req_label = Label(board_req_frame, text='data')
        self.board_req_label.config(fg='red')
        self.board_req_label.pack(side='left', anchor='w', padx=5, pady=5)

        # Error Frame
        error_frame = Frame(self, relief='flat', bd=2)
        error_frame.pack(side='top', fill='both', anchor='center')

        # Server State Frame
        server_state_frame = Frame(error_frame, relief='solid', bd=2)
        server_state_frame.pack(side='left', anchor='center', fill='both', padx=5)

        desc_label = Label(server_state_frame, text='서버 통신')
        desc_label.pack(side='top', anchor='center', padx=5, pady=5)

        self.server_state_label = Label(server_state_frame, text='정상')
        self.server_state_label.pack(side='top', anchor='center', pady=5)

        # Board State Frame
        board_state_frame = Frame(error_frame, relief='solid', bd=2)
        board_state_frame.pack(side='left', anchor='center', fill='both', padx=5)

        desc_label = Label(board_state_frame, text='외부보드 통신')
        desc_label.pack(side='top', anchor='center', padx=5, pady=5)

        self.board_state_label = Label(board_state_frame, text='정상')
        self.board_state_label.pack(side='top', anchor='center', pady=5)

        # Error State
        error_state_frame = Frame(error_frame, relief='solid', bd=2)
        error_state_frame.pack(side='left', anchor='center', fill='both', padx=5, expand=True)

        self.error_label = Label(error_state_frame, text='No Error')
        self.error_label.pack(side='top', anchor='center', pady=20)

        # Init Value
        self.client_id = ''
        self.frequency = 0
        self.cert = False
        self.count = 0
        self.board_count = 0
        self.protector = True
        self.board_protector = True
        self.new_window_token = False
        self.data = {
            'client_id': None,
            'ip': None,
            'port': None,
            'server_frequency': 0,
            'server_method': None,
            'port_name': None,
            'port_rate': None,
            'port_frequency': 0,
            'cert': False,
            'running': False,
        }
        self.ser = None
        self.cur_recv = None
        self.server_error_cnt = 0
        self.board_error_cnt = 0
        self.server_error = False
        self.board_error = False

        # Load Value
        self.load()

        # Start timer
        self.start_timer()

        # Update Information
        self.update()

        # Main Button
        main_button.config(state=DISABLED)
        setting_button.config(state=NORMAL)

        # Exit Event
        master.protocol("WM_DELETE_WINDOW", self.save)

    def board_close(self):
        self.ser.close()

    def setting(self):
        self.pack_forget()
        sett = Settings(self.root, self.main_pack, self.data, self.board_close, self.save_files)
        sett.mainloop()

    def main_pack(self):
        self.pack()

    @staticmethod
    def mk_dataframe(data_frame, label_text, data_text):
        frame = Frame(data_frame, relief='solid', bd=2, padx=20, pady=5)
        desc_label = Label(frame, text=label_text)
        data_label = Label(frame, text=data_text)

        return frame, desc_label, data_label

    @staticmethod
    def new_line(string, count=80):
        new_string = ''
        cnt = 0
        for char in string:
            cnt += 1
            if cnt >= count:
                new_string += '\n'
                cnt = 0
            new_string += char
        for i in range(count - cnt):
            new_string += ' '
        return new_string

    def error_update(self):
        if self.board_error is True and self.server_error is True:
            self.error_label['text'] = '서버 통신 에러, 인터넷 연결을 확인해주세요.\n' + \
                                       '보드 통신 에러, 보드 연결을 확인해주세요.'
        elif self.server_error is True:
            self.error_label['text'] = '서버 통신 에러, 인터넷 연결을 확인해주세요.'
        elif self.board_error is True:
            self.error_label['text'] = '보드 통신 에러, 보드 연결을 확인해주세요.'
        else:
            self.error_label['text'] = 'No Error'

    def start_timer(self):
        timer = threading.Timer(1, self.start_timer)
        timer.start()

        s = datetime.datetime.now()
        s = str(s).split('.')[0]
        self.error_update()
        try:
            self.datetime_label['text'] = s
        except RuntimeError:
            timer.cancel()

        if self.data['cert'] is True and self.data['running'] is True:
            self.count += 1
            self.board_count += 1

            if self.count >= self.data['server_frequency'] and self.protector is True:
                self.protector = False
                self.update(self.data['client_id'])
                self.count = 0
                self.protector = True
            if self.board_count >= self.data['port_frequency'] and self.board_protector is True:
                self.board_protector = False
                if self.ser is None:
                    self.ser = board.connect(self.data['port_name'], self.data['port_rate'])
                now = datetime.datetime.now()
                now = str(now).split('.')[0]
                req_data = board.send_data(self.ser, self.cur_recv, now)
                if req_data.__contains__('Port'):
                    self.board_req_time_label['text'] = now
                    self.board_error = True
                    self.board_state_label['text'] = '이상'
                    self.ser = None
                else:
                    self.board_req_time_label['text'] = now
                    self.board_state_label['text'] = '정상'
                    self.board_error = False
                self.board_req_label['text'] = '[S]' + self.new_line(req_data, 130)
                self.board_count = 0
                self.board_protector = True

    def update(self, client_id=None):
        if client_id is None:
            return None
        if self.data['ip'] == '' or self.data['port'] == '':
            self.server_state_label['text'] = '이상'
            return None
        req, recv = get_request(client_id, self.data['ip'], int(self.data['port']))
        self.cur_recv = recv
        if len(recv) == 0:
            self.server_state_label['text'] = '이상'
            self.server_error_cnt += 1
            if self.server_error_cnt >= 4 and not self.error_label['text'].__contains__('서버'):
                self.server_error = True
            return None
        self.server_error = False
        self.server_error_cnt = 0
        self.server_state_label['text'] = '정상'
        now = datetime.datetime.now()
        now = str(now).split('.')[0]

        self.server_req_time_label['text'] = now
        self.server_req_label['text'] = '[S]' + self.new_line(req, 130)
        self.server_recv_time_label['text'] = now
        self.server_recv_label['text'] = '[R]' + self.new_line(recv, 130)

        recv = recv.split(',')
        self.clientId_data_label['text'] = recv[1]
        self.ver_data_label['text'] = self.util_data(recv[3])
        self.dust_data_label['text'] = self.util_data(recv[5])
        self.uldust_data_label['text'] = self.util_data(recv[6])
        self.o3_data_label['text'] = self.util_data(recv[7])
        self.no2_data_label['text'] = self.util_data(recv[8])
        self.co_data_label['text'] = self.util_data(recv[9])
        self.so2_data_label['text'] = self.util_data(recv[10])
        self.mode_data_label['text'] = self.util_data(recv[11])
        self.brit_data_label['text'] = self.util_data(recv[12])
        self.disp_data_label['text'] = self.util_data(recv[13])
        self.sky_data_label['text'] = self.util_data(recv[14])
        self.pty_data_label['text'] = self.util_data(recv[15])
        self.t1h_data_label['text'] = self.util_data(recv[16])
        self.reh_data_label['text'] = self.util_data(recv[17])
        self.rn1_data_label['text'] = self.util_data(recv[18])
        self.vec_data_label['text'] = self.util_data(recv[19])
        self.wsd_data_label['text'] = self.util_data(recv[20])

    def load(self):
        if os.path.isfile('data'):
            file = open('data', 'rb')
            self.data = pickle.load(file)
            
    def save_files(self):
        file = open('data', 'wb')
        pickle.dump(self.data, file)
        file.close()

    def save(self):
        file = open('data', 'wb')
        pickle.dump(self.data, file)
        file.close()
        self.destroy()
        self.root.destroy()
        os._exit(1)

    @staticmethod
    def util_data(recv):
        if recv.__contains__('!'):
            recv = recv.split('!')[0]
        if recv.__contains__('/'):
            recv = recv.split('/')

            degree = int(recv[1])

            if degree == 1:
                degree = '좋음'
            elif degree == 2:
                degree = '보통'
            elif degree == 3:
                degree = '나쁨'
            else:
                degree = '매우나쁨'
            return recv[0].split(':')[1] + ' ' + degree

        return recv.split(':')[1]


def refresh_time():
    if platform.system() != "Linux":
        print("Not Linux system")
        return False
    try:
        subprocess.call(shlex.split("sudo rdate -s time.bora.net"))
        return True
    except FileNotFoundError:
        print("rdate not installed")
        subprocess.call(shlex.split("sudo apt-get install time.bora.net"))
        return False


def update():
    if platform.system() != "Linux":
        print("Not Linux system")
        return False
    subprocess.call(shlex.split("git -C /home/pi/UCLab pull"))
    return True


if __name__ == "__main__":
    print('current')
    update()
    refresh_time()
    print('new')
    window = Tk()
    window.title("AQS Client")
    window.geometry("1150x600+100+100")
    window.resizable(False, False)
    app = Application(window)
    app.mainloop()
    refresh_time()
