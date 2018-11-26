#!/usr/bin/python

with open('./scripts/connectivitymat.txt') as f:
  node_list = f.readline().strip().split()

node_num = len(node_list)

open('./scripts/vars_file.yaml', 'w').close() #Clear Previous data
file =open('./scripts/vars_file.yaml','a')
file.write("container_names:\n")
for node_name in node_list:
  file.write("  - "+node_name+"\n")

