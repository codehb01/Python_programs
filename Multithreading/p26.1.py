# Program 26 : Implement a multithreading program for banking scenario to demonstrate RACE condition – 1) without and, ii) with LOCK

# 1.Without 
import threading
import time

# Shared resource
balance = 1000

def withdraw(amount):
    global balance
    if balance >= amount:
        time.sleep(0.1)  # simulate processing delay
        print(f"{threading.current_thread().name} withdrawing {amount}")
        balance -= amount
        print(f"Balance left: {balance}")
    else:
        print(f"{threading.current_thread().name} - Not enough balance!")

threads = []
for i in range(5):
    t = threading.Thread(target=withdraw, args=(300,), name=f"User-{i+1}")
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Final balance:", balance)
