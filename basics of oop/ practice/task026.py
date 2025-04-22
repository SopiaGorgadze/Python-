# duck typing


class Hammer:
    def turnon(self):
        print("hammer is ready")

    def use(self):
        print("hammering the nail...")

class Screwdriver:
    def turnon(self):
        print("schrewdriver is ready")

    def use(self):
        print("rotating the screw")

hammer = Hammer()
schrewdriver = Screwdriver()


def use_tool(tool):
    tool.turnon()
    tool.use()
    

use_tool(hammer)
use_tool(schrewdriver)
