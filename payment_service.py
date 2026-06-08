import time

def process_payment(amount):
    retries = 3

    for _ in range(retries):
        try:
            print(f"Processing {amount}")
            return True
        except:
            time.sleep(1)

    return False
