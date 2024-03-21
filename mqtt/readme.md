# readme

- 在本机安装 [Mosquitto](https://mosquitto.org/download/)
- 启动 mosquitto(配置文件: mosquitto.conf)
    
        mosquitto -c mosquitto.conf

- 启动消息观测器:

        python monitor.py


默认的配置信息为(应该修改为你自己的配置):

```
# 监听 MQTT 连接的端口
listener 1883

# 与兼容 RabbitMQ web mqtt 一致
listener 15675
protocol websockets

# 账户信息
username: dynalab
password: dynalab_rmq
```