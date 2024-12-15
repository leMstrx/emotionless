import json
from solana.keypair import Keypair
from pathlib import Path

def load_keypair(keyfile_path: str = "local_keys/secret.json") -> Keypair:
    keypath = Path(keyfile_path)
    if not keypath.exists():
        raise RuntimeError(f"Keyfile not found: {keypath}")

    with keypath.open("r") as keyfile:
        secret = json.load(keyfile)

    #The secret should be a list of 64 integers
    secret_bytes = bytes(secret)
    return Keypair.from_secret_key(secret_bytes)
    