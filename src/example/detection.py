from is_wire.core import Channel, Subscription
from is_msgs.image_pb2 import Image
from src.utils import to_np
import cv2
import socket

broker_uri = "amqp://guest:guest@10.10.2.211:30000"
channel = Channel(broker_uri)
subscription = Subscription(channel)

subscription.subscribe("tiffanyDetector.*.Rendered")
# print("Waiting rendered images...")

while True:
    try:
        msg = channel.consume(timeout=5.0)
        image_pb = msg.unpack(Image)
        frame = to_np(image_pb)

        cv2.imshow("Tiffany Detector", frame) # Show image

        # Close window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    except socket.timeout:
        print("No images received.")

cv2.destroyAllWindows()
