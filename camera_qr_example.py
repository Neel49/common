"""
Camera to QR scanner example
"""

import cv2

from camera.modules import camera_device
from qr.modules import qr_scanner


if __name__ == "__main__":

    camera = camera_device.CameraDevice(0, 0, "")

    text = ""
    while True:
        result, image = camera.get_image()
        if not result:
            continue

        cv2.imshow("Camera", image)

        result, text = qr_scanner.QrScanner.get_qr_text(image)
        if result:
            break

        # Required for image display
        # Delay for 100 ms
        cv2.waitKey(100)

    print(text)

    print("Done!")
