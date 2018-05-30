from aws_monitoring.extensions import ec2_key_pairs as kp

def main():
    keypairs = kp.EC2KeyPairs()
    keypairs.initialize()
    print(keypairs.run())
  
if __name__== "__main__":
    main()
