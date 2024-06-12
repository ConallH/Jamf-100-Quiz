Basic script to install Kivy on a Unix-like system (Linux, macOS) using pip:

```bash
#!/bin/bash

# Install dependencies
sudo apt-get update
sudo apt-get install -y python3-pip python3-dev build-essential libgl1-mesa-dev git

# Install Kivy
pip3 install kivy
```

Save this script to a file, for example, install_kivy.sh, and make it executable:

```bash
chmod +x install_kivy.sh
```

Then, you can run the script:

```bash
./install_kivy.sh
```

This script will update the package list, install necessary dependencies, and then install Kivy using pip. Adjustments might be needed depending on your system and package manager (e.g., apt-get for Debian-based systems). For macOS, you might need to use Homebrew or another package manager instead. 