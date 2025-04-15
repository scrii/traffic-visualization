import csv
import time
from typing import Never

import requests

SERVER_URL: str = "http://localhost:8080"


def read_packages() -> list[dict[str, str]]:
    with open("ip_addresses.csv") as csv_file:
        packages = list(csv.DictReader(csv_file))

    packages.sort(key=lambda it: int(it["Timestamp"]))

    return packages


def wait_until_ready() -> None | Never:
    while True:
        try:
            if not requests.get(f"{SERVER_URL}/health/").ok:
                time.sleep(1.0)
            else:
                break
        except Exception:
            time.sleep(1.0)


def main() -> None:
    wait_until_ready()

    for package in read_packages():
        requests.post(f"{SERVER_URL}/package/", json=package)


if __name__ == "__main__":
    main()
