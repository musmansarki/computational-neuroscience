#!/bin/bash
# WBAI077-05 Environment Setup Script
# Run this script to automatically set up your Python environment

set -e  # Exit on any error

echo "=================================="
echo "WBAI077-05 Environment Setup"
echo "Computational Methods in Neuroscience"
echo "=================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed!"
    echo "Please install Python 3.10 or higher first."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "✓ Found Python $PYTHON_VERSION"

# Check Python version
MAJOR=$(echo $PYTHON_VERSION | cut -d'.' -f1)
MINOR=$(echo $PYTHON_VERSION | cut -d'.' -f2)

if [ "$MAJOR" -lt 3 ] || ([ "$MAJOR" -eq 3 ] && [ "$MINOR" -lt 10 ]); then
    echo "⚠️  Warning: Python $PYTHON_VERSION detected"
    echo "   Recommended: Python 3.10 or 3.11"
    echo "   Continue anyway? (y/n)"
    read -r response
    if [[ ! "$response" =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

echo ""
echo "Creating virtual environment..."
python3 -m venv cmn-env

echo "✓ Virtual environment created"
echo ""

# Activate environment
echo "Activating environment..."
source cmn-env/bin/activate

echo "✓ Environment activated"
echo ""

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip > /dev/null 2>&1
echo "✓ Pip upgraded"
echo ""

# Install core packages
echo "Installing core packages..."
echo "(This may take a few minutes)"
pip install numpy scipy pandas matplotlib seaborn jupyterlab > /dev/null 2>&1
echo "✓ Core packages installed"
echo ""

# Install neuroscience packages
echo "Installing neuroscience-specific packages..."
pip install mne scikit-learn statsmodels nibabel nilearn > /dev/null 2>&1
echo "✓ Neuroscience packages installed"
echo ""

# Export requirements
pip freeze > requirements.txt
echo "✓ Requirements exported to requirements.txt"
echo ""

# Run verification
echo "Running verification tests..."
python verify_setup.py

echo ""
echo "=================================="
echo "✅ SETUP COMPLETE!"
echo "=================================="
echo ""
echo "Your environment is ready. To start working:"
echo ""
echo "1. Activate the environment:"
echo "   source cmn-env/bin/activate"
echo ""
echo "2. Start Jupyter Lab:"
echo "   jupyter lab"
echo ""
echo "Or open this folder in VS Code and select the cmn-env interpreter."
echo ""
echo "See QUICK_START.md for daily workflow reference."
echo "=================================="
