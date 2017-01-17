Filter plugins for ansible
--------------------------

Output a specific ansible hash indented by the hash name

Example:-

hashname:
    test: test
    test2: test2

        {{ hashname | root_to_nice_yaml( root='hashname' ) }}


