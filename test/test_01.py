import pytest
import sys
import os
sys.path.append(os.getcwd())
from SectionOne import unzip


def test_01():
   assert  unzip.extractFile("../SectionOne/evil.zip", "123") == None

