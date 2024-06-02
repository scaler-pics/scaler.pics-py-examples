import os
from scaler_pics import Scaler, TransformOptions, InputOptions, OutputOptions, Fit, ImageDelivery
import asyncio

# Initialize the Scaler instance with the API key from environment variables
scaler = Scaler(
    os.getenv('API_KEY', ''))


async def test():
    options = TransformOptions(
        input=InputOptions(localPath='test-data/test.heic'),
        output=OutputOptions(
            type='jpeg',
            fit=Fit(width=1024, height=1024),
            imageDelivery=ImageDelivery(saveToLocalPath='test-data/test.jpg'),
            quality=0.8
        )
    )
    response = await scaler.transform(options)
    print('response', response.to_dict())


if __name__ == "__main__":
    asyncio.run(test())
