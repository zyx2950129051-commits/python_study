# 9. 使用 Pipe 实现进程通信

Pipe 就像一根“水管”，一头负责发送，另一头负责接收。

1️⃣ 创建管道

```
# Pipe() 会返回两个连接对象，它们分别代表管道的两端。
# duplex用于控制管道为单向还是双向，True表示双向，False表示单向
con1, con2 = Pipe(duplex=True)

# 单向 Pipe 的规则：con1只能发送，con2只能接收。
```

2️⃣发送与接收

send方法： 向管道中发送数据。

recv方法： 从管道中接收数据。

3️⃣测试代码：

```
import time
from multiprocessing import Process, Pipe

def test1(con1):
    time.sleep(2)
    con1.send(100)
    print('test1发送了100')

def test2(con2):
    data = con2.recv()
    print(f'test2接收了{data}')


if __name__ == '__main__':
    con1, con2 = Pipe(duplex=False)
    p1 = Process(target=test1, args=(con1,))
    p2 = Process(target=test2, args=(con2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
```
