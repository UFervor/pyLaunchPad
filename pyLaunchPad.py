import sqlite3
from contextlib import contextmanager
import threading
import json


_local = threading.local()


@contextmanager
def acquire(*locks):
    locks = sorted(locks, key=lambda x: id(x))
    acquired = getattr(_local, 'acquired', [])
    if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):
        raise RuntimeError('Lock Order Violation')
    acquired.extend(locks)
    _local.acquired = acquired
    try:
        for lock in locks:
            lock.acquire()
        yield
    finally:
        for lock in reversed(locks):
            lock.release()
        del acquired[-len(locks):]


class pyLaunchPad():
    def __init__(self, dbp="./db"):
        self.conn = sqlite3.connect(dbp, check_same_thread=False, timeout=5)
        self.cur = self.conn.cursor()
        self.Lock = threading.Lock()
    
    def fetchAll(self, table):
        with acquire(self.Lock):
            self.cur.execute(
                f"SELECT * FROM {table}", ())
            rows = self.cur.fetchall()
            columns = [description[0] for description in self.cur.description]

        results = []
        for row in rows:
            result = dict(zip(columns, row))
            results.append(result)
                
        return results
