import sys
from scaler_pics import Scaler, TransformOptions, InputOptions, OutputOptions, Fit, ImageDelivery
import asyncio

apiKey = sys.argv[1] if len(sys.argv) > 1 else 'YOUR_API_KEY'
scaler = Scaler(apiKey)


async def main():
    options = TransformOptions(
        input=InputOptions(localPath='images/test.heic'),
        output=OutputOptions(
            type='jpeg',
            fit=Fit(width=1024, height=1024),
            imageDelivery=ImageDelivery(saveToLocalPath='results/test.jpg'),
            quality=0.8
        )
    )
    response = await scaler.transform(options)
    print('response', response.to_dict())


if __name__ == "__main__":
    asyncio.run(main())
