#!/bin/bash

# Clone the fn CLI repository
git clone https://github.com/fnproject/cli.git
cd cli

# Install Go (if not already installed)
sudo dnf -y install go

# Set up Go environment variables
export GOPATH=$HOME/go
export PATH=$GOPATH/bin:$PATH

# Build the fn CLI for aarch64
GOARCH=arm64 go build -o fn

# Move fn binary to /usr/local/bin if build successful
if [ -f fn ]; then
    sudo mv fn /usr/local/bin/fn
    echo "fn binary moved to /usr/local/bin/fn"
else
    echo "Failed to build fn binary. Exiting."
    exit 1
fi

# Verify the compiled fn CLI binary
file /usr/local/bin/fn

# Run the fn CLI version command
/usr/local/bin/fn --version

# Delete the cli folder
cd ..
rm -rf cli