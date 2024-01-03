from ping3 import ping
import ipaddress


def ping_ip_address(ipv4_address:str ) -> str:
    #TODO: I should add a logger here that would capture the pings that fail
    ping_response = ping(ipv4_address, timeout=1)
    if ping_response is not None and ping_response != False:
        return ipv4_address
    # else:
    #     return f'IP Address {ipv4_address} not found.'

def network_to_ip_address(network:str) -> list:
    #TODO: I should add a couple checks here that would make sure they enter in a correct network.
    host_ip_addresses = []
    host_list = list(ipaddress.IPv4Network(network).hosts())
    for host_ip in host_list:
        host_ip_addresses.append(str(host_ip))
    return host_ip_addresses


def main():
    temp_list = network_to_ip_address("192.168.2.0/26")
    pingable_ip_addresses = []
    for ip_address in temp_list:
        ping_result = ping_ip_address(ip_address)
        print(ping_result)
        if ping_result is not None:
            pingable_ip_addresses.append(ip_address)
    
    print(pingable_ip_addresses)
    
if __name__ == "__main__":
    main()
    