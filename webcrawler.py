"""sync using queue"""
import multiprocessing
import requests


def web_cralwer(q):
    """child process"""
    try:
        p_name = multiprocessing.current_process().name
        url = q.get()  # block
        response = requests.get(url)
        print(f'{p_name}: {url}: {response.content[:128]}')
    except requests.exceptions.ConnectionError as err:
        subject = f'{p_name}: error in requesting : {url}'
        print(subject)
        print(err)

def main():
    urls = ['http://python.org', 'http://linux.org', 'http://kernel.org',
            'http://golang.org', 'http://perllang.org']
    queue = multiprocessing.Queue()  # IPC, sync technique, empty

    for url in urls:
        p = multiprocessing.Process(target=web_cralwer, args=(queue,))
        p.start()

    for url in urls:
        queue.put(url)  # add urls into the queue

    for child in multiprocessing.active_children():
        child.join()


if __name__ == '__main__':
    main()

