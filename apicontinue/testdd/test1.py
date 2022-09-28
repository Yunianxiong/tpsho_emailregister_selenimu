#coding=utf-8

import os
import sys


def test_os():
    gcw_path=os.getcwd()
    file=os.path.dirname(__file__)
    dir_gcw=os.path.dirname(os.getcwd())
    abs_dir=os.path.abspath(os.path.dirname(__file__))
    abs_gcw=os.path.abspath(os.getcwd())
    abs_dir_gcw=os.path.abspath(os.path.dirname(os.getcwd()))
    print(f'gcw_path-->{gcw_path}')
    print(f'file-->{file}')
    print(f'dir_gcw-->{dir_gcw}')
    print(f'abs_dir-->{abs_dir}')
    print(f'abs_gcw-->{abs_gcw}')
    print(f'abs_dir_gcw-->{abs_dir_gcw}')


if __name__=='__main__':
    test_os()


