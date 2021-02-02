import pytest
import yaml

from page.app import App
from test_case.test_base import TestBase


class Test_Main(TestBase):
    @pytest.mark.parametrize("value1,value2",yaml.safe_load(open("../test_case/test_mian.yaml")))
    def test_main(self,value1,value2):
        self.app.start().main().goto_search().search("长沙")

