# Run as script or module by using functions

def main():
    print('When only this script is executed.')
    module1()

def module1():
    print('As a module...')

if __name__ == '__main__':
    main()
