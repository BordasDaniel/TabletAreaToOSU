#with open(file='./presets.json', encoding='utf-8', opener=int, mode='+',):
#    pass


class Area:
    def __init__(self, bottom, top, left, right, width=0, height=0, tablet_width=0, tablet_height=0, x=0, y=0):
        self.bottom = bottom
        self.top = top
        self.left = left
        self.right = right
        self.width = width
        self.height = height
        self.tablet_width = tablet_width
        self.tablet_height = tablet_height
        self.x = x
        self.y = y


    def wacom_veikk(self):
        self.width = (self.right - self.left) / 100
        self.height = (self.bottom - self.top) / 100
        self.x = (self.left / 100) + (self.width / 2)
        self.y = (self.top / 100) + (self.height / 2)

    def xp_pen(self):
        self.width = self.width / 3.937
        self.height = self.height / 3.937
        self.x = (self.width / 2) + (self.x / 3.937)
        self.y = (self.height / 2) + (self.y / 3.937)

    def huion_gaomon(self):
        self.width = (self.right - self.left) * self.tablet_width
        self.height = (self.bottom - self.top) * self.tablet_height
        self.x = (self.width / 2) + (self.left * self.tablet_width)
        self.y = (self.height / 2) + (self.top * self.tablet_height)

    def output(self):
        return f'Your x offset is: {self.x}\nYour y offset is: {self.y}\nYour width is: {self.width}\nYour height is: {self.height}'

    @staticmethod
    def copyright(version = 1.0):
        return f'Sources from: https://opentabletdriver.net/Wiki/FAQ/General\nVersion: {version} by Dániel Bordás'
    
    @staticmethod
    def welcome():
        return f'\t\tWelcome to my area converter program!\nHere are the supported device brands: Wacom, VEIKK, XP-Pen, Huion, Gaomon'

    @staticmethod
    def linebreak():
        return f'-------------------------------------------------------------------------------'

    @staticmethod
    def huion_gaomon_warning():
        return f"Note: Huion and Gaomon areas use a percentage area, which uses a percentage of the tablet's maximum area to calculate the area.\nYou must know your tablet's digitizer dimensions in millimeters in order to properly convert these areas.\nHuion website: https://store.huion.com/eu/\nGaomon website: https://www.gaomon.net/"


def my():
    bottom = 7550
    top = 2421
    left = 4300
    right = 10534
    return Area(bottom, top, left, right)


def user_xp_wacom_veikk():
    bottom = int(input('Please, give me your current bottom:\t'))
    top = int(input('Please, give me your current top:\t'))
    left = int(input('Please, give me your current left:\t'))
    right = int(input('Please, give me your current right:\t'))
    return Area(bottom, top, left, right)


def user_huion_gaomon():
    bottom = int(input('Please, give me your current bottom:\t'))
    top = int(input('Please, give me your current top:\t'))
    left = int(input('Please, give me your current left:\t'))
    right = int(input('Please, give me your current right:\t'))
    tablet_width = int(input('Please, give me your current tablet width:\t'))
    tablet_height = int(input('Please, give me your current tablet height:\t'))
    return Area(bottom, top, left, right, tablet_width, tablet_height)


def selection():
    choice = input(f"To begin the convert please, select one brand by writing it's starting letter!\nYou can also recall your saved one by writing „My”\nIf you want to stop the request press an enter!\nYour choice:\t")
    return choice


def pick(choice):
    try:
        if choice == 'W' or choice == 'w':
            print('You chose: Wacom/VEIKK')
            to_convert = user_xp_wacom_veikk()
            to_convert.wacom_veikk()
            print(to_convert.output())

        elif choice == 'x' or choice == 'X':
            print('You chose: XP-PEN')
            to_convert = user_xp_wacom_veikk()
            to_convert.xp_pen()
            print(to_convert.output())

        elif choice == 'h' or choice == 'H' or choice =='G' or choice == 'g':
            print('You chose: Huion/Gaomon')
            to_convert = user_huion_gaomon()
            to_convert.huion_gaomon()

        elif choice == 'my' or choice == 'MY':
            to_convert = my()
            to_convert.wacom_veikk()
            print(to_convert.output())

        elif choice == '':
            print('Its me')

        else:
            print(f"Error, „{choice}” function not found. Please try again.")
    except:
        print(f'Error, {choice} function not found. Please try again.')


def main():
    print(Area.welcome())
    print(Area.copyright())
    print(Area.linebreak())
    print(Area.huion_gaomon_warning())
    print(Area.linebreak())
    while not (choice := selection()) == '':
        pick(choice)
    else:
        print('See you next time!')

main()
