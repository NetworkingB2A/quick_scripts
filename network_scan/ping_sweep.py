from ping3 import ping
import concurrent.futures
import ipaddress


def network_to_ip_address(network: str) -> list:
    """
    Converts a given network address to a list of individual IP addresses.

    Args:
        network (str): The network address in CIDR format (e.g., "192.168.2.0/24").

    Returns:
        list: A list of individual IP addresses within the specified network.
    """
    # TODO: Add checks to ensure the correct format of the network is provided.
    host_list = list(ipaddress.IPv4Network(network).hosts())
    host_ip_addresses = [str(host_ip) for host_ip in host_list]
    return host_ip_addresses


def ping_ip_address(ipv4_address: str, timeout: float=1) -> dict:
    """
    Pings a given IPv4 address and returns the ping result.

    Args:
        ipv4_address (str): The IPv4 address to ping.
        timeout (float): Timeout value for the ping operation in seconds (default is 1).

    Returns:
        dict: A dictionary containing the IP address and the result of the ping operation.
    """
    # TODO: Add a logger to capture failed ping attempts.
    ping_response = ping(ipv4_address, timeout=timeout)
    if ping_response is not None and ping_response != False:
        print(f"IP address {ipv4_address} was able to ping")
        ping_results = {"ip_address": ipv4_address, "ping_successful": True}
    else:
        print(f"IP address {ipv4_address} was not able to ping")
        ping_results = {"ip_address": ipv4_address, "ping_successful": False}
    return ping_results


def ping_ip_address_multithreaded(ipv4_addresses: list) -> list:
    """
    Performs multithreaded ping operations on a list of IPv4 addresses.

    Args:
        ipv4_addresses (list): A list of IPv4 addresses to ping.

    Returns:
        list: A list of dictionaries containing the IP addresses and their ping results.
    """
    if isinstance(ipv4_addresses, list):
        pass
    else:
        raise ValueError("Please pass in a list of IP addresses to ping")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(ping_ip_address, ipv4_addresses))
    return results


def main():
    # Example of using network_to_ip_address function
    temp_list = network_to_ip_address("192.168.2.0/24")

    # Example of using the ping_ip_address function
    # ip_address = '192.168.2.1'
    # ping_result = ping_ip_address(ip_address)
    # print(ping_result)

    # Example of using ping_ip_address_multithreaded function
    pinging_ips = ping_ip_address_multithreaded(temp_list)
    print(pinging_ips)


if __name__ == "__main__":
    main()
