echo "Starting Installation........"

# Install the required packages
sudo apt-get install -y python3-pip

# Install the required python packages
sudo pip3 install -r requirements.txt

# Manually Install tk
sudo apt-get install -y python3-tk

# Successfully Installed
echo "Successfully Installed"

# Run the application
python3 main.py