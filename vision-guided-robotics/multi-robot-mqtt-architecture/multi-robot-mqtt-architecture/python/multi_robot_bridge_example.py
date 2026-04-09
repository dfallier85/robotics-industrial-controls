"""
multi_robot_bridge_example.py

A simple reference example showing how one Python process could subscribe to:
- robot/ur/cmd
- robot/abb/cmd

and publish responses to:
- robot/ur/response
- robot/abb/response

This is intentionally lightweight and meant as a teaching example.
"""

import json
import paho.mqtt.client as mqtt

MQTT_BROKER = "192.168.4.1"
MQTT_PORT = 1883

UR_CMD_TOPIC = "robot/ur/cmd"
UR_RESP_TOPIC = "robot/ur/response"

ABB_CMD_TOPIC = "robot/abb/cmd"
ABB_RESP_TOPIC = "robot/abb/response"


def handle_ur_command(command: str) -> dict:
    """
    Replace this stub with real UR bridge logic.
    """
    return {
        "robot": "ur",
        "requested_command": command,
        "result": "ok",
        "detail": f"Simulated UR handling for command: {command}",
    }


def handle_abb_command(command: str) -> dict:
    """
    Replace this stub with real ABB bridge logic.
    """
    return {
        "robot": "abb",
        "requested_command": command,
        "result": "ok",
        "detail": f"Simulated ABB handling for command: {command}",
    }


def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT broker with result code {rc}")
    client.subscribe(UR_CMD_TOPIC)
    client.subscribe(ABB_CMD_TOPIC)


def on_message(client, userdata, msg):
    topic = msg.topic
    command = msg.payload.decode().strip()

    if topic == UR_CMD_TOPIC:
        response = handle_ur_command(command)
        client.publish(UR_RESP_TOPIC, json.dumps(response))

    elif topic == ABB_CMD_TOPIC:
        response = handle_abb_command(command)
        client.publish(ABB_RESP_TOPIC, json.dumps(response))


def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_forever()


if __name__ == "__main__":
    main()
