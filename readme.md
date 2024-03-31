# Dynatalk

Dynatalk 致力于对象之间的交流, 尤其关心不同语言/环境之间的互操作。

构建 Dynatalk 的原因: 我喜欢在 Squeak 进行探索性编程, 但 Squeak 第三方库不够丰富。 渴望一个简单的跨语言的对象协作机制, 在需要时, 就可以在 Squeak里使用 Python 或浏览器的 API。

## Get started

Dynatalk 使用 MQTT 来传递消息, 需要[运行一个 MQTT broker](./mqtt/readme.md).

然后在以下语言的客户端中开始编程。

## Supported languages

Dynatalk 支持多种编程语言

- [dynatalk-js](https://github.com/wwj718/dynatalk-js)
- [dynatalk-squeak](https://github.com/wwj718/dynatalk-squeak)
- [dynatalk-py](https://github.com/wwj718/dynatalk-py)
- [dynatalk-MicroBlocks](https://github.com/wwj718/dynatalk-MicroBlocks)
- [dynatalk-snap](https://github.com/wwj718/dynatalk-snap)

## 开发笔记

<!--"软件只是心智成熟的副产品", 思考本身是更重要的, 记录它们-->

和 [SqueakJS](https://github.com/codefrau/SqueakJS)类似, 最初的 Dynatalk 以探索性编程的风格在 [LivelyKernel](https://github.com/LivelyKernel/LivelyKernel) 中开发, 受益于 LivelyKernel 强大的 liveness, 开发过程高效而愉快。

### 消息结构

参考 [消息结构](./docs/消息结构.md)

### 设计理念

参考 [设计理念](./docs/设计理念.md)


## roadmap

- interpret 的进程机制
    -   supervisor 与 agent 直接使用消息队列，降低耦合
- 更多 space
    -   内部通信
- DynatalkHub