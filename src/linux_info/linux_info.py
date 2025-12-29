import paramiko, csv


# the script will access a host via ssh and retrieve useful information. 

# Flags can be used to specify the level of detail. Where information is not available, a specific exit code is returned. 

def linux_info():

    host = '100.121.243.99'
    user = 'judah'
    

    client = paramiko.SSHClient()

    # so no environment variables are ever required, downside is that this is not portable
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        host, 
        username=user, 
        port='2222',)
    
    stdin_, stdout_, stderr_ = client.exec_command('''                                        
                                                   hostname
                                                   ifconfig -a
                                                   systemctl list-units --all
                                                   ps aux
                                                   free -h''')
    stdout_.channel.recv_exit_status()
    lines = stdout_.readlines()
    
    for line in lines:
        print(line)
        with open ('/tmp/output.csv', 'a') as output:
            output.write(line)


    client.close()

# still to do:

# logging 
# error handling
# properly parsing received data
# properly displaying received data