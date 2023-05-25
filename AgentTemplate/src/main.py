import asyncio
import datetime

import novelcraft.sdk as sdk


async def main():
    await sdk.initialize()
    sdk.get_logger().info('Hello, world!')

    start_time = datetime.datetime.now()
    count = 0
    count_10 = 0

    while True:
        if (datetime.datetime.now() - start_time).total_seconds() > 60:
            break

        # Required to keep the SDK alive
        await asyncio.sleep(0.1)
        agent = sdk.get_agent()

        if agent is None:
            continue
        count_10 = int(count / 10) % 2
        if count_10 == 0:
            agent.set_movement(sdk.IAgent.MovementKind.RIGHT)
            agent.jump()
        else:
            agent.set_movement(sdk.IAgent.MovementKind.LEFT)
            agent.jump()
        count += 1

    await sdk.finalize()
    sdk.get_logger().info('Goodbye, world!')

if __name__ == '__main__':
    asyncio.run(main())
