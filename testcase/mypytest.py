

import re
def test_demo1():
    assert 100 == 100
    
def test_demo2():
    assert 100 == 99
    
def test_demo3():
    assert 77 == 77
    
def test_demo4():
    assert 88 == 99

def test_re():
    str=""""filter_checkbox" onChange="filterTable(this)" type="checkbox"/><span class="passed">2 passed</span>, <input checked="true" class="filter" data-test-result="skipped" """
    regular = re.findall(r'span class="passed">(\d*?) passed<', str)
    print(regular)
    
test_re()