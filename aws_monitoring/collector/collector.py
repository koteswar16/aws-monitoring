from aws_monitoring.extensions import ec2_key_pairs as kp
from aws_monitoring.extensions import ec2_addresses as addr

def main():
    """keypairs = kp.EC2KeyPairs()
    keypairs.initialize()
    print(keypairs.run())"""
    
    ip_addr = addr.EC2Addresses()
    ip_addr.initialize()
    print(ip_addr.run())
  
if __name__== "__main__":
    main()
