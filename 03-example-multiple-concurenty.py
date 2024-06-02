import os
import asyncio
import json
from scaler_pics import Scaler, TransformOptions, InputOptions, OutputOptions, Fit, ImageDelivery

api_key = os.getenv('API_KEY', 'YOUR_API_KEY')
scaler = Scaler(api_key)


async def main():
    time_start = time.time()
    tasks = []
    count = 10

    for i in range(count):
        tasks.append(transform_image(i))

    await asyncio.gather(*tasks)

    print(f'Total time for {count} concurrent transforms: {
          time.time() - time_start:.2f} seconds')


async def transform_image(index):
    options = TransformOptions(
        input=InputOptions(localPath=f'images/test-{index + 1}.heic'),
        output=[
            OutputOptions(
                type='jpeg',
                fit=Fit(width=1280, height=1280),
                quality=0.8,
                imageDelivery=ImageDelivery(
                    saveToLocalPath=f'results/output-{index}-1280.jpeg')
            ),
            OutputOptions(
                type='jpeg',
                fit=Fit(width=1024, height=1024),
                quality=0.8,
                imageDelivery=ImageDelivery(
                    saveToLocalPath=f'results/output-{index}-1024.jpeg')
            ),
            OutputOptions(
                type='jpeg',
                fit=Fit(width=512, height=512),
                quality=0.8,
                imageDelivery=ImageDelivery(
                    saveToLocalPath=f'results/output-{index}-512.jpeg')
            )
        ]
    )

    response = await scaler.transform(options)
    print('response', json.dumps(response.to_dict(), indent=3))

if __name__ == "__main__":
    asyncio.run(main())
