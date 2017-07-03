import os
from multiprocessing import Process
from job51.settings import CORENUM

class scheduler(object):

    @staticmethod
    def crawl():
        os.system('scrapy crawl gd_job')

    def run(self):
        names = locals()
        if CORENUM:
            for x in range(CORENUM):
                names['process%x' % x] = Process(target=scheduler.crawl)
                names['process%x' % x].start()

if __name__ == '__main__':
    r = scheduler()
    r.run()