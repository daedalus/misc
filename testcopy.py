import sys

def test(f1,f2):

    def _load(filename):
        data = ''
        fp = open(filename,'rb')
        recvbuf = fp.read(1024*128)
        while len(recvbuf) > 0:
                data += recvbuf
                recvbuf = fp.read(1024*128)
        fp.close()
        del recvbuf
        del fp
        return data

    def _save(data,filename):
        fp = open(filename,'wb')
        SIZE = 1024*128
        for i in xrange(0,len(data)-1,SIZE):
                wrbuf = data[i:i+SIZE]
                fp.write(wrbuf)
        fp.close()
        del fp
        del wrbuf
        del SIZE

    _save(_load(f1),f2)


test(sys.argv[1],sys.argv[2])
