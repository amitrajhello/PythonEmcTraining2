import threading
import pyexcel
from sshClient import CustomSSHClient

target_file = 'sshresponse.log'


class ThreadedSSHClient(CustomSSHClient):
    def __init__(self, host, port, user, pwd, job):
        super().__init__(host, port, user, pwd)
        self.job = job
        self.t_name = threading.current_thread().name
        self.task_runner()

    def task_runner(self):
        payload = self.check_output(self.job)
        caption = f'{self.t_name} ran {self.job} @ {self.host}'

        with open(target_file, 'a') as fw:
            fw.write(caption.center(80, '-') + '\n')
            fw.write(payload + '\n')


def main():
    sheet = pyexcel.get_sheet(file_name=r'C:\Users\raja6\Desktop\study\emc python training\hosts.xlsx')

    for ssh_host_info in sheet:
        t = threading.Thread(target=ThreadedSSHClient, args=ssh_host_info)
        t.start()


if __name__ == '__main__':
    main()
