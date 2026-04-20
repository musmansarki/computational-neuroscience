#!/usr/bin/env python3
"""
Environment Verification Script for WBAI077-05
Run this to verify your Python environment is correctly set up.
"""

import sys

def test_imports():
    """Test that all required packages can be imported."""
    print("Testing package imports...")
    print("-" * 60)
    
    packages = {
        'numpy': 'np',
        'scipy.signal': 'signal',
        'pandas': 'pd',
        'matplotlib.pyplot': 'plt',
        'seaborn': 'sns',
        'mne': 'mne',
        'sklearn': 'sklearn',
        'statsmodels.api': 'sm',
    }
    
    all_good = True
    
    for package, alias in packages.items():
        try:
            if '.' in package:
                # Handle submodules
                parts = package.split('.')
                exec(f"import {parts[0]}")
                module = sys.modules[parts[0]]
                for part in parts[1:]:
                    module = getattr(module, part)
                print(f"✓ {package:30s} imported successfully")
            else:
                exec(f"import {package} as {alias}")
                version = eval(f"{alias}.__version__")
                print(f"✓ {package:30s} v{version}")
        except ImportError as e:
            print(f"✗ {package:30s} FAILED: {e}")
            all_good = False
        except AttributeError:
            print(f"✓ {package:30s} imported successfully")
    
    print("-" * 60)
    return all_good


def test_basic_functionality():
    """Test basic functionality with a simple signal processing example."""
    print("\nTesting basic functionality...")
    print("-" * 60)
    
    try:
        import numpy as np
        import matplotlib.pyplot as plt
        
        # Generate test signal
        t = np.linspace(0, 1, 1000)
        signal = np.sin(2 * np.pi * 10 * t) + 0.5 * np.random.randn(1000)
        
        # Create a simple plot
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(t[:200], signal[:200])
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Amplitude")
        ax.set_title("Test Signal - If you see this, your setup works!")
        ax.grid(True, alpha=0.3)
        
        # Save the plot
        plt.savefig('/home/claude/cmn-practical/test_plot.png', dpi=100, bbox_inches='tight')
        plt.close()
        
        print("✓ Generated test signal")
        print("✓ Created and saved test plot to test_plot.png")
        print("-" * 60)
        return True
        
    except Exception as e:
        print(f"✗ Basic functionality test failed: {e}")
        print("-" * 60)
        return False


def main():
    print("=" * 60)
    print("WBAI077-05 Environment Verification")
    print("=" * 60)
    print(f"Python version: {sys.version}")
    print(f"Python executable: {sys.executable}")
    print("=" * 60)
    
    imports_ok = test_imports()
    functionality_ok = test_basic_functionality()
    
    print("\n" + "=" * 60)
    if imports_ok and functionality_ok:
        print("✓✓✓ ALL TESTS PASSED ✓✓✓")
        print("Your environment is ready for the course!")
    else:
        print("✗✗✗ SOME TESTS FAILED ✗✗✗")
        print("Please check the errors above and reinstall failed packages.")
    print("=" * 60)
    
    return 0 if (imports_ok and functionality_ok) else 1


if __name__ == "__main__":
    sys.exit(main())
