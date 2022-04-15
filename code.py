import final
import time
from telethon.sync import TelegramClient
import sys
from PyQt5 import QtWidgets
groups_path=""
interval=30
repeats=1
logoutput_path=""
Groups=[]
Message=""
phone=""
api_id=""
hash_id=""
class ExampleApp(QtWidgets.QMainWindow, final.Ui_Dialog):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле final.py
        super().__init__()
        self.setupUi(self)
        self.start.clicked.connect(self.start_func)
        self.filechoose3.clicked.connect(self.logs_path_func)
        self.filechoose2.clicked.connect(self.groups_path_func)
        self.load.clicked.connect(self.load_func)
    def groups_path_func(self):
        global groups_path
        groups_path = QtWidgets.QFileDialog.getOpenFileName(self,'Кому капец?',None,'Че зыришь?(*.txt;*.json)')[0]
        self.directory2.setText(groups_path)
        print(groups_path)
    def logs_path_func(self):
        global logoutput_path
        logoutput_path = QtWidgets.QFileDialog.getExistingDirectory()
        self.directory4.setText(logoutput_path)
        logoutput_path = f'{logoutput_path}/logs-' + time.asctime().replace(' ', '-').replace(':','-').lower() + '.txt'
        print(logoutput_path)
    def load_func(self):
        global interval,repeats,Groups,Message,phone
        logs=open(logoutput_path,'w')
        try:
            datasetup=open(str(sys.argv[0])[:-7]+'config.txt','r')
            global phone,api_id,hash_id
            rawdata=datasetup.read().split()
            print(rawdata)
            api_id=int(rawdata[0])
            hash_id=rawdata[1]
            phone=rawdata[2]
            datasetup.close()
        except FileNotFoundError:
            status='[ERROR] No file config.txt found in directory'+str(sys.argv[0])[:-7]+'config.txt '+time.asctime().replace(' ', '-').replace(':', '-').lower()
            logs.write(status + '\n')
            status=time.asctime().replace(' ', '-').replace(':', '-').lower() + f'-run-setup.py-first'
            logs.write(status + '\n')
            sys.exit()
        status=time.asctime().replace(' ', '-').replace(':','-').lower()+'-opening-groups-file'
        logs.write(status+'\n')
        f=open(groups_path,'r')
        Groups=f.read().split()
        f.close()
        status=time.asctime().replace(' ', '-').replace(':','-').lower()+'-saving-message-to-a-variable'
        logs.write(status+'\n')
        Message=self.Message.toPlainText()
        status = time.asctime().replace(' ', '-').replace(':', '-').lower() + '-saving-interval-to-a-variable'
        logs.write(status + '\n')
        interval=int(self.Interval.toPlainText())
        status = time.asctime().replace(' ', '-').replace(':', '-').lower() + '-saving-amount-of-repeats-to-a-variable'
        logs.write(status + '\n')
        repeats=int(self.repeats.toPlainText())
        status= time.asctime().replace(' ', '-').replace(':', '-').lower() + '-load-complete'
        self.status.setText(status)
        logs.write(status + '\n')
        logs.close()
    def start_func(self):
        logs=open(logoutput_path,'a')
        with TelegramClient(phone,api_id,hash_id) as client:
            for i in range(repeats):
                for a in Groups:
                    status = time.asctime().replace(' ', '-').replace(':','-').lower() + f'-trying-to-send-message-to-a-group-{a}'
                    print(status)
                    logs.write(status + '\n')
                    try:
                        client.send_message(a,Message)
                        status = time.asctime().replace(' ', '-').replace(':', '-').lower() + '-success'
                        logs.write(status + '\n')
                        print(status)
                        time.sleep(interval)
                    except Exception as e:
                        status = "[!] Error:"+str(e)
                        logs.write(status + '\n')
                        print(status)
                        status = f"[!] Stopped while trying to message {a}"
                        print(status)
                        logs.write(status + '\n')
                        continue
        status= time.asctime().replace(' ', '-').replace(':', '-').lower() + f'-im-done'
        logs.write(status+'\n')
        self.status.setText(status)
        logs.close()
        

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':
    main()