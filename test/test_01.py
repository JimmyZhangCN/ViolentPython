import pytest
import sys
sys.path.append("..")
from SectionOne import unzip


def test_01():
   assert  unzip.extractFile("../SectionOne/evil.zip", "123") == None

