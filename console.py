#!/usr/bin/python3
"""class"""
import cmd


class HBNBCommand(cmd.Cmd):
	"""class"""
	prompt = "(hbnb)"
	def emptyline(self):
        pass
	def do_quit(self, line):
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        return True

    def help_EOF(self):
        print("Quit command to exit the program\n")
 



if __name__ == '__main__':
    HBNBCommand().cmdloop()