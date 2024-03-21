# readme

```bash
mosquitto -c mosquitto.conf
```

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