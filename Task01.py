from queue import Queue
import random
import time

queue = Queue(maxsize = 50)

def generate_request(queue: Queue) -> Queue:
    req_id = random.getrandbits(128)
    print(f"Request ID - {req_id} added to queue for processing")
    queue.put({"req_id":req_id, "request": "Reauest to do this and that"})
    return queue

def process_request(queue: Queue) -> None:
    if not queue.empty():
        id = queue.get()
        dots = "..."
        for i in range(1, random.randint(2, 12)):
            print(f"Request {id["req_id"]} processing {dots}")
            time.sleep(0.3)
            dots = dots + "..."
        print(f"Request {id["req_id"]} is completed")
    else:
        print(f"There is no requests left. all done")
        return 

if __name__ == "__main__":
    try:
        while True:
            q = generate_request(queue)
            process_request(q)
    except KeyboardInterrupt:
        print("\nstopped by user.")
        








