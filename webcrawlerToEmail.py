"""sync using queue"""
import multiprocessing
from smtplib import SMTP
from email.mime.text import MIMEText
import requests

SMTP_SERVER_ADDR = 'mailhub.lss.emc.com'


def send_alert_mail(from_address, to_address, subject, message):
    # smtp client
    mesg = MIMEText(message)
    mesg['From'] = from_address
    mesg['To'] = to_address
    mesg['Subject'] = subject

    with SMTP(SMTP_SERVER_ADDR) as smtp:
        smtp = SMTP(SMTP_SERVER_ADDR)
        smtp.debuglevel = 1
        smtp.sendmail(from_address, to_address, mesg.as_string())


def web_crawler(q):
    """child process"""
    try:
        p_name = multiprocessing.current_process().name
        url = q.get()  # block
        response = requests.get(url)
        print(f'{p_name}: {url}: {response.content[:128]}')
    except requests.exceptions.ConnectionError as err:
        subject = f'{p_name}: error in requesting : {url}'
        send_alert_mail('amit.raj@dell.com', 'amit.raj@dell.com', subject, str(err))


def main():
    """parent process"""
    urls = ['http://python.org', 'http://linux.org', 'http://kernel.org',
            'http://golang.org', 'http://perllang.org']
    queue = multiprocessing.Queue()  # IPC, sync technique, empty

    for url in urls:
        p = multiprocessing.Process(target=web_crawler, args=(queue,))
        p.start()

    for url in urls:
        queue.put(url)  # add urls into the queue

    for child in multiprocessing.active_children():
        child.join()


if __name__ == '__main__':
    main()
