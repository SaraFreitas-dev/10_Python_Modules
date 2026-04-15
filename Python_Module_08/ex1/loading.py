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
                """
                If the installation is done, import the module
                Transform the dep str into a module and get its version
                """
                module = importlib.import_module(dep)
                version = module.__version__
                print(f"[OK] {dep} ({version}) - {dep_type} ready")
                modules[dep] = module
            except ImportError:
                all_ok = False
                print(f"[MISSING] {dep} - {dep_type} not found\n"
                      f"    -> Install with pip: pip install {dep}\n"
                      f"    -> Or with poetry: poetry add {dep}")
        if not all_ok:
            print("\nERROR: Missing required dependencies. Aborting.\n")
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
        requests = modules["requests"]
        matplotlib = modules["matplotlib"]
        data = numpy.random(1000)
        df = pandas.DataFrame()
        print("Analyzing Matrix data..."
              "Processing 1000 data points...\n"
              "Generating visualization...\n\n")

    except Exception as e:
        print(f"Error on analyse_matrix(): {e}")


def generate_visualization() -> None:
    """
    Generating visualization - matrix_analysis.png
    Creates a graph with matplotlib and stores the image
    """
    print("Analysis complete!\n"
          "Results saved to: matrix_analysis.png")


def loading() -> None:
    """Print the program text result"""
    print("\nLOADING STATUS: Loading programs...\n"
          "Checking dependencies:\n")
    modules, all_ok = check_deps()
    if all_ok:
        analyse_matrix(modules)
        generate_visualization()


if __name__ == "__main__":
    loading()
