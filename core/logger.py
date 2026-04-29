import datetime

class Logger:

    @staticmethod
    def log(message):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{now}] {message}")