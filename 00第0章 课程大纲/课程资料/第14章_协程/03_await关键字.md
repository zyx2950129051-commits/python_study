# 3. await 关键字

```
await 关键有三个作用：
```

挂起：await 会暂停当前协程的执行。

等待：遇到 await 关键字，事件循环会立即安排 await 后面的对象去执行，并等待该对象执行完成，并且可以拿到执行结果。

💡关键点：在执行 await 后面的对象时，会出现两种情况:

情况一：如果在执行该对象中的代码时，遇到了【await I/O操作】（需要等待外部资源返回结果的操作）例如：网络请求、文件读写等，那 CPU 的控制权就会交给事件循环。事件循环会去调度循环中的其他任务（如果有的话）。

情况二：如果该对象中的代码，不包含任何【await I/O操作】。例如：print打印、数学计算、逻辑计算等。此时事件循环拿不到 CPU 控制权，无法调度循环中的其他任务，不会发生任务切换。

恢复：当 await 后的对象执行完毕，事件循环会恢复之前被挂起的协程，该协程会从当时挂起的位置继续执行，并拿到返回值。

🚨注意：await 后面只能写『可等待对象』，常见可等待对象有：协程对象、Future对象、Task对象。

```
import asyncio

async def work():
    print('work开始')
    print('work执行中......')
    # await去等待一个协程对象（靠asyncio.sleep方法，返回一个协程对象）
    res = await asyncio.sleep(2)
    print(res)
    print('work结束')
    return '工作结果'

async def main():
    print('main开始')
    # await去等待一个协程对象（靠自己去编写协程函数，随后调用该函数来得到协程对象）
    res = await work()
    print(res)
    print('main结束')
    return 'main的返回值'

result = asyncio.run(main())
print(result)
```
