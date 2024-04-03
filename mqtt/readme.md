# readme

dynatalk 支持常见的 MQTT broker(mosquitto(参考页面底下的 FAQ), [emqx](https://www.emqx.com/zh) 等)。

最简单的方式是下载并运行 DynatalkHub (内置了一个 MQTT broker):

-   [MacOS](https://scratch3-files.just4fun.site/DynatalkHub-0.2.0-mac.zip)
-   [Windows](https://scratch3-files.just4fun.site/DynatalkHub-0.2.0-win.zip)
-   Linux 可在 Python 中运行 DynatalkHub (参考页面底下的 FAQ)

# FAQ

##  DynatalkHub 的 MQTT broker 默认配置

```
tcp port: 1883

websockets port: 15675

# 账户信息
username: guest
password: test
```

## 在 Python 中运行 DynatalkHub

- 确保本地安装了 Python(版本不低于 3.8)
- 安装 dynatalk

        python -m pip install dynatalk

- 启动 dynatalk 内置的 MQTT broker:
    
        dynatalk-hub

通过环境变量修改 broker 账户信息：

- MQTT_USERNAME
- MQTT_PASSWORD

## 使用 mosquitto 作为 MQTT broker

1. 下载 [mosquitto](https://mosquitto.org/download/)
2. 下载当前仓库, 进入 mqtt 目录中运行:

`mosquitto -c mosquitto.conf`

## 启动消息观察器

- 确保本地安装了 Python(版本不低于 3.8)
- 安装 dynatalk

        python -m pip install dynatalk

- 启动消息观测器(可选):

        dynatalk-monitor

## 使用 emqx broker

使用公网 broker 的好处是, 用户无需本地安装。

以下是一个位于公网上的 [emqx](https://www.emqx.com/zh) broker。

```
url: mqtt.aimaker.space
默认用户名/密码: guest/test
tcp port: 1883
tls port 8883
websockets port: 8084
```

- [MicroBlocks demo](https://microblocksfun.cn/run/microblocks.html?#project=https://wwj718.github.io/post/img/dynatalk-emqx-20240331.ubp)
- [Snap! demo](https://codelabclub.github.io/Snap/snap.html#open:https://wwj718.github.io/post/img/dynatalk-emqx-20240331.xml)
- [Python demo](https://github.com/wwj718/dynatalk-py/blob/main/Workspace-emqx.ipynb)
- [JavaScript demo](https://github.com/wwj718/dynatalk-js?tab=readme-ov-file#%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8%E5%85%AC%E7%BD%91-emqx-%E6%9C%8D%E5%8A%A1%E5%99%A8)

## 关于安全性

- 不允许匿名连接
  - 目前的默认配置
- 如果确实需要来自局域网的连接, 请修改默认 mqtt 密码
  - 可以使用自己的手机热点提高安全性
- Agent 解释消息时, 当心使用 eval.

## 视频介绍

[在线视频](https://www.bilibili.com/video/BV1Fr42187ip/)