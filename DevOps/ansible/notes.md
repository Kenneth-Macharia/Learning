# Using anible playbooks

- Ensure the ansible virtual environment is acitvated
- Run a playbook _on host node_: `ansible-playbook <playbook_file.yml>`
- Run a playbook _on remote nodes_: `ansible-playbook <playbook_file> -i <dynamic_inventory_file> -u <node_user>`
