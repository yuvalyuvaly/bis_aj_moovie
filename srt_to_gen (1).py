#!/usr/bin/python

def to_gen():
    txt = open('KungFuPanda.srt', 'rb').read().decode('utf-8')
    txt = txt.replace('\r\n', '\n')
    if txt[0] == '\ufeff' or txt[0] == u'\ufeff':
        txt = txt[1:]

    parts = [x.split('\n') for x in txt.split('\n\n')[:-1]]
    assert all(x[0] == str(i + 1) for i, x in enumerate(parts))
    
    res = '\n\n'.join('\n'.join(p[1:]) for p in parts)
    
    with open('KungFuPanda.txt', 'wb') as f:
        f.write(res.replace('\n', '\r\n').encode('utf-8'))


if __name__ == '__main__':
    to_gen()
