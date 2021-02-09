#!/usr/bin/env python
# --coding=utf-8--
import click
import importlib


@click.command()
@click.option("--package", prompt="Your package", help="Package in application")
@click.option("--module", prompt="Your module", help="module in Package")
@click.option("--method", prompt="Your method", help="method in Module")
def run(package: str, module: str, method: str) -> None:
    """根据命令行所给的参数，运行对应模块方法"""
    modulePath: str = "app"
    if package and module:
        modulePath += f".{package}.{module}"
    runModule = importlib.import_module(modulePath)
    if method in dir(runModule):
        getattr(runModule, method)()
    else:
        print(f"{method} is not in {runModule}")


def main():
    run()


main()
