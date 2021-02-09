#! /usr/bin/env python
# -*- encoding: utf-8 -*-
# Desc: Demo
# Date: 2021-01-30


from unittest import TestCase
from app.demo.app import aa, bb


class DemoTest(TestCase):

    def test_aa(self):
        self.assertEqual(aa(), 1)

    def test_bb(self):
        self.assertEqual(bb(), "bb")
