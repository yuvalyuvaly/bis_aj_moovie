#!/usr/bin/python

def from_gen():
    with open('KungFuPanda.txt', 'rb') as f:
        txt = f.read().decode('utf-8')
    txt = txt.replace('\r\n', '\n')
    parts = txt.split('\n\n')
    res = '\n\n'.join(str(i + 1) + '\n' + x for i, x in enumerate(parts)) + '\n\n'

    with open('KungFuPanda.srt', 'wb') as f:
        f.write(res.encode('utf8'))

if __name__ == '__main__':
    from_gen()
