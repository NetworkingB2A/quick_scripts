from ping3 import ping
import concurrent.futures
import ipaddress

def network_to_ip_address(network:str) -> list:
    #TODO: I should add a couple checks here that would make sure they enter in a correct network.
    host_list = list(ipaddress.IPv4Network(network).hosts())
    host_ip_addresses = [str(host_ip) for host_ip in host_list]
    return host_ip_addresses

def ping_ip_address(ipv4_address:str, timeout=1 ) -> dict:
    #TODO: I should add a logger here that would capture the pings that fail
    ping_response = ping(ipv4_address, timeout=timeout)
    if ping_response is not None and ping_response != False:
        print(f'IP address {ipv4_address} was able to ping')
        ping_results = {'ip_address':ipv4_address, 'ping_successful':True}
    else:
        print(f'IP address {ipv4_address} was not able to ping')
        ping_results = {'ip_address':ipv4_address, 'ping_successful':False}
    return ping_results


def ping_ip_address_multithreaded(ipv4_addresses:list ) -> list:
    if isinstance(ipv4_addresses, list):
        pass
    else:
        raise ValueError("Please pass in a list of ip address to ping")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(ping_ip_address, ipv4_addresses))
    return results
    
    

def main():
    temp_list = network_to_ip_address("192.168.2.0/24")
    # Here is an example of using the ping_ip_address function  
    # ip_address = '192.168.2.1'
    # ping_result = ping_ip_address(ip_address)
    # print(ping_result)

    
    pinging_ips = ping_ip_address_multithreaded(temp_list)
    print(pinging_ips)

    
if __name__ == "__main__":
    main()
    