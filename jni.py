import os
import sys
import readchar

'''
Author: Surya Rajendhran
Usage: python3 jni.py Sample.java
If you want further instructions: https://gist.github.com/DmitrySoshnikov/8b1599a5197b5469c8cc07025f600fdb
In case you get a fatal error while compiling C program,
set environmental variable using this command:
export JAVA_HOME="$(/usr/libexec/java_home -v 1.8)"
'''

def execute(statement, optional=None):
	print('System command:', statement)
	if not optional is None:
		print(optional)
	os.system(statement)
def print_info(info):
	print('Info: ', info)

program_name = sys.argv[1].split('.')[0]
print("Program name: ", program_name)
lower_program_name = program_name.lower() 
statement1 = 'javac {}.java'.format(program_name) #Compile java program
statement2 = 'javah -jni ' + program_name #Generate header
statement3 = 'gcc -I"$JAVA_HOME/include" -I"$JAVA_HOME/include/darwin/" -o lib{0}.jnilib -shared {1}.c'.format(lower_program_name, program_name)
statement4 = 'java -Djava.library.path=. '+program_name

print_info("Compiling Java program...")
execute(statement1)
execute(statement2)
print_info("Complete C program({}.c) and press any key to continue...".format(program_name))
_ = readchar.readchar()
print_info("Compiling C program and creating JNI Library...")
execute(statement3)
print_info("Executing Java Program...")
execute(statement4, "Output:")