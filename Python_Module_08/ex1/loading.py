import importlib
from typing import Any


def check_deps() -> tuple[dict[str, Any], bool]:
    """
    Check for the presence of each dependency (pandas, numpy, etc)
    If there is any missing dependency, it show instructions on how to add them
    """
    try:
        dependencies = [('pandas', 'Data manipulation'),
                        ('numpy', 'Numerical computation'),
                        ('requests', 'Network access'),
                        ('matplotlib', 'Visualization')]
        modules = {}
        all_ok = True
        for dep, dep_type in dependencies:
            try:
                # If the installation is done, import the module
                # Transform the dep str into a module and get its version

                module = importlib.import_module(dep)
                version = module.__version__
                print(f"[OK] {dep} ({version}) - {dep_type} ready")
                modules[dep] = module

            except Exception:
                if dep == "requests":
                    print(f"[OPTIONAL] {dep} not found")
                    continue
                all_ok = False
                print(f"[MISSING] {dep} - {dep_type} not found\n"
                      f"    -> Install with pip: pip install {dep}\n"
                      f"    -> Or with poetry: poetry add {dep}")
        if not all_ok:
            print("\nInstall all dependencies with the pip command: "
                  "pip install -r requirements.txt\n"
                  "Or with the poetry command: "
                  "poetry install -> poetry run python loading.py\n"
                  "\nERROR: Missing required dependencies. Aborting.\n")
            return ({}, all_ok)
        return (modules, all_ok)
    except Exception as e:
        print(f"Error on check_deps(): {e}")
        return ({}, False)


def analyse_matrix(modules: dict[str, Any]) -> None:
    """
    Generate data with numpy
    Create the dataframe with pandas
    """
    try:
        pandas = modules["pandas"]
        numpy = modules["numpy"]
        # Generate random signal values
        signal = numpy.random.rand(1000)
        # Create a counter
        time = numpy.arange(1000)
        # Create a table using pandas
        data_f = pandas.DataFrame({"time": time, "signal": signal})

        print("\nAnalyzing Matrix data...\n"
              "Processing 1000 data points...\n"
              "Generating visualization...\n\n")
        # Generate the png image
        generate_visualization(data_f)

    except Exception as e:
        print(f"Error on analyse_matrix(): {e}")


def generate_visualization(data_f: Any) -> None:
    """
    Generating visualization - matrix_analysis.png
    Creates a graph with pandas DataFrame and stores the image
    """
    try:
        import matplotlib.pyplot as plt

        file_name = "matrix_analysis.png"
        plt.figure(figsize=(10, 5))
        plt.plot(data_f["time"], data_f["signal"])
        plt.title("Matrix Signal Analysis")
        plt.xlabel("Time")
        plt.ylabel("Signal")
        plt.grid(True)
        plt.savefig(file_name)
        plt.close()
        print("Analysis complete!\n"
              f"Results saved to: {file_name}")
    except Exception as e:
        print(f"Error on generate_visualization(): {e}")


def loading() -> None:
    """
    Print the program text result.
    """
    print("\nLOADING STATUS: Loading programs...\n"
          "Checking dependencies:\n")
    modules, all_ok = check_deps()
    if all_ok:
        analyse_matrix(modules)


if __name__ == "__main__":
    loading()
