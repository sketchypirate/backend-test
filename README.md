### SETUP PROCEDURE, ONLY NEEDS TO BE RUN ONCE

# 1. Upgrade pip
python3 -m pip install --upgrade pip

# 2. Install virtual environment
pip3 install virtualenv

# 3. Create a virtual environment. Make sure you are in the right directory.
virtualenv -p python3 virtual

# 4. Start the virtual environment. Now your terminal should have a "(virtual)" prefix, indicating that you are running virtually.
source virtual/bin/activate

# Since this is the first time you activated your virtual environment, you now have to install all the project's requirements.
# Install the requirement files.
pip3 install -r requirements.txt

# MAKE SURE you deactivate the virtual environment when you are done by running
deactivate

### ACTIVATION PROCEDURE, you run this to start the virtual environment. 
source virtual/bin/activate

# Run server on port 8080.
./run.bin