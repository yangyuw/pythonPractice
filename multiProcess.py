# from multiprocessing import Pool
# import os, time, random
#
# def long_time_process(name):
#     print('process start %s (%s)...' % (name, os.getpid()))
#     startTime = time.time()
#     time.sleep(random.random() * 5)
#     endTime = time.time()
#     print ('process cost %.2f seconds.' % (endTime - startTime))
#
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_process, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')

# import subprocess
#
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print (output.decode('utf-8'))
# print ('Exit code:', p.returncode)

# from multiprocessing import Process, Queue
# import os, time, random
#
# def write(q):
#     print('process to write: %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print ('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random() *3)
#
# def read(q):
#     print ('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)
#
# if __name__=='__main__':
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     pw.start()
#     pr.start()
#     pw.join()
#     pr.terminate()

# import time, threading
#
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print ('thread %s ended.' % threading.current_thread().name)
#
# print ('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread.')
# t.start()
# t.join()
# print ('thread %s ended.' % threading.current_thread().name)

# import time, threading
#
# balance = 0
# lock = threading.Lock()
#
# def change_it(n):
#     global balance
#     balance = balance + n
#     balance = balance - n
#
# def run_thread(n):
#     for i in range(100000):
#         lock.acquire()
#         try:
#             change_it(n)
#         finally:
#             lock.release()
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

# import threading, multiprocessing
#
# def loop():
#     x = 0
#     while True:
#         x = x ^ 1
#
# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     t.start()

# import threading
# local_school = threading.local()
# def process_student():
#     std = local_school.student
#     print('Hello, %s (in %s)' % (std, threading.current_thread().name))
#
# def process_thread(name):
#     local_school.student = name
#     process_student()
#
# t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
# t2 = threading.Thread(target=process_thread, args=('James',), name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.sina.com.cn', 80))
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
s.close()