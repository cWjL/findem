#!/usr/bin/python3
import whois
import sys
import argparse

def main():
    '''
    Do main stuff
    
    Check this out:  https://stackoverflow.com/a/2575779/4678883  Reverse DNS lookup using socket library
    '''
    parser = argparse.ArgumentParser()
    reqd = parser.add_argument_group('required arguments')
    reqd.add_argument('-t','--target',action='store',dest='tar',help='Keyword to find')
    
    args = parser.parse_args()
    effect = effects()
    
    sys.exit(0)
    
class effects(object):
    '''
    Terminal color object
    '''
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    g_prefix = "["+GREEN+"*"+ENDC+"] "
    b_prefix = "["+RED+"*"+ENDC+"] "
    w_prefix = "["+YELLOW+"*"+ENDC+"] "
    bl_prefix = "["+BLUE+"*"+ENDC+"] "
    
    def warn_msg(self, in_str):
        '''
        Warning message
        @param String in_str
        @return String yellow
        '''
        return self.YELLOW+in_str+self.ENDC
    
    def err_msg(self, in_str):
        '''
        Error message
        @param String in_str
        @return String red
        '''
        return self.RED+in_str+self.ENDC
    
    def good_msg(self, in_str):
        '''
        Good message
        @param String in_str
        @return String green
        '''
        return self.GREEN+in_str+self.ENDC

    def blue_msg(self, in_str):
        '''
        Normal message
        @param String in_str
        @return String blue
        '''
        return self.BLUE+in_str+self.ENDC
        
if __name__ == "__main__":
    main()