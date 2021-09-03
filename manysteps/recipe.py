import asyncio
import functools


class Recipe:
    def __init__(self):
        self.steps = {}
        pass

    def step(self, *, depends=[]):
        def step_decorator(func):
            self.steps[func] = depends
            return func

        return step_decorator

    async def run(self):
        tasks = {}
        for step, step_ in self.steps.items():
            tasks = self.start_step(tasks, step)

        final_tasks = []
        for step, step_task in tasks.items():
            final_tasks.append(step_task)

        if len(final_tasks) > 0:
            await asyncio.gather(*final_tasks)

    def start_step(self, tasks, c):
        if c in tasks:
            return tasks

        c_d_tasks = []
        for c_d in self.steps[c]:
            tasks = self.start_step(tasks, c_d)
            c_d_tasks.append(tasks[c_d])

        async def step_dec():
            if len(c_d_tasks) > 0:
                await asyncio.gather(*c_d_tasks)
            await c()

        # print(f"starting {c}")
        t = asyncio.create_task(step_dec())
        tasks[c] = t
        return tasks
