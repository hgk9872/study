import asyncio
import time

# # Syncronous version
# def task():
#     print('hello')
#     time.sleep(1)
#     print('world')

# def main():
#     for _ in range(3):
#         task()

# if __name__ == '__main__':
#     # returns the float value of time in seconds
#     start = time.perf_counter() # 현재 시간 check
#     main()
#     time_took = time.perf_counter() - start
#     print(f'it took {time_took} seconds.')



# single event loop
async def task():
    print('hello')

    # return the control back to "event loop"
    await asyncio.sleep(1)
    print('world')


async def main():
    await asyncio.gather(task(), task(), task()) # 또 다른 coroutine)


if __name__ == "__main__":
    # returns the float value of time in seconds
    start = time.perf_counter()
    asyncio.run(main()) # asyncio.run 하는 순간에 event loop 실행
    # main() coroutine을 event loop안으로 던짐
    time_took = time.perf_counter() - start
    print(f'it took {time_took} seconds.')