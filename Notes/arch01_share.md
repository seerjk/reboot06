arch01_share
> date:2016-1-10

## 控制系统目标
最大单一任务数 2^32
平均响应时间 500ms
安全 Blowfish 权限控制，信道加密
可追溯 100% 所有过程可追溯

## 任务控制
* 并发控制
滑动窗口模型

* 控制人物
*状态回调

### 速度
hermes
ssh

zerrMQ
veryMQ

### 安全
百度 华北机房 ping 10ms
360 郑州 汇聚节点  全国3个汇聚节点，所有机房专线连过来
    70个机房

* 严格的权限树限制
    - 插件审核机制
    - 用户只能操作自己有权限的树节点

* agent控制信道加密 SSL
    ECCDH + AES 256 CTR

## 整体架构
分布式控制系统
baidu 没有crontab 靠系统做集中式的crontab
机器可以随意替换

控制与监控同一套agent

### 分布式控制系统
redis 全异步非阻塞单线程模型
nginx 全异步非阻塞多进程模型

memcache改造的模型
    全异步非阻塞多线程模型
    gko_pool
    
内置特别诱惑过的内存池实现
    gkoAlloc

异步DNS查询
        DNS over TCP
        cares+libev (curl)
        从python的gevent库学来的
        dns递归模型
            权威
            授权
    
微信 如何在1s内将发送的消息推送到对方
    推送方式

高性能客户端编程：端口扫描、DDoS攻击

### 分布式调度器

不能有单点
Raft分布式一致性算法(简化的Paxos)，
    [CAP 定理](http://zhuanlan.zhihu.com/auxten/20399316)
    从Paxos到Zookeeper到Raft

任务以来&定时模型

Powered by Golang
    go 开发效率高

长连接，HTTP接口

[CAP 定理](http://zhuanlan.zhihu.com/auxten/20399316)

它指出对于一个分布式计算系统来说，不可能同时满足以下三点：
* 一致性 (Consistency)（等同于所有节点访问同一份最新的数据副本）
* 可用性（Availability）（对数据更新具备高可用性）
* 网络分区容忍性（Partition tolerance）（以实际效果而言，分区相当于对通信的时限要求。系统如果不能在时限内达成数据一致性，就意味着发生了分区的情况，必须就当前操作在C和A之间做出选择。）

硬件不改变，提升一点，需要降低其他的

hash 多用于解决性能问题

优雅降级

多副本写入 sharding模式
    可用性下降 (两个都写入成功才算成功)
    写的可用性降低 -- 读的可用性上升 (多读少写)
    降低一致性来提升可用性 (写一个成功，就算成功)

多副本 同步 -- cluster模式 集群模式
    写其中一个，同步完成才任务写成功
    写可用性下降，取决于同步线路(分区可容忍性下降)

    牺牲一致性，提升分区可容忍性
        mysql 主从
        写入主，认为成功，主从同步后续进行

为什么多数DB放弃一致性，换取 分区可容忍性 和 可用性
    互联网的业务驱动，一致性要求不高
    银行的一致性要求高(放弃分区可容忍性 和 可用性，保证强一致性)

提升或降低硬件可以使CAP一起升或者降
    银行，砸钱，砸硬件，死抓一致性，同时提升分区可容忍性和可用性
    浪潮pc server成本更低
    浪潮大型机 只有一台(强一致性保证)

cluster和sharding对比 表格
    补充

## 心得

Architecture is shit, all in details.
细节和整体代码质量
* 性能调优
    调优是不断的try & profiler
    没有捷径，网上各种kernel、网络、编译器优化基本都是误导
* 高可用
    简洁即可靠，架构的实现要考虑现有人员的技术水平和能力
    但总归简单总是不容易出错的
* 语言
    python很适合糙快猛的做原型出来
    golang在服务端几乎可以代替c/c++
    java适合做很复杂业务逻辑，不适合做较为底层的高性能服务
        高层次抽象 复杂-->简单
* 新技术
    不要为了追新而引入新技术
    引入新技术的前提是要吃透
* 学习
    基础总是很重要的 (linux系统, tcp/ip)
    基础好了才能低成本的学习新技术
* 文档
    文档工作很重要，做项目前最好把项目实现的细枝末节全部想清楚
    拿到文档能重新实现


# 运维职业规划

http://blog.csdn.net/apache0554/article/details/44955265

http://zhidao.baidu.com/link?url=W7vCtvhdzTlUeioCN4mhGBOzd1pKA6HmKd-qaB_PjAynCP2u_SBxSfigvnynmpa2io5LYxWlqxIWAle6DFVnOqA

不要把运维当成最终的职业

公司人数 / 25 = CTO (5000人 -- 200w)

运维在IT中待遇偏低

技术在一段时间内被高估，在长远时间内被低估
运维长远背黑锅
运维出事的时候才被想到

US今天是我们5年后的今天。
    没有下机房和搞交换机的运维
    Amazon的云

入学试题