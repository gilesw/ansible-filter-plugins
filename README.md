Filter plugins for ansible
==========================




root_to_nice_yaml
-----------------


Output a specific ansible hash indented by the hash name

Example:-


    wibble:
        test: test
    hashname:
        test: test
        test2: test2

        {{ hashname | root_to_nice_yaml( root='hashname' ) }}

will print out:-

    hashname:
        test: test
        test2: test2


!! Currently failing on ansible 2.2.1.0

Appears to be caused by objects in the hash

https://github.com/ansible/ansible/issues/20253
