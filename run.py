import os
from multiprocessing import Process
try:
    from job51.settings import CORE_NUMBER
except:
    CORE_NUMBER=None

class scheduler(object):

    def __init__(self):
        self.core_number = CORE_NUMBER

    @staticmethod
    def crawl():
        os.system('scrapy crawl gd_job')

    def run(self):
        names = locals()
        if self.core_number:
            for x in range(self.core_number):
                names['process%x' % x] = Process(target=scheduler.crawl)
                names['process%x' % x].start()


if __name__ == '__main__':
    r = scheduler()
    r.run()

