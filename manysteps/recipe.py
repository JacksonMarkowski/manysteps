import asyncio
import functools

class Recipe:
    def __init__(self):
        self.steps = []
        self.dep = {}
        pass

    def step_dep(self, *, deps=[]):
        def step_dec(func):
            print(func)
            self.dep[func] = deps
            # own = self.dep.get(func, None)
            # if own is None:
            #     print("Adding own")
            #     self.dep[func] = []

            # for dep in deps:
            #     par = self.dep.get(dep, None)
            #     if par is not None:
            #         print("Adding dep to existing")
            #         par.append(func)
            #     else:
            #         print("adding dep to new")
            #         self.dep[dep] = func

            return func
        return step_dec

    async def run(self):

        tasks = {}
        for c, c_dep in self.dep.items():
            tasks = self.start_dep(tasks, c)

        final_tasks = []
        for c, c_task in tasks.items():
            final_tasks.append(c_task)
        
        if len(final_tasks) > 0:
            await asyncio.gather(*final_tasks)

    def start_dep(self, tasks, c):
        if c in tasks:
            return tasks

        c_d_tasks = []
        for c_d in self.dep[c]:
            tasks = self.start_dep(tasks, c_d)
            c_d_tasks.append(tasks[c_d])

        async def step_dec():
            if len(c_d_tasks) > 0:
                await asyncio.gather(*c_d_tasks)
            await c()
        
        print(f"starting {c}")
        t = asyncio.create_task(step_dec())
        tasks[c] = t
        return tasks

            


    def step(self, func):
        print("hi??")
        self.steps.append(func)
        return func