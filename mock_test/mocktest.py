# -*- coding: utf-8 -*-

#!/usr/bin/env python

import os, sys, time

# sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import unittest

from unittest import TestCase

import mock

import module


class Foo(object):

	pass


class TestMock(TestCase):

	# 1

	def test_method(self):

		obj = Foo()

		obj.method = mock.MagicMock(return_value=3)

		print(obj.method)

		self.assertEqual(obj.method(4), 3)

	# 2

	@mock.patch('module.foo')

	def test_decorator(self, foo):

		# res = module.foo()

		foo.return_value = [1, 2, 3]

		self.assertEqual(foo(), [1, 2, 3])

	# 3

	def test_with(self):

		with mock.patch('module.give_me_five') as give_me_five:

			give_me_five.return_value = "I'm Mock"

			self.assertEqual(module.foo(), "I'm Mock")

	# 4

	def test_module(self):

		module.give_me_five = mock.Mock(return_value=[1] * 5)

		module.give_me_five([1]) # 此时已经变成了一个Mock对象, 并尝试调用

		module.give_me_five.assert_called_with([1]) # 对mock的参数进行断言

		self.assertEqual(module.foo(), [1] * 5)
		

if __name__ == '__main__':

	unittest.main()