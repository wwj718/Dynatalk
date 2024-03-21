# #!/usr/bin/env python

# remix from ./receive_logs_topic.py


"""
# https://www.rabbitmq.com/tutorials/tutorial-five-python.html
# https://github.com/rabbitmq/rabbitmq-tutorials/blob/main/python/receive_logs_topic.py

Install:
    python -m pip install paho-mqtt python-dotenv

Usage:

-    python monitor.py  订阅所有消息
-    python monitor.py "+" 订阅所有消息
-    python monitor.py --topics "*_roblox" 订阅所有 action 消息
"""

import sys
import os
import time
import json
import argparse
import paho.mqtt.client as mqtt
from dotenv import load_dotenv

load_dotenv()

def main(topics=None, json_only=False):
    if not topics:
        topics = ["+"]
    # print(topics, json_only)
    # return
    if True:

        # The callback for when the client receives a CONNACK response from the server.
        def on_connect(client, userdata, flags, rc):
            # print("Connected with result code " + str(rc))
            if rc == 0:
                print("Connected to MQTT broker successfully")
            else:
                print(f"Connection to MQTT broker failed with error code {rc}")
            for i in topics:
                mqtt_client.subscribe(i)

        # def callback(body, message):
        def _on_message(client, userdata, msg):
            # %r: raw string, repr()
            def set_string_color(text, color):
                reset_color = "\033[0m"
                color_map = {
                    "green": "\033[32m",
                    "red": "\033[31m",
                    "blue": "\033[34m", 
                    "yellow": "\033[33m"
                }
                return color_map.get(color, reset_color) + text + reset_color
            
            body = msg.payload

            # verify the message
            try:
                body_json = json.loads(body) # json strings may have different formats, unified style
                assert "to" in body_json
                assert "from" in body_json
                assert "action" in body_json
            except:
                print(f'{{"bad message": {body} }}')
                return
            # add timestamp, time when the message was received
            # import datetime
            # body_json["timestamp"] = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            format_body = json.dumps(body_json, sort_keys=True)

            # --json-only
            if json_only:
                print(format_body, flush=True)
            else:
                
                from_to = set_string_color(f'{body_json["from"]} -> {body_json["to"]}', "green")
                routing_key = f'routing_key : {msg.topic}'
                delimiter = set_string_color("|", "yellow")
                print(" [x] %s %s %s %s %s" % (from_to, delimiter, format_body, delimiter, routing_key), flush=True) # flush for linue pipline |


        mqtt_host = os.environ.get("MQTT_HOST", "localhost")
        mqtt_port = int(os.environ.get("MQTT_PORT", 1883))
        mqtt_username = os.environ.get("MQTT_USERNAME", "guest")
        mqtt_password = os.environ.get("MQTT_PASSWORD", "guest")

        mqtt_client = mqtt.Client()
        mqtt_client.on_connect = on_connect
        mqtt_client.on_message = _on_message
        mqtt_client.username_pw_set(mqtt_username, mqtt_password)
        mqtt_client.connect(mqtt_host, mqtt_port, 60)
        mqtt_client.loop_forever()  # blocking

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python script with --topics and --json-only options.")
    parser.add_argument("--topics", nargs="*", help="List of topics.")
    parser.add_argument("--json-only", action="store_true", default=False, help="Enable JSON-only mode.")
    args = parser.parse_args()
    if not args.json_only:
        print(f'Dynatalk host: {os.getenv("MQTT_HOST")}', flush=True)
    try:
        main(topics=args.topics, json_only=args.json_only)
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
