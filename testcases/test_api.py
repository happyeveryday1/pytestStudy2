import pytest
class TestApi:
    # @pytest.mark.parametrize('args',["hym","冀江涛"])
    # def test_api1(self,args):
    #     print(args)

    # @pytest.mark.parametrize('args', [["hym",29],["冀江涛",30]])
    # def test_api(self, args):
    #     print(args)

    @pytest.mark.parametrize('name,age', [["hym", 29], ["冀江涛", 30]])
    def test_api(self, name,age):
        print(name,age)

if __name__ == '__main__':
    pytest.main(['test_api'])