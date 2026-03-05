#!/bin/bash

# CrypTrus2.0 Manual Installation Script for Termux
# Use this if automated setup fails

echo "CrypTrus2.0 - Manual Installation"
echo "=================================="
echo ""

# Step 1: Update packages
echo "[1/5] Updating package manager..."
apt update
apt upgrade -y

# Step 2: Install system dependencies
echo "[2/5] Installing system dependencies..."
apt install -y \
    python3 \
    python3-pip \
    curl \
    wget \
    git \
    inetutils \
    net-tools \
    openssh \
    nano \
    grep \
    sed

# Step 3: Install Python packages
echo "[3/5] Installing Python packages..."
pip install --upgrade pip
pip install pyyaml netaddr

# Step 4: Create directories
echo "[4/5] Creating necessary directories..."
mkdir -p output
mkdir -p configs
mkdir -p logs
mkdir -p results

# Step 5: Set permissions
echo "[5/5] Setting permissions..."
chmod +x cryptrus2.0.py
chmod +x termux/launcher.sh
chmod +x setup.sh

echo ""
echo "✅ Installation Complete!"
echo ""
echo "Next steps:"
echo "1. cd to CrypTrus2.0 directory"
echo "2. Run: python3 cryptrus2.0.py --help"
echo "3. Start scanning: python3 cryptrus2.0.py -t 192.168.1.0/24 --all"