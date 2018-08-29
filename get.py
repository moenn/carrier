import re
import subprocess

# SELECT = "you-get"
SELECT = "youtube-dl"

CONFIG_FILE = './you-get.config'
SAVE_PATH = '/home/meng/Downloads/you-get'

def read_urls():
    with open(CONFIG_FILE, 'r') as f:
        _ = f.readlines()
        data = ''.join([n for n in _ if not n.startswith('#')])
    pattern = re.compile(r"https://www.youtube.com/watch\?v=[a-zA-Z0-9_-]{11}")
    urls = re.findall(pattern, data)
    return urls    


def print_info(urls):
    print('total : {}'.format(len(urls)))
    for n in urls:
        print(n)
        

def run(urls):
    for n in urls:
        if SELECT == "you-get":
            print(subprocess.run(['proxychains', 'you-get', '-o', SAVE_PATH, n]))
        elif SELECT == "youtube-dl":
            print(subprocess.run(['youtube-dl', n]))
        else:
            pass

def mark_urls():
    with open(CONFIG_FILE, 'r+') as f:
        data = f.readlines()
        i = 0
        while i < len(data):
            if not data[i].startswith('#') and data[i] != '\n':
                data[i] = "#{}".format(data[i])
            i += 1

        f.seek(0)
        f.truncate()
        f.write(''.join(data))
    

def main():
    urls = read_urls()
    print_info(urls)
    if urls:
        run(urls)
        mark_urls()


if __name__ == '__main__':
    main()
