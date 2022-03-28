import socket
import time

IP = "212.129.38.224"
PORT = 51015
BUFFER_SIZE = 1024


def timing_attack():
    # ip address of challenge01.root-me.org

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    data = s.recv(BUFFER_SIZE)
    print(data.decode())

    time_char = 0
    char_found = ""
    key = ""

    while len(key) < 12:
        # the charset is only "0123456789-" but we didn't know before we solved the challenge
        for char in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
            message = key + char

            s.send(message.encode())

            start = time.time()
            s.recv(BUFFER_SIZE)
            finish = time.time()

            delay = finish - start
            if delay > time_char:
                time_char = delay
                char_found = char

        key += char_found
        time_char = 0
        print(f"key : {key + '*' * (12 - len(key))}")
    s.close()
    return key


if __name__ == "__main__":
    timing_attack()