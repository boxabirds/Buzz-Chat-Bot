# Copyright (C) 2010 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import simple_buzz_wrapper
import unittest

class SimpleBuzzWrapperTest(unittest.TestCase):
  def test_wrapper_rejects_empty_message(self):
    wrapper = simple_buzz_wrapper.SimpleBuzzWrapper()
    self.assertEquals(None, wrapper.post('sender@example.org', ''))

  def test_wrapper_rejects_messsage_containing_only_whitespace(self):
    wrapper = simple_buzz_wrapper.SimpleBuzzWrapper()
    self.assertEquals(None, wrapper.post('sender@example.org', '            '))

  def test_wrapper_rejects_none_message(self):
    wrapper = simple_buzz_wrapper.SimpleBuzzWrapper()
    self.assertEquals(None, wrapper.post('sender@example.org', None))