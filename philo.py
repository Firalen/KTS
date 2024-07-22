import threading
import time
import random

class Philosopher(threading.Thread):
    def __init__(self, id, left_fork, right_fork, table_lock):
        threading.Thread.__init__(self)
        self.id = id
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.table_lock = table_lock

    def run(self):
        while True:
            self.think()
            self.eat()

    def think(self):
        print(f"Philosopher {self.id} is thinking.")
        time.sleep(random.uniform(1, 3))

    def eat(self):
        print(f"Philosopher {self.id} is hungry.")
        
        with self.table_lock:  # Critical section start
            with self.left_fork:
                print(f"Philosopher {self.id} picked up left fork.")
                with self.right_fork:
                    print(f"Philosopher {self.id} picked up right fork.")
                    print(f"Philosopher {self.id} is eating.")
                    time.sleep(random.uniform(1, 3))
                    print(f"Philosopher {self.id} put down right fork.")
                print(f"Philosopher {self.id} put down left fork.")
        # Critical section end

def main():
    forks = [threading.Lock() for _ in range(5)]
    table_lock = threading.Lock()  # Mutex for the critical section
    philosophers = [Philosopher(i, forks[i], forks[(i + 1) % 5], table_lock) for i in range(5)]

    for philosopher in philosophers:
        philosopher.start()

    for philosopher in philosophers:
        philosopher.join()

if __name__ == "__main__":
    main()
