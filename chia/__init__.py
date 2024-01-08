from __future__ import annotations

import importlib.metadata

__version__: str
try:
    __version__ = importlib.metadata.version("chia-blockchain")
    __version__ += "-sweet"
except importlib.metadata.PackageNotFoundError:
    # package is not installed
    __version__ = "unknown"
