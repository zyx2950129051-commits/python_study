# 8. 使用 Queue 实现进程通信

进程之间是不共享数据的，那如果进程之间如何进行数据沟通（进程通信）呢？手段多种多样，我们本小节给大家说通过Queue 实现进程通信。

核心思想： 一个进程负责生产数据，另一个进程负责消费数据，中间通过 Queue 进行“传话”

```
import time
from multiprocessing import Process, Queue

# 子进程1：往队列里放数据
def test1(q):
    for index in range(5):
        print(f'【test1】放入数据：{index}')
        q.put(index)
        time.sleep(0.5)

# 子进程2：从队列里取数据
def test2(q):
    for index in range(5):
        data = q.get()
        print(f'【test2】取出数据：{data}')
        time.sleep(1)

if __name__ == '__main__':
    q = Queue()

    p1 = Process(target=test1, args=(q,))
    p2 = Process(target=test2, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
```

备注：q 是在主进程中创建的，但可以被子进程使用，因为 multiprocessing.Queue是跨进程的。

为什么数据不会乱掉？ —— 因为队列是先进先出的。
