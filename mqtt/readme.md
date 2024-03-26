# readme

- 在本机安装 [Mosquitto](https://mosquitto.org/download/)
- 启动 mosquitto(配置文件: mosquitto.conf)
    
        mosquitto -c mosquitto.conf

- 启动消息观测器:

        # pip install dynatalk
        dynatalk-monitor


默认的配置信息为(应该修改为你自己的配置):

```
# 监听 MQTT 连接的端口
listener 1883

# 与兼容 RabbitMQ web mqtt 一致
listener 15675
protocol websockets

# 账户信息
username: guest
password: test
```

## 安全

- 不允许匿名连接
  - 目前的默认配置
- 仅允许本地连接
  - `listener 1883` 表示允许来自外部的连接。
  - 监听特定 ip, 可能会[出问题](https://stackoverflow.com/questions/66285014/why-does-my-mosquitto-broker-fail-to-start-on-boot-but-works-when-started-manua)
- 如果确实需要局域网的连接, 不要使用当前仓库默认 mqtt 密码
  - 可以使用自己的手机热点提高安全性
- Agent 解释消息时, 当心使用 eval.



# FAQ

## 生成 MQTT 账号密码

```bash
# 添加 用户名: guest  密码:test 
mosquitto_passwd -b mosquitto_passwordfile guest test
```