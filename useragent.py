# Author Alienrazor
#Tool purpose / user_agent for scraping
#Educational purpose 
import os
import time
os.system('pip install -U user_agent')
os.system('pip install user-agent')

logo = '''\033[1;91m
                 ..              .:.
              ~YJ^.              .~J5!.
            ^G@J                   .J@B!
         ?~ B@Y                      5@&:7?
        ^@5:#@J                      Y@@!P@^
        ~@@#&@&7        ....:~      ?@@@#@@^
       7:J@@@@@7     :75####B7      ?@@@@@J^7
       !#55#@@@~:    :!~P@@@!      :~@@@#55#!
        ~P&@@@@5J?^.    !@@@Y   .^JJ5@@@@&P^
         .7YPB&@BB##BPYY#@@@@YPB##GB@&BPY7.
          ?B##&@@@@@@@@@@@@@@@@@@@@@@@##G7
           :?G&@&G#@@@@@@@@@@@@@&#B&@#P7.
              :~?7~~?#@&@@@@&@B?^!?7^.
                 !!YP5~~&@@&~~PPJ!!
                .^7J^  5@@@@Y .^J7^
                      J@&&&&@?
                     !#&G##B&#!
                     G5&5##P&PG
                     Y7&Y##5#7Y
                     ..GJ##5P..
                       J?#&Y?
                       ~7#&J^
                       .~#&!.
                        .#&:
                        .B&:
                         G#.
                         GB
                         5P
                         7J
                         .   
                         '
                                                            
\033[1;91m_________________________________________________\n
\033[0;96m [\033[0;96m✯\033[1;96m] \033[0;96mFB GROUP : Alienrazor
\033[0;96m [\033[0;96m✯\033[0;96m] \033[0;96mGITHUB   : Alienrazor
\033[0;96m [\033[0;96m✯\033[0;96m] \033[0;96mTOOL     : USER_AGENT
\033[1;91m_________________________________________________\033[1;96m
    '''
    
def main():
    os.system("clear")
    print(logo)
    print ('       \033[32m     Fresh Useragent \033[1;96m')
    print ('')
    print (' [1] fast useragents ')
    print (' [2] Exit ')
    print ('\033[1;91m_________________________________________________\033[33m')
    ag = input(" [√] CHOOSE : ")
    if ag in ["1","01"]:
        hun()
    elif ag in ["2","02"]:
       exit()
    else:
        print('\033[1;31mINCORECT OPTION!\033[1;31m')
        main()
 


def hun():
    os.system("clear")
    print(logo)
    print('      \033[32m          NOTE')
    print('\033[96m Agents Saved In /sdcard/USER-AGENT.txt')
    print(' To Stop Process CTRL + Z\033[32m')
    print ('\033[1;91m_________________________________________________\033[32m')
    print('')
    time.sleep(20)
    os.system('python test.py')
        
main()
#Script End