from concurrent.futures import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor
from time import sleep


def fun1(sec):
    print("execute start")
    sleep(sec)
    print("execute end")

def callmultiproc():
    #max_workers is maxing number of process you want to create.
    with ProcessPoolExecutor(max_workers=3) as pexecuter:
        for _ in range(10):
            pexecuter.submit(fun1,1)
    with ThreadPoolExecutor(max_workers=5) as thexecuter:
        for _ in range(10):
            thexecuter.submit(fun1,10)
