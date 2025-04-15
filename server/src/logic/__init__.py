import datetime as dt
from ipaddress import IPv4Address
from typing import TypedDict

PackageIn = TypedDict(
    "PackageIn",
    {
        "ip address": str,
        "Latitude": str,
        "Longitude": str,
        "Timestamp": str,
        "suspicious": str,
    },
)


class PackageOut(TypedDict):
    ip_address: str
    latitude: float
    longitude: float
    timestamp: float
    is_suspicious: bool


packages: list[PackageOut] = []


def parse_package(data: PackageIn, /) -> PackageOut:
    suspicious_parsed = float(data["suspicious"])

    if abs(suspicious_parsed - 0.0) < 1e-9:
        is_suspicious = False
    elif abs(suspicious_parsed - 1.0) < 1e-9:
        is_suspicious = True
    else:
        raise ValueError("`suspicious` should only be `0.0` or `1.0`")

    return {
        "ip_address": IPv4Address(data["ip address"]).compressed,
        "latitude": float(data["Latitude"]),
        "longitude": float(data["Longitude"]),
        "timestamp": dt.datetime.fromtimestamp(float(data["Timestamp"])).timestamp(),
        "is_suspicious": is_suspicious,
    }


def add_package_raw(data: PackageIn, /) -> None:
    global packages

    packages.append(parse_package(data))


def get_packages() -> list[PackageOut]:
    global packages

    return packages
