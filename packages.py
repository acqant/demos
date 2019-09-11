'''
Packages are a way of structuring Python’s module namespace by using “dotted module names”.
For example, the module name A.B designates a submodule named B in a package named A.
Just like the use of modules saves the authors of different modules from having
to worry about each other’s global variable names, the use of dotted module names
 saves the authors of multi-module packages like NumPy or Pillow from having to
  worry about each other’s module names.
'''
import my_package.my_sub_package.sub_package_echo
my_package.my_sub_package.sub_package_echo.echo_example('Long import hello message')

# ew, that's ugly
from my_package.my_sub_package import sub_package_echo
sub_package_echo.echo_example('Same message but shorter, hello message')
