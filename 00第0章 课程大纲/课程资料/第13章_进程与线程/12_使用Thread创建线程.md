# 12. 使用 Thread 创建线程

首先我们要明确一个概念：任何一个正在运行的 Python 程序，至少都有一个线程！

1️⃣回顾一下我们之前的代码：

```
if __name__ == '__main__':
    print('主进程中的代码')
```

对于上述代码来说：print('主进程中的代码') 确实属于主进程，但更准确地说，是运行在主进程里的主线程中。

2️⃣线程是进程中的执行单位：

一个进程里，至少有一个线程（主线程）

一个进程里，也可以有多个线程

多个线程之间会： 共享进程的内存空间、 但执行顺序由操作系统调度。

3️⃣示例代码：

```
import os
import time
from threading import get_native_id, Thread, RLock

def speak(lock):
    for index in range(5):
        with lock:
            print(f'我在说话{index}, 进程pid是:{os.getpid()}, 线程编号:{get_native_id()}')
        time.sleep(1)

def study(lock):
    for index in range(5):
        with lock:
            print(f'我在学习{index}, 进程pid是:{os.getpid()}, 线程编号:{get_native_id()}')
        time.sleep(1)

if __name__ == '__main__':
    print(f'-------start------- 进程pid是:{os.getpid()}, 线程编号:{get_native_id()}')
    lock = RLock()
    # Thread 的参数：
    # 🔸group： 默认值为 None（应当始终为 None）。
    # 🔸target： 子线程要执行的可调用对象，默认值为 None。
    # 🔸name： 线程名称，默认为 None。如果设置为 None，Python 会自动分配名字
    # 🔸args： 给 target 传的位置参数（元组）。
    # 🔸kwargs： 给 target 传的关键字参数（字典）。
    # 🔸daemon： 标记线程是否为守护线程，取值为布尔值（默认为 None）。
    # 使用 Thread 创建线程对象
    t1 = Thread(target=speak, args=(lock,))
    t2 = Thread(target=study, args=(lock,))
    # 调用线程对象的 start 方法，会立刻将该线程交由操作系统进行调度。
    t1.start()
    t2.start()
    # 让主线程等 t1和t2 线程执行完毕后，主线程再继续执行。
    t1.join()
    t2.join()
    print('-------end-------')
```
