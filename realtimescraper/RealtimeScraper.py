import queue
import threading
from concurrent.futures import ThreadPoolExecutor
import twint
import time
from datetime import datetime, timedelta

class RealtimeScraper:

    def __init__(self, search_string, limit):
        self.q = queue.Queue()
        self.config = self.create_twint_context(search_string, limit)

    def start_scrambler(self):
        executor = ThreadPoolExecutor(5)
        printer = threading.Thread(target=self.worker, daemon=True)
        printer.start()
        self.scramble_tweets(executor)

    def create_twint_context(self, search_string, limit):
        c = twint.Config()
        c.Limit = limit
        c.Search = search_string
        c.Hide_output = True
        c.Pandas = True
        return c

    def worker(self):
        print("created worker, starting printing")
        while True:
            print(self.q.get())
            self.q.task_done()

    def queuer(self, config, message):
        twint.run.Search(config)
        pd_df = twint.output.panda.Tweets_df
        tweets = pd_df[["tweet"]]
        print(len(tweets))
        print(type(tweets))
        for index, row in tweets.iterrows():
            self.q.put(row["tweet"])
        return message

    def scramble_tweets(self, executor):
        while True:
            print("\nscrambling tweets")
            since_time = datetime.now() - timedelta(days=0, hours=0, minutes=1)
            future = executor.submit(self.queuer, self.config, "Completed")
            since_time_formatted = since_time.strftime("%Y-%m-%d %H:%M:%S")
            self.config.Since = since_time_formatted
            print("sleeping")
            time.sleep(59)
            print(future.result())
            time.sleep(1)
