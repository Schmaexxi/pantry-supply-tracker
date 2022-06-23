import uvicorn  # type: ignore
from fastapi import FastAPI
from pantry_supply_tracker.config import app_config
from pantry_supply_tracker.utils import logger

log = logger.setup_logger(__name__)

app = FastAPI(debug=True)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=app_config.host,
        port=app_config.server_port,
        reload=True,
    )
