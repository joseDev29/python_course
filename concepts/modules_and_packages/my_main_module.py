from my_module import hello, my_add
# from my_module import *

from my_package import my_package_module_1, my_package_module_2
# from my_package.my_package_module_1 import package_hello
# from my_package.my_package_module_2 import package_bye
# from my_package.my_package_module_1 import *
# from my_package.my_package_module_2 import *

from my_package.my_subpackage import my_subpackage_module_1
# from my_package.my_subpackage.my_subpackage_module_1 import subpackage_hello
# from my_package.my_subpackage.my_subpackage_module_1 import *

hello()
my_add(23, 45)
my_package_module_1.package_hello()
my_package_module_2.package_bye()
my_subpackage_module_1.subpackage_hello()
