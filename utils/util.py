from typing import List
import os


def find_module_in_package(packagePath: str, rootDir: str) -> List[str]:
    pPath = packagePath.replace(".", os.sep)
    modlist: List[str] = []
    solutePath = os.path.join(rootDir, pPath)
    for f in os.listdir(solutePath):
        if f.find("__") >= 0:
            continue
        pPath2 = os.path.join(solutePath, f)
        if os.path.isdir(pPath2):
            modlist.extend(find_module_in_package(f"{packagePath}.{f}", rootDir))
        if f.rfind(".py") >= 0:
            f = f.replace(".py", "")
            modlist.append(f"{packagePath}.{f}")
    return modlist


if __name__ == "__main__":
    packagePath = "tests.demo"
    rootDir = os.path.join(os.path.dirname(__file__), "../")
    print(find_module_in_package(packagePath, rootDir))
