import json
from pathlib import Path
from solders.keypair import Keypair # type: ignore

def load_keypair(keyfile_path: str = "local_keys/secret.json") -> Keypair:
    keypath = Path(keyfile_path)
    if not keypath.exists():
        raise RuntimeError(f"Keyfile not found: {keypath}")

    with keypath.open("r") as keyfile:
        secret = json.load(keyfile)

    # The secret is typically a 64-byte array (64 integers).
    # Convert it to bytes and use Keypair.from_bytes().
    secret_bytes = bytes(secret)
    return Keypair.from_bytes(secret_bytes)
