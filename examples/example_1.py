import asyncio

from manysteps import Recipe

r = Recipe()


@r.step(depends=[])
async def my_step_a():
    print("my_step_a enter")
    await asyncio.sleep(1)
    print("my_step_a exit")


@r.step(depends=[my_step_a])
async def my_step_b():
    print("my_step_b enter")
    await asyncio.sleep(5)
    print("my_step_b exit")


@r.step(depends=[my_step_a])
async def my_step_c():
    print("my_step_c enter")
    await asyncio.sleep(5)
    print("my_step_c exit")


# @manysteps.step(abc)
# @r.step()
# async def step1():
#     print("hi")

# def two(func):
#     async def wrapper():
#         print('e')
#         await func()
#         print('ex')
#     return wrapper

# @two
# async def one():
#     print("one")

# @two
# async def another_one():
#     print("another one")
#     await one()


async def main():
    # print(my_step1.__name__)
    # await bla()
    # for c in r.steps:
    #     await c()

    # print(r.dep)
    await r.run()
    # dummy()
    # print(dummy.__name__)

    # manysteps.exe(abc)
    # for c in r.steps:
    #     await c
    # await step1()
    # await one()
    # await another_one()


if __name__ == "__main__":
    asyncio.run(main())
