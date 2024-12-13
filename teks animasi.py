import time

def animated_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)
    print()

animated_text("Halo, selamat datang di Python!")
