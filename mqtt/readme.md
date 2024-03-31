# readme

- 确保本地安装了 Python(版本不低于 3.8)
- 安装 dynatalk

        python -m pip install dynatalk

- 启动 dynatalk 内置的 MQTT broker:
    
        dynatalk-hub

- 启动消息观测器(可选):

        dynatalk-monitor


默认的配置信息为:

```
tcp port: 1883

websockets port: 15675

# 账户信息
username: guest
password: test
```

## 安全

- 不允许匿名连接
  - 目前的默认配置
- 如果确实需要来自局域网的连接, 请修改默认 mqtt 密码
  - 可以使用自己的手机热点提高安全性
- Agent 解释消息时, 当心使用 eval.

# FAQ

## 如何修改账号信息

通过环境变量修改 broker 账户信息：

- MQTT_USERNAME
- MQTT_PASSWORD

## 使用 mosquitto 作为 MQTT broker

1. 下载 [mosquitto](https://mosquitto.org/download/)
2. 下载当前仓库, 进入 mqtt 目录中运行:

`mosquitto -c mosquitto.conf`