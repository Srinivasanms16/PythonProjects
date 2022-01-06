import concurrent.futures
import time
import mypro


def callmultiThreading():
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as texecuter:
        texecuter.map(callmultiprocessings,range(10))
            


def callmultiprocessings():
    print("calling multiprocessing")
    mypro.callmultiproc()
