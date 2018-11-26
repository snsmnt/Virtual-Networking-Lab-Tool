# Virtual-Networking-Lab-Tool

Tool to deploy and configure quagga router topology in a Linux box.

Execution:
1. If the customized ubuntu image is not built in the host before, build it by running the playbook, create_quagga_image.yml (skip if "initialscript.bash" is executed) 
   sudo ansible-playbook -i inventory create_quagga_image.yml
2. Modify the network adjacency matrix (./scripts/connectivitymat.txt) according to the required topology.
3. Run the connectivity_script.yml playbook to create the topology or run script "rnd_lab.bash" to run the playbook
   sudo ansible-playbook -i inventory connectivity_script.yml
4. Management IP addresses of the containers are assigned in the range 172.17.0.2 -172.17.0.254, sequencially and by the order in which they are placed in the network connectivity matrix. 
5. To access a container: do ssh to the management IP with username: root password: root
6. Once inside a router, to enter in the router CLI, type vtysh and hit enter.
7. You can check the topology created by reading "connectivity_map.txt" which gives topology design and IP addresses assigned to the topology.
