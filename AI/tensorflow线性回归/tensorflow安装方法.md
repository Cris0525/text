# TensorFlow的安装方法
----
## 基于Ubuntu(版本16.04)


1. 确定好自己的Python版本是Python2还是Python3.

2. 安装对于的pip依赖包,如果有则进行一次更新确认

   > * Python2:sudo pip install --upgrade pip
   > * Python3:sudo pip3 install --upgrade pip

3. 进行安装TensorFlow,选择安装CPU版本或者GPU版本(目前我们三人都是安装的CPU版本)

   CPU版本安装命令如下:

   > * python 2：sudo pip install tensorflow
   > * python 3：sudo pip3 install tensorflow

   GPU版本安装命令如下(暂时并未进行安装GPU版本):
        
   > * python 2.7版本：sudo pip install tensorflow-gpu 
   > * python 3.x版本：sudo pip3 install tensorflow-gpu 
----

### TensorfFowCPU版本与GPU版本的区别
![cmd-markdown-logo](https://img-blog.csdn.net/20171212165304607?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc2luYXRfMzY0NTg4NzA=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

1. Cache, local memory(本地存储器)： CPU > GPU
2. Threads(线程数): GPU > CPU
3. Registers（寄存器）: GPU > CPU 多寄存器可以支持非常多的Thread
4. thread(线程)需要用到register,thread数目大register也必须得跟着很大才行。
5. SIMD Unit(单指令多数据流,以同步方式，在同一时间内执行同一条指令): GPU > CPU。



CPU有强大的ALU, 可以在很少的时钟周期内完成算术计算，可以达到64bit  双精度，执行双精度浮点源算的加法和乘法只需要1～3个[时钟周期].CPU版本的适合计算高精度的运算



GPU是基于大的吞吐量,适合计算密集型的程序和易于并行的程序,通俗来讲就是适合做数据量大但是简单的运算
