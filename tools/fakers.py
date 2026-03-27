import time

def get_random_email() -> str:
    return f"test.{time.time()}@example.com" #time.time() - метка времени (кол-во сек с 1970)
