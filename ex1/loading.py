import importlib
import sys


def poetry_pip_detect() -> None:
    if "pypoetry" in sys.prefix:
        print("Dependency Manager: Poetry")
        print("Environment: Isolated (Poetry virtualenv)")
        print("Dependencies: Managed via pyproject.toml")
    else:
        print("Dependency Manager: pip / system")
        print("Environment: Global or virtualenv")
        print("Dependencies: Managed via requirements.txt")

def check_module(module: str, message: str) -> bool:
    try:
        module_name = importlib.import_module(module)
        print(f"[OK] {module_name.__name__} "
              f"({getattr(module_name, '__version__', 'unknown')}) "
              f"- {message}")
        return True
    except ImportError:
        print(f"[ERROR] {module} not installed")
        return False


if __name__ == "__main__":
    poetry_pip_detect()
    print("\nLOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")
    checking_all: list[bool] = [
        check_module("pandas", "Data manipulation ready"),
        check_module("numpy", "Numerical computation ready"),
        check_module("requests", "Network access ready"),
        check_module("matplotlib", "Visualization ready")
    ]

    if all(checking_all):
        print("\nAnalyzing Matrix data...")
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt

        data = np.random.rand(1000)
        data_frame = pd.DataFrame(data, columns=["Values"])
        print(f"Processing {len(data)} data points...")
        print("Generating visualization...")
        try:
            plt.plot(data_frame["Values"])
            plt.title("Matrix Data Analysis")
            plt.xlabel("Time")
            plt.ylabel("Values")
            plt.savefig("matrix_analysis.png", dpi=300, bbox_inches="tight")
            plt.close()
        except Exception as e:
            print("Error on analysis")
        print("\nAnalysis complete!")
        print("Results saved to: matrix_analysis.png")
