import logging
from pathlib import Path
from logging.handlers import TimedRotatingFileHandler
from typing import Optional


def setup_logger(
    name: str,
    level: int = logging.INFO,
    interval_type: str = "midnight",
    interval: int = 1,
    backup_count: int = 14,
    filename: Optional[str] = None,
) -> logging.Logger:
    """setup a streaming and file-based rotating logger
    Args:
        name: name of the logger (also used as filename)
        level: loglevel
        interval_type: type of interval. Possible values: 'S', 'M', 'H', 'D',
        'W0'-'W6', 'midnight'
        interval: number of occurrences until handler uses new file
        backup_count: number of files to keep at one time
        filename: base name of the log file
    Returns:
        created logger
    """

    if filename is None:
        (Path().cwd() / "logs").mkdir(exist_ok=True)
        filename = f"logs/{name}.log"
    logging.basicConfig(
        level=level,
        handlers=[
            logging.StreamHandler(),
            TimedRotatingFileHandler(
                filename,
                when=interval_type,
                interval=interval,
                backupCount=backup_count,
            ),
        ],
        format="%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    return logging.getLogger(name)
