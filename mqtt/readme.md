# readme

dynatalk 支持常见的 MQTT broker(mosquitto(参考页底的 FAQ), [emqx](https://www.emqx.com/zh) 等)。

最简单的方式是下载并运行 DynatalkHub (内置了一个 MQTT broker):

-   [MacOS](https://scratch3-files.just4fun.site/DynatalkHub-0.2.0-mac.zip)
-   [Windows](https://scratch3-files.just4fun.site/DynatalkHub-0.2.0-win.zip)
-   [Linux](https://github.com/wwj718/Dynatalk/tree/main/mqtt)

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

## 关于安全性

- 不允许匿名连接
  - 目前的默认配置
- 如果确实需要来自局域网的连接, 请修改默认 mqtt 密码
  - 可以使用自己的手机热点提高安全性
- Agent 解释消息时, 当心使用 eval.
