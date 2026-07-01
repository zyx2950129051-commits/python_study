# 7. flush方法

概述：Python 写入文件时，并不是每写一次就立刻落盘，而是：先写到“缓冲区”里。

flush方法：把缓冲区中的数据，立刻写入到文件中。

测试代码：

```
import time
with open('demo.txt', 'at', encoding='utf-8') as file:
    file.write('你好1')
    file.write('你好2')
    file.flush()
    time.sleep(10000)
    file.write('你好3')
    file.write('你好4')
```
