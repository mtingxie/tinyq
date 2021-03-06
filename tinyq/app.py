# -*- coding: utf-8 -*-
from redis import StrictRedis

from tinyq.constants import DEFAULT_SCHEDULE_QUEUE_KEY, DEFAULT_JOB_QUEUE_KEY
from tinyq.queue import RedisQueue
from tinyq.task import Task


class Application:
    """
    :

        app = Application('redis://')

        @app.task()
        def add(m, n):
            return m + n

        add.delay(2, 3)

    """
    def __init__(self, redis_uri='redis://',
                 schedule_queue_key=DEFAULT_SCHEDULE_QUEUE_KEY,
                 job_queue_key=DEFAULT_JOB_QUEUE_KEY):
        self.schedule_queue = RedisQueue(redis_uri, schedule_queue_key)
        self.job_queue = RedisQueue(redis_uri, job_queue_key)

    def task(self, name=None):
        """

        :param name: task name
        :return:
        """
        task = Task(self.schedule_queue)
        return task(name=name)
