const SERVER_ADDRESS: string = "http://localhost:8080";

export type Package = {
  ipAddress: string;
  latitude: number;
  longitude: number;
  timestamp: Date;
  isSuspicious: boolean;
};

export async function getPackages(): Promise<Package[]> {
  type PackageIn = {
    ip_address: string;
    latitude: number;
    longitude: number;
    timestamp: number;
    is_suspicious: boolean;
  };

  const parsedPackages: Package[] = await fetch(`${SERVER_ADDRESS}/packages/`)
    .then((response) => response.json() as Promise<PackageIn[]>)
    .then((packages_raw) =>
      packages_raw.map((it) => ({
        ipAddress: it.ip_address,
        latitude: it.latitude,
        longitude: it.longitude,
        timestamp: new Date(1000 * it.timestamp),
        isSuspicious: it.is_suspicious,
      })),
    );

  return parsedPackages;
}
