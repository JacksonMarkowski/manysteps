import asyncio
import functools


class Recipe:
    def __init__(self):
        self.steps = {}
        pass

    def step(self, _func=None, *, depends=[]):
        def step_decorator(func):
            self.steps[func] = depends
            return func

        if _func is None:
            return step_decorator
        else:
            return step_decorator(_func)

    async def run(self):
        tasks = {}
        for step in self.steps.keys():
            tasks = self._start_step(step, tasks)

        all_tasks = []
        for step_task in tasks.values():
            all_tasks.append(step_task)

        if len(all_tasks) > 0:
            await asyncio.gather(*all_tasks)

    def _start_step(self, step, tasks):
        if step in tasks:
            return tasks

        deps_tasks = []
        for dep in self.steps[step]:
            tasks = self._start_step(dep, tasks)
            deps_tasks.append(tasks[dep])

        async def step_wrapper():
            if len(deps_tasks) > 0:
                await asyncio.gather(*deps_tasks)
            await step()

        task = asyncio.create_task(step_wrapper())
        tasks[step] = task
        return tasks
