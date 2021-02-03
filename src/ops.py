from pathlib import Path

import yaml

ROOT_DIR = Path(__file__).parents[1]


def load_secrets(path: Path = ROOT_DIR / "secret.yml"):
    with open(path.as_posix(), "r") as f:
        secrets = yaml.safe_load(f)

    return secrets
