# Minimal Roboto SDK Docker Image

## Build Docker Image
```bash
docker build -t ubuntu-roboto-sdk:latest .
```

## Run the Container
```bash
docker run --rm -e ROBOTO_API_KEY=YOUR_PRIVATE_API_KEY ubuntu-roboto-sdk:latest
```

## Usage
Replace `YOUR_PRIVATE_API_KEY` with your actual Roboto API key when running the container. You can find it under "token" in your `~/.roboto/config.json` file. 

For more information, check our [Getting Started documentation](https://docs.roboto.ai/getting-started/programmatic-access.html).
