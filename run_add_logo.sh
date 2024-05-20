if ! command -v brew &> /dev/null
then
    echo "Homebrew not found. Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "Homebrew is already installed."
fi

if ! command -v python3 &> /dev/null
then
    echo "Python3 not found. Installing Python3..."
    brew install python
else
    echo "Python3 is already installed."
fi

if ! command -v pip3 &> /dev/null
then
    echo "pip3 not found. Installing pip3..."
    python3 -m ensurepip --upgrade
else
    echo "pip3 is already installed."
fi

echo "Installing required Python packages..."
pip3 install pillow

echo "Running the add_logo.py script..."
python3 add_logo.py "$@"

