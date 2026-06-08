from is_wire.core import Channel, Subscription
from is_msgs.image_pb2 import ObjectAnnotations
import socket

# Create a channel and a subscription for replies
broker_uri = "amqp://guest:guest@10.10.2.211:30000"
channel = Channel(broker_uri)
subscription = Subscription(channel)

# Receives rendered images from any camera.
subscription.subscribe("tiffanyDetector.*.Detection")
# print("Waiting images...")

while True:
    try:
        msg = channel.consume(timeout=5.0) # Please wait for a message for up to 5 seconds.
        detections = msg.unpack(ObjectAnnotations)

        print("New detection")
        print("Topic:", msg.topic)
        print(detections)

        print("Objects detected: ", len(detections.objects))
      
    except socket.timeout:
        print("No reply.")
