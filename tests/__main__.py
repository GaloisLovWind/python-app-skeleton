#! /usr/bin/env python
# -*- encoding: utf-8 -*-
# Desc: 单元测试模块
# Date: 2021-01-30
import os
from unittest import TestSuite, TestLoader, TextTestRunner
import click
import importlib
from utils.util import find_module_in_package


@click.command()
@click.option("--package", prompt="Your Test Package", help="package name")
@click.option("--module", help="module name")
@click.option("--clsname", help="class name")
def main(package: str, module: str, clsname: str) -> None:
    suite: TestSuite = TestSuite()
    modulePath: str = "tests"
    loader: TestLoader = TestLoader()
    if clsname and module and package:
        modulePath += f".{package}.{module}.{clsname}"
        suite.addTests(TestLoader().loadTestsFromName(modulePath))
    elif module and package:
        modulePath += f".{package}.{module}"
        suite.addTests(loader.loadTestsFromModule(importlib.import_module(modulePath)))
    else:
        if package:
            modulePath += f".{package}"
        rootDir = os.path.join(os.path.dirname(__file__), "../")
        moduleList = find_module_in_package(modulePath, rootDir)
        for mod in moduleList:
            suite.addTests(loader.loadTestsFromModule(importlib.import_module(mod)))
    runner: TextTestRunner = TextTestRunner(verbosity=2)
    runner.run(suite)


main()
