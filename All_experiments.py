import os
##################
if __name__ == '__main__':
    # <editor-folder desc="1. BA">
    os.system('screen -dmS BA1 python ./run.py -n BA_UNIOA -o UNIOA_BA_syncE_syncG')
    os.system('screen -dmS BA2 python ./run.py -n BA_UNIOA_asyncE_syncG -o UNIOA_BA_asyncE_syncG')
    os.system('screen -dmS BA3 python ./run.py -n BA_SEP -o SEP_BA_asyncE_asyncG')
    os.system('screen -dmS BA4 python ./run.py -n BA_SEP_syncE_syncG -o SEP_BA_syncE_syncG')
    os.system('screen -dmS BA5 python ./run.py -n BA_SEP_fix -o SEP_BA_asyncE_syncG')
    #
    os.system('screen -dmS BA01 python ./run.py -n BA_SEP_fix -o SEP_BA_fix')
    os.system('screen -dmS BA02 python ./run.py -n BA_UNIOA -o UNIOA_BA')
    # </editor-folder>

    # <editor-folder desc="2. GOA">
    os.system('screen -dmS GOA11 python ./run.py -n GOA_UNIOA -o UNIOA_GOA_syncE_syncG -p 1:2')
    os.system('screen -dmS GOA12 python ./run.py -n GOA_UNIOA -o UNIOA_GOA_syncE_syncG -p 3:4')
    os.system('screen -dmS GOA13 python ./run.py -n GOA_UNIOA -o UNIOA_GOA_syncE_syncG -p 5:6')
    os.system('screen -dmS GOA14 python ./run.py -n GOA_UNIOA -o UNIOA_GOA_syncE_syncG -p 7:8')
    os.system('screen -dmS GOA15 python ./run.py -n GOA_UNIOA -o UNIOA_GOA_syncE_syncG -p 9:10')
    os.system('screen -dmS GOA16 python ./run.py -n GOA_UNIOA -o UNIOA_GOA_syncE_syncG -p 11:12')
    os.system('screen -dmS GOA17 python ./run.py -n GOA_UNIOA -o UNIOA_GOA_syncE_syncG -p 13:14')
    os.system('screen -dmS GOA18 python ./run.py -n GOA_UNIOA -o UNIOA_GOA_syncE_syncG -p 15:16')
    os.system('screen -dmS GOA19 python ./run.py -n GOA_UNIOA -o UNIOA_GOA_syncE_syncG -p 17:18')
    os.system('screen -dmS GOA110 python ./run.py -n GOA_UNIOA -o UNIOA_GOA_syncE_syncG -p 19:20')
    os.system('screen -dmS GOA111 python ./run.py -n GOA_UNIOA -o UNIOA_GOA_syncE_syncG -p 21:22')
    os.system('screen -dmS GOA112 python ./run.py -n GOA_UNIOA -o UNIOA_GOA_syncE_syncG -p 23:24')

    os.system('screen -dmS GOA21 python ./run.py -n GOA_UNIOA_asyncE_syncG -o UNIOA_GOA_asyncE_syncG -p 1:2')
    os.system('screen -dmS GOA22 python ./run.py -n GOA_UNIOA_asyncE_syncG -o UNIOA_GOA_asyncE_syncG -p 3:4')
    os.system('screen -dmS GOA23 python ./run.py -n GOA_UNIOA_asyncE_syncG -o UNIOA_GOA_asyncE_syncG -p 5:6')
    os.system('screen -dmS GOA24 python ./run.py -n GOA_UNIOA_asyncE_syncG -o UNIOA_GOA_asyncE_syncG -p 7:8')
    os.system('screen -dmS GOA25 python ./run.py -n GOA_UNIOA_asyncE_syncG -o UNIOA_GOA_asyncE_syncG -p 9:10')
    os.system('screen -dmS GOA26 python ./run.py -n GOA_UNIOA_asyncE_syncG -o UNIOA_GOA_asyncE_syncG -p 11:12')
    os.system('screen -dmS GOA27 python ./run.py -n GOA_UNIOA_asyncE_syncG -o UNIOA_GOA_asyncE_syncG -p 13:14')
    os.system('screen -dmS GOA28 python ./run.py -n GOA_UNIOA_asyncE_syncG -o UNIOA_GOA_asyncE_syncG -p 15:16')
    os.system('screen -dmS GOA29 python ./run.py -n GOA_UNIOA_asyncE_syncG -o UNIOA_GOA_asyncE_syncG -p 17:18')
    os.system('screen -dmS GOA210 python ./run.py -n GOA_UNIOA_asyncE_syncG -o UNIOA_GOA_asyncE_syncG -p 19:20')
    os.system('screen -dmS GOA211 python ./run.py -n GOA_UNIOA_asyncE_syncG -o UNIOA_GOA_asyncE_syncG -p 21:22')
    os.system('screen -dmS GOA212 python ./run.py -n GOA_UNIOA_asyncE_syncG -o UNIOA_GOA_asyncE_syncG -p 23:24')

    os.system('screen -dmS GOA31 python ./run.py -n GOA_SEP -o SEP_GOA_syncE_syncG -p 1:2')
    os.system('screen -dmS GOA32 python ./run.py -n GOA_SEP -o SEP_GOA_syncE_syncG -p 3:4')
    os.system('screen -dmS GOA33 python ./run.py -n GOA_SEP -o SEP_GOA_syncE_syncG -p 5:6')
    os.system('screen -dmS GOA34 python ./run.py -n GOA_SEP -o SEP_GOA_syncE_syncG -p 7:8')
    os.system('screen -dmS GOA35 python ./run.py -n GOA_SEP -o SEP_GOA_syncE_syncG -p 9:10')
    os.system('screen -dmS GOA36 python ./run.py -n GOA_SEP -o SEP_GOA_syncE_syncG -p 11:12')
    os.system('screen -dmS GOA37 python ./run.py -n GOA_SEP -o SEP_GOA_syncE_syncG -p 13:14')
    os.system('screen -dmS GOA38 python ./run.py -n GOA_SEP -o SEP_GOA_syncE_syncG -p 15:16')
    os.system('screen -dmS GOA39 python ./run.py -n GOA_SEP -o SEP_GOA_syncE_syncG -p 17:18')
    os.system('screen -dmS GOA310 python ./run.py -n GOA_SEP -o SEP_GOA_syncE_syncG -p 19:20')
    os.system('screen -dmS GOA311 python ./run.py -n GOA_SEP -o SEP_GOA_syncE_syncG -p 21:22')
    os.system('screen -dmS GOA312 python ./run.py -n GOA_SEP -o SEP_GOA_syncE_syncG -p 23:24')

    os.system('screen -dmS GOA41 python ./run.py -n GOA_SEP_asyncE_syncG -o SEP_GOA_asyncE_syncG -p 1:2')
    os.system('screen -dmS GOA42 python ./run.py -n GOA_SEP_asyncE_syncG -o SEP_GOA_asyncE_syncG -p 3:4')
    os.system('screen -dmS GOA43 python ./run.py -n GOA_SEP_asyncE_syncG -o SEP_GOA_asyncE_syncG -p 5:6')
    os.system('screen -dmS GOA44 python ./run.py -n GOA_SEP_asyncE_syncG -o SEP_GOA_asyncE_syncG -p 7:8')
    os.system('screen -dmS GOA45 python ./run.py -n GOA_SEP_asyncE_syncG -o SEP_GOA_asyncE_syncG -p 9:10')
    os.system('screen -dmS GOA46 python ./run.py -n GOA_SEP_asyncE_syncG -o SEP_GOA_asyncE_syncG -p 11:12')
    os.system('screen -dmS GOA47 python ./run.py -n GOA_SEP_asyncE_syncG -o SEP_GOA_asyncE_syncG -p 13:14')
    os.system('screen -dmS GOA48 python ./run.py -n GOA_SEP_asyncE_syncG -o SEP_GOA_asyncE_syncG -p 15:16')
    os.system('screen -dmS GOA49 python ./run.py -n GOA_SEP_asyncE_syncG -o SEP_GOA_asyncE_syncG -p 17:18')
    os.system('screen -dmS GOA410 python ./run.py -n GOA_SEP_asyncE_syncG -o SEP_GOA_asyncE_syncG -p 19:20')
    os.system('screen -dmS GOA411 python ./run.py -n GOA_SEP_asyncE_syncG -o SEP_GOA_asyncE_syncG -p 21:22')
    os.system('screen -dmS GOA412 python ./run.py -n GOA_SEP_asyncE_syncG -o SEP_GOA_asyncE_syncG -p 23:24')

    os.system('screen -dmS GOA51 python ./run.py -n GOA_SEP_asyncE_asyncG -o SEP_GOA_asyncE_asyncG -p 1:2')
    os.system('screen -dmS GOA52 python ./run.py -n GOA_SEP_asyncE_asyncG -o SEP_GOA_asyncE_asyncG -p 3:4')
    os.system('screen -dmS GOA53 python ./run.py -n GOA_SEP_asyncE_asyncG -o SEP_GOA_asyncE_asyncG -p 5:6')
    os.system('screen -dmS GOA54 python ./run.py -n GOA_SEP_asyncE_asyncG -o SEP_GOA_asyncE_asyncG -p 7:8')
    os.system('screen -dmS GOA55 python ./run.py -n GOA_SEP_asyncE_asyncG -o SEP_GOA_asyncE_asyncG -p 9:10')
    os.system('screen -dmS GOA56 python ./run.py -n GOA_SEP_asyncE_asyncG -o SEP_GOA_asyncE_asyncG -p 11:12')
    os.system('screen -dmS GOA57 python ./run.py -n GOA_SEP_asyncE_asyncG -o SEP_GOA_asyncE_asyncG -p 13:14')
    os.system('screen -dmS GOA58 python ./run.py -n GOA_SEP_asyncE_asyncG -o SEP_GOA_asyncE_asyncG -p 15:16')
    os.system('screen -dmS GOA59 python ./run.py -n GOA_SEP_asyncE_asyncG -o SEP_GOA_asyncE_asyncG -p 17:18')
    os.system('screen -dmS GOA510 python ./run.py -n GOA_SEP_asyncE_asyncG -o SEP_GOA_asyncE_asyncG -p 19:20')
    os.system('screen -dmS GOA511 python ./run.py -n GOA_SEP_asyncE_asyncG -o SEP_GOA_asyncE_asyncG -p 21:22')
    os.system('screen -dmS GOA512 python ./run.py -n GOA_SEP_asyncE_asyncG -o SEP_GOA_asyncE_asyncG -p 23:24')
    #
    os.system('screen -dmS GOA011 python ./run.py -n GOA_SEP -o SEP_GOA -p 1:2')
    os.system('screen -dmS GOA012 python ./run.py -n GOA_SEP -o SEP_GOA -p 3:4')
    os.system('screen -dmS GOA013 python ./run.py -n GOA_SEP -o SEP_GOA -p 5:6')
    os.system('screen -dmS GOA014 python ./run.py -n GOA_SEP -o SEP_GOA -p 7:8')
    os.system('screen -dmS GOA015 python ./run.py -n GOA_SEP -o SEP_GOA -p 9:10')
    os.system('screen -dmS GOA016 python ./run.py -n GOA_SEP -o SEP_GOA -p 11:12')
    os.system('screen -dmS GOA017 python ./run.py -n GOA_SEP -o SEP_GOA -p 13:14')
    os.system('screen -dmS GOA018 python ./run.py -n GOA_SEP -o SEP_GOA -p 15:16')
    os.system('screen -dmS GOA019 python ./run.py -n GOA_SEP -o SEP_GOA -p 17:18')
    os.system('screen -dmS GOA0110 python ./run.py -n GOA_SEP -o SEP_GOA -p 19:20')
    os.system('screen -dmS GOA0111 python ./run.py -n GOA_SEP -o SEP_GOA -p 21:22')
    os.system('screen -dmS GOA0112 python ./run.py -n GOA_SEP -o SEP_GOA -p 23:24')

    os.system('screen -dmS GOA021 python ./run.py -n GOA_UNIOA -o UNIOA_GOA -p 1:2')
    os.system('screen -dmS GOA022 python ./run.py -n GOA_UNIOA -o UNIOA_GOA -p 3:4')
    os.system('screen -dmS GOA023 python ./run.py -n GOA_UNIOA -o UNIOA_GOA -p 5:6')
    os.system('screen -dmS GOA024 python ./run.py -n GOA_UNIOA -o UNIOA_GOA -p 7:8')
    os.system('screen -dmS GOA025 python ./run.py -n GOA_UNIOA -o UNIOA_GOA -p 9:10')
    os.system('screen -dmS GOA026 python ./run.py -n GOA_UNIOA -o UNIOA_GOA -p 11:12')
    os.system('screen -dmS GOA027 python ./run.py -n GOA_UNIOA -o UNIOA_GOA -p 13:14')
    os.system('screen -dmS GOA028 python ./run.py -n GOA_UNIOA -o UNIOA_GOA -p 15:16')
    os.system('screen -dmS GOA029 python ./run.py -n GOA_UNIOA -o UNIOA_GOA -p 17:18')
    os.system('screen -dmS GOA0210 python ./run.py -n GOA_UNIOA -o UNIOA_GOA -p 19:20')
    os.system('screen -dmS GOA0211 python ./run.py -n GOA_UNIOA -o UNIOA_GOA -p 21:22')
    os.system('screen -dmS GOA0212 python ./run.py -n GOA_UNIOA -o UNIOA_GOA -p 23:24')
    # </editor-folder>

    # <editor-folder desc="3. CSA">
    os.system('screen -dmS CSA1 python ./run.py -n CSA_UNIOA -o UNIOA_CSA_syncE')
    os.system('screen -dmS CSA2 python ./run.py -n CSA_UNIOA_asyncE -o UNIOA_CSA_asyncE')
    os.system('screen -dmS CSA3 python ./run.py -n CSA_SEP -o SEP_CSA_syncE')
    os.system('screen -dmS CSA4 python ./run.py -n CSA_SEP_asyncE -o SEP_CSA_asyncE')
    #
    os.system('screen -dmS CSA01 python ./run.py -n CSA_SEP -o SEP_CSA')
    os.system('screen -dmS CSA02 python ./run.py -n CSA_UNIOA -o UNIOA_CSA')
    # </editor-folder>

    # <editor-folder desc="4. MFO">
    os.system('screen -dmS MFO1 python ./run.py -n MFO_UNIOA -o UNIOA_MFO_syncE')
    os.system('screen -dmS MFO2 python ./run.py -n MFO_UNIOA_asyncE -o UNIOA_MFO_asyncE')
    os.system('screen -dmS MFO3 python ./run.py -n MFO_SEP -o SEP_MFO_syncE')
    os.system('screen -dmS MFO4 python ./run.py -n MFO_SEP_asyncE -o SEP_MFO_asyncE')
    #
    os.system('screen -dmS MFO01 python ./run.py -n MFO_SEP -o SEP_MFO')
    os.system('screen -dmS MFO02 python ./run.py -n MFO_UNIOA -o UNIOA_MFO')
    # </editor-folder>

    # <editor-folder desc="5. MBO">
    os.system('screen -dmS MBO11 python ./run.py -n MBO_UNIOA -o UNIOA_MBO_syncE_syncG -p 1:2')
    os.system('screen -dmS MBO12 python ./run.py -n MBO_UNIOA -o UNIOA_MBO_syncE_syncG -p 3:4')
    os.system('screen -dmS MBO13 python ./run.py -n MBO_UNIOA -o UNIOA_MBO_syncE_syncG -p 5:6')
    os.system('screen -dmS MBO14 python ./run.py -n MBO_UNIOA -o UNIOA_MBO_syncE_syncG -p 7:8')
    os.system('screen -dmS MBO15 python ./run.py -n MBO_UNIOA -o UNIOA_MBO_syncE_syncG -p 9:10')
    os.system('screen -dmS MBO16 python ./run.py -n MBO_UNIOA -o UNIOA_MBO_syncE_syncG -p 11:12')
    os.system('screen -dmS MBO17 python ./run.py -n MBO_UNIOA -o UNIOA_MBO_syncE_syncG -p 13:14')
    os.system('screen -dmS MBO18 python ./run.py -n MBO_UNIOA -o UNIOA_MBO_syncE_syncG -p 15:16')
    os.system('screen -dmS MBO19 python ./run.py -n MBO_UNIOA -o UNIOA_MBO_syncE_syncG -p 17:18')
    os.system('screen -dmS MBO110 python ./run.py -n MBO_UNIOA -o UNIOA_MBO_syncE_syncG -p 19:20')
    os.system('screen -dmS MBO111 python ./run.py -n MBO_UNIOA -o UNIOA_MBO_syncE_syncG -p 21:22')
    os.system('screen -dmS MBO112 python ./run.py -n MBO_UNIOA -o UNIOA_MBO_syncE_syncG -p 23:24')

    os.system('screen -dmS MBO21 python ./run.py -n MBO_UNIOA_asyncE_syncG -o UNIOA_MBO_asyncE_syncG -p 1:2')
    os.system('screen -dmS MBO22 python ./run.py -n MBO_UNIOA_asyncE_syncG -o UNIOA_MBO_asyncE_syncG -p 3:4')
    os.system('screen -dmS MBO23 python ./run.py -n MBO_UNIOA_asyncE_syncG -o UNIOA_MBO_asyncE_syncG -p 5:6')
    os.system('screen -dmS MBO24 python ./run.py -n MBO_UNIOA_asyncE_syncG -o UNIOA_MBO_asyncE_syncG -p 7:8')
    os.system('screen -dmS MBO25 python ./run.py -n MBO_UNIOA_asyncE_syncG -o UNIOA_MBO_asyncE_syncG -p 9:10')
    os.system('screen -dmS MBO26 python ./run.py -n MBO_UNIOA_asyncE_syncG -o UNIOA_MBO_asyncE_syncG -p 11:12')
    os.system('screen -dmS MBO27 python ./run.py -n MBO_UNIOA_asyncE_syncG -o UNIOA_MBO_asyncE_syncG -p 13:14')
    os.system('screen -dmS MBO28 python ./run.py -n MBO_UNIOA_asyncE_syncG -o UNIOA_MBO_asyncE_syncG -p 15:16')
    os.system('screen -dmS MBO29 python ./run.py -n MBO_UNIOA_asyncE_syncG -o UNIOA_MBO_asyncE_syncG -p 17:18')
    os.system('screen -dmS MBO210 python ./run.py -n MBO_UNIOA_asyncE_syncG -o UNIOA_MBO_asyncE_syncG -p 19:20')
    os.system('screen -dmS MBO211 python ./run.py -n MBO_UNIOA_asyncE_syncG -o UNIOA_MBO_asyncE_syncG -p 21:22')
    os.system('screen -dmS MBO212 python ./run.py -n MBO_UNIOA_asyncE_syncG -o UNIOA_MBO_asyncE_syncG -p 23:24')

    os.system('screen -dmS MBO31 python ./run.py -n MBO_SEP -o SEP_MBO_syncE_syncG -p 1:2')
    os.system('screen -dmS MBO32 python ./run.py -n MBO_SEP -o SEP_MBO_syncE_syncG -p 3:4')
    os.system('screen -dmS MBO33 python ./run.py -n MBO_SEP -o SEP_MBO_syncE_syncG -p 5:6')
    os.system('screen -dmS MBO34 python ./run.py -n MBO_SEP -o SEP_MBO_syncE_syncG -p 7:8')
    os.system('screen -dmS MBO35 python ./run.py -n MBO_SEP -o SEP_MBO_syncE_syncG -p 9:10')
    os.system('screen -dmS MBO36 python ./run.py -n MBO_SEP -o SEP_MBO_syncE_syncG -p 11:12')
    os.system('screen -dmS MBO37 python ./run.py -n MBO_SEP -o SEP_MBO_syncE_syncG -p 13:14')
    os.system('screen -dmS MBO38 python ./run.py -n MBO_SEP -o SEP_MBO_syncE_syncG -p 15:16')
    os.system('screen -dmS MBO39 python ./run.py -n MBO_SEP -o SEP_MBO_syncE_syncG -p 17:18')
    os.system('screen -dmS MBO310 python ./run.py -n MBO_SEP -o SEP_MBO_syncE_syncG -p 19:20')
    os.system('screen -dmS MBO311 python ./run.py -n MBO_SEP -o SEP_MBO_syncE_syncG -p 21:22')
    os.system('screen -dmS MBO312 python ./run.py -n MBO_SEP -o SEP_MBO_syncE_syncG -p 23:24')

    os.system('screen -dmS MBO41 python ./run.py -n MBO_SEP_asyncE_syncG -o SEP_MBO_asyncE_syncG -p 1:2')
    os.system('screen -dmS MBO42 python ./run.py -n MBO_SEP_asyncE_syncG -o SEP_MBO_asyncE_syncG -p 3:4')
    os.system('screen -dmS MBO43 python ./run.py -n MBO_SEP_asyncE_syncG -o SEP_MBO_asyncE_syncG -p 5:6')
    os.system('screen -dmS MBO44 python ./run.py -n MBO_SEP_asyncE_syncG -o SEP_MBO_asyncE_syncG -p 7:8')
    os.system('screen -dmS MBO45 python ./run.py -n MBO_SEP_asyncE_syncG -o SEP_MBO_asyncE_syncG -p 9:10')
    os.system('screen -dmS MBO46 python ./run.py -n MBO_SEP_asyncE_syncG -o SEP_MBO_asyncE_syncG -p 11:12')
    os.system('screen -dmS MBO47 python ./run.py -n MBO_SEP_asyncE_syncG -o SEP_MBO_asyncE_syncG -p 13:14')
    os.system('screen -dmS MBO48 python ./run.py -n MBO_SEP_asyncE_syncG -o SEP_MBO_asyncE_syncG -p 15:16')
    os.system('screen -dmS MBO49 python ./run.py -n MBO_SEP_asyncE_syncG -o SEP_MBO_asyncE_syncG -p 17:18')
    os.system('screen -dmS MBO410 python ./run.py -n MBO_SEP_asyncE_syncG -o SEP_MBO_asyncE_syncG -p 19:20')
    os.system('screen -dmS MBO411 python ./run.py -n MBO_SEP_asyncE_syncG -o SEP_MBO_asyncE_syncG -p 21:22')
    os.system('screen -dmS MBO412 python ./run.py -n MBO_SEP_asyncE_syncG -o SEP_MBO_asyncE_syncG -p 23:24')

    os.system('screen -dmS MBO51 python ./run.py -n MBO_SEP_asyncE_asyncG -o SEP_MBO_asyncE_asyncG -p 1:2')
    os.system('screen -dmS MBO52 python ./run.py -n MBO_SEP_asyncE_asyncG -o SEP_MBO_asyncE_asyncG -p 3:4')
    os.system('screen -dmS MBO53 python ./run.py -n MBO_SEP_asyncE_asyncG -o SEP_MBO_asyncE_asyncG -p 5:6')
    os.system('screen -dmS MBO54 python ./run.py -n MBO_SEP_asyncE_asyncG -o SEP_MBO_asyncE_asyncG -p 7:8')
    os.system('screen -dmS MBO55 python ./run.py -n MBO_SEP_asyncE_asyncG -o SEP_MBO_asyncE_asyncG -p 9:10')
    os.system('screen -dmS MBO56 python ./run.py -n MBO_SEP_asyncE_asyncG -o SEP_MBO_asyncE_asyncG -p 11:12')
    os.system('screen -dmS MBO57 python ./run.py -n MBO_SEP_asyncE_asyncG -o SEP_MBO_asyncE_asyncG -p 13:14')
    os.system('screen -dmS MBO58 python ./run.py -n MBO_SEP_asyncE_asyncG -o SEP_MBO_asyncE_asyncG -p 15:16')
    os.system('screen -dmS MBO59 python ./run.py -n MBO_SEP_asyncE_asyncG -o SEP_MBO_asyncE_asyncG -p 17:18')
    os.system('screen -dmS MBO510 python ./run.py -n MBO_SEP_asyncE_asyncG -o SEP_MBO_asyncE_asyncG -p 19:20')
    os.system('screen -dmS MBO511 python ./run.py -n MBO_SEP_asyncE_asyncG -o SEP_MBO_asyncE_asyncG -p 21:22')
    os.system('screen -dmS MBO512 python ./run.py -n MBO_SEP_asyncE_asyncG -o SEP_MBO_asyncE_asyncG -p 23:24')

    #
    os.system('screen -dmS MBO011 python ./run.py -n MBO_SEP -o SEP_MBO -p 1:2')
    os.system('screen -dmS MBO012 python ./run.py -n MBO_SEP -o SEP_MBO -p 3:4')
    os.system('screen -dmS MBO013 python ./run.py -n MBO_SEP -o SEP_MBO -p 5:6')
    os.system('screen -dmS MBO014 python ./run.py -n MBO_SEP -o SEP_MBO -p 7:8')
    os.system('screen -dmS MBO015 python ./run.py -n MBO_SEP -o SEP_MBO -p 9:10')
    os.system('screen -dmS MBO016 python ./run.py -n MBO_SEP -o SEP_MBO -p 11:12')
    os.system('screen -dmS MBO017 python ./run.py -n MBO_SEP -o SEP_MBO -p 13:14')
    os.system('screen -dmS MBO018 python ./run.py -n MBO_SEP -o SEP_MBO -p 15:16')
    os.system('screen -dmS MBO019 python ./run.py -n MBO_SEP -o SEP_MBO -p 17:18')
    os.system('screen -dmS MBO0110 python ./run.py -n MBO_SEP -o SEP_MBO -p 19:20')
    os.system('screen -dmS MBO0111 python ./run.py -n MBO_SEP -o SEP_MBO -p 21:22')
    os.system('screen -dmS MBO0112 python ./run.py -n MBO_SEP -o SEP_MBO -p 23:24')

    os.system('screen -dmS MBO021 python ./run.py -n MBO_UNIOA -o UNIOA_BA -p 1:2')
    os.system('screen -dmS MBO022 python ./run.py -n MBO_UNIOA -o UNIOA_BA -p 3:4')
    os.system('screen -dmS MBO023 python ./run.py -n MBO_UNIOA -o UNIOA_BA -p 5:6')
    os.system('screen -dmS MBO024 python ./run.py -n MBO_UNIOA -o UNIOA_BA -p 7:8')
    os.system('screen -dmS MBO025 python ./run.py -n MBO_UNIOA -o UNIOA_BA -p 9:10')
    os.system('screen -dmS MBO026 python ./run.py -n MBO_UNIOA -o UNIOA_BA -p 11:12')
    os.system('screen -dmS MBO027 python ./run.py -n MBO_UNIOA -o UNIOA_BA -p 13:14')
    os.system('screen -dmS MBO028 python ./run.py -n MBO_UNIOA -o UNIOA_BA -p 15:16')
    os.system('screen -dmS MBO029 python ./run.py -n MBO_UNIOA -o UNIOA_BA -p 17:18')
    os.system('screen -dmS MBO0210 python ./run.py -n MBO_UNIOA -o UNIOA_BA -p 19:20')
    os.system('screen -dmS MBO0211 python ./run.py -n MBO_UNIOA -o UNIOA_BA -p 21:22')
    os.system('screen -dmS MBO0212 python ./run.py -n MBO_UNIOA -o UNIOA_BA -p 23:24')
    # </editor-folder>

    # <editor-folder desc="6. BOA">
    os.system('screen -dmS BOA1 python ./run.py -n BOA_UNIOA -o UNIOA_BOA_syncE_syncG')
    os.system('screen -dmS BOA2 python ./run.py -n BOA_UNIOA_asyncE_syncG -o UNIOA_BOA_asyncE_syncG')
    os.system('screen -dmS BOA3 python ./run.py -n BOA_SEP -o SEP_BOA_asyncE_asyncG')
    os.system('screen -dmS BOA4 python ./run.py -n BOA_SEP_syncE_syncG -o SEP_BOA_syncE_syncG')
    os.system('screen -dmS BOA5 python ./run.py -n BOA_SEP_fix -o SEP_BOA_asyncE_syncG')
    #
    os.system('screen -dmS BOA01 python ./run.py -n BOA_SEP_fix -o SEP_BOA_fix')
    os.system('screen -dmS BOA02 python ./run.py -n BOA_UNIOA -o UNIOA_BOA')
    # </editor-folder>

    # <editor-folder desc="7. PSO">
    os.system('screen -dmS PSO1 python ./run.py -n PSO_UNIOA -o UNIOA_PSO_syncE_syncG')
    os.system('screen -dmS PSO2 python ./run.py -n PSO_UNIOA_asyncE_syncG -o UNIOA_PSO_asyncE_syncG')
    os.system('screen -dmS PSO3 python ./run.py -n PSO_SEP -o SEP_PSO_asyncE_asyncG')
    os.system('screen -dmS PSO4 python ./run.py -n PSO_SEP_syncE_syncG -o SEP_PSO_syncE_syncG')
    os.system('screen -dmS PSO5 python ./run.py -n PSO_SEP_fix -o SEP_PSO_asyncE_syncG')
    #
    os.system('screen -dmS PSO01 python ./run.py -n PSO_SEP_fix -o SEP_PSO_fix')
    os.system('screen -dmS PSO02 python ./run.py -n PSO_UNIOA -o UNIOA_PSO')
    # </editor-folder>










