import subprocess
##################
if __name__ == '__main__':
    # <editor-folder desc="1. BA">
    subprocess.call(['screen -dmS BA1 python ./run.py -n BA_UNIOA               -o UNIOA_BA_syncE_syncG'], shell=True)
    subprocess.call(['screen -dmS BA2 python ./run.py -n BA_UNIOA_asyncE_syncG  -o UNIOA_BA_asyncE_syncG'], shell=True)
    subprocess.call(['screen -dmS BA3 python ./run.py -n BA_orig                -o orig_BA_asyncE_asyncG'], shell=True)
    subprocess.call(['screen -dmS BA4 python ./run.py -n BA_orig_syncE_syncG    -o orig_BA_syncE_syncG'], shell=True)
    subprocess.call(['screen -dmS BA5 python ./run.py -n BA_orig_fix            -o orig_BA_asyncE_syncG'], shell=True)
    #
    subprocess.call(['screen -dmS BA01 python ./run.py -n BA_orig_fix           -o orig_BA_fix'], shell=True)
    subprocess.call(['screen -dmS BA02 python ./run.py -n BA_UNIOA              -o UNIOA_BA'], shell=True)
    # </editor-folder>

    # <editor-folder desc="2. GOA">
    subprocess.call(['screen -dmS GOA11 python ./run.py -n GOA_UNIOA -o UNIOA_GOA_syncE_syncG -p 1:2'], shell=True)
    subprocess.call(['screen -dmS GOA12 python ./run.py -n GOA_UNIOA -o UNIOA_GOA_syncE_syncG -p 3:4'], shell=True)
    subprocess.call(['screen -dmS GOA13 python ./run.py -n GOA_UNIOA -o UNIOA_GOA_syncE_syncG -p 5:6'], shell=True)
    subprocess.call(['screen -dmS GOA14 python ./run.py -n GOA_UNIOA -o UNIOA_GOA_syncE_syncG -p 7:8'], shell=True)
    subprocess.call(['screen -dmS GOA15 python ./run.py -n GOA_UNIOA -o UNIOA_GOA_syncE_syncG -p 9:10'], shell=True)
    subprocess.call(['screen -dmS GOA16 python ./run.py -n GOA_UNIOA -o UNIOA_GOA_syncE_syncG -p 11:12'], shell=True)
    subprocess.call(['screen -dmS GOA17 python ./run.py -n GOA_UNIOA -o UNIOA_GOA_syncE_syncG -p 13:14'], shell=True)
    subprocess.call(['screen -dmS GOA18 python ./run.py -n GOA_UNIOA -o UNIOA_GOA_syncE_syncG -p 15:16'], shell=True)
    subprocess.call(['screen -dmS GOA19 python ./run.py -n GOA_UNIOA -o UNIOA_GOA_syncE_syncG -p 17:18'], shell=True)
    subprocess.call(['screen -dmS GOA110 python ./run.py -n GOA_UNIOA -o UNIOA_GOA_syncE_syncG -p 19:20'], shell=True)
    subprocess.call(['screen -dmS GOA111 python ./run.py -n GOA_UNIOA -o UNIOA_GOA_syncE_syncG -p 21:22'], shell=True)
    subprocess.call(['screen -dmS GOA112 python ./run.py -n GOA_UNIOA -o UNIOA_GOA_syncE_syncG -p 23:24'], shell=True)

    subprocess.call(['screen -dmS GOA21 python ./run.py -n GOA_UNIOA_asyncE_syncG -o UNIOA_GOA_asyncE_syncG -p 1:2'], shell=True)
    subprocess.call(['screen -dmS GOA22 python ./run.py -n GOA_UNIOA_asyncE_syncG -o UNIOA_GOA_asyncE_syncG -p 3:4'], shell=True)
    subprocess.call(['screen -dmS GOA23 python ./run.py -n GOA_UNIOA_asyncE_syncG -o UNIOA_GOA_asyncE_syncG -p 5:6'], shell=True)
    subprocess.call(['screen -dmS GOA24 python ./run.py -n GOA_UNIOA_asyncE_syncG -o UNIOA_GOA_asyncE_syncG -p 7:8'], shell=True)
    subprocess.call(['screen -dmS GOA25 python ./run.py -n GOA_UNIOA_asyncE_syncG -o UNIOA_GOA_asyncE_syncG -p 9:10'], shell=True)
    subprocess.call(['screen -dmS GOA26 python ./run.py -n GOA_UNIOA_asyncE_syncG -o UNIOA_GOA_asyncE_syncG -p 11:12'], shell=True)
    subprocess.call(['screen -dmS GOA27 python ./run.py -n GOA_UNIOA_asyncE_syncG -o UNIOA_GOA_asyncE_syncG -p 13:14'], shell=True)
    subprocess.call(['screen -dmS GOA28 python ./run.py -n GOA_UNIOA_asyncE_syncG -o UNIOA_GOA_asyncE_syncG -p 15:16'], shell=True)
    subprocess.call(['screen -dmS GOA29 python ./run.py -n GOA_UNIOA_asyncE_syncG -o UNIOA_GOA_asyncE_syncG -p 17:18'], shell=True)
    subprocess.call(['screen -dmS GOA210 python ./run.py -n GOA_UNIOA_asyncE_syncG -o UNIOA_GOA_asyncE_syncG -p 19:20'], shell=True)
    subprocess.call(['screen -dmS GOA211 python ./run.py -n GOA_UNIOA_asyncE_syncG -o UNIOA_GOA_asyncE_syncG -p 21:22'], shell=True)
    subprocess.call(['screen -dmS GOA212 python ./run.py -n GOA_UNIOA_asyncE_syncG -o UNIOA_GOA_asyncE_syncG -p 23:24'], shell=True)

    subprocess.call(['screen -dmS GOA31 python ./run.py -n GOA_orig -o orig_GOA_syncE_syncG -p 1:2'], shell=True)
    subprocess.call(['screen -dmS GOA32 python ./run.py -n GOA_orig -o orig_GOA_syncE_syncG -p 3:4'], shell=True)
    subprocess.call(['screen -dmS GOA33 python ./run.py -n GOA_orig -o orig_GOA_syncE_syncG -p 5:6'], shell=True)
    subprocess.call(['screen -dmS GOA34 python ./run.py -n GOA_orig -o orig_GOA_syncE_syncG -p 7:8'], shell=True)
    subprocess.call(['screen -dmS GOA35 python ./run.py -n GOA_orig -o orig_GOA_syncE_syncG -p 9:10'], shell=True)
    subprocess.call(['screen -dmS GOA36 python ./run.py -n GOA_orig -o orig_GOA_syncE_syncG -p 11:12'], shell=True)
    subprocess.call(['screen -dmS GOA37 python ./run.py -n GOA_orig -o orig_GOA_syncE_syncG -p 13:14'], shell=True)
    subprocess.call(['screen -dmS GOA38 python ./run.py -n GOA_orig -o orig_GOA_syncE_syncG -p 15:16'], shell=True)
    subprocess.call(['screen -dmS GOA39 python ./run.py -n GOA_orig -o orig_GOA_syncE_syncG -p 17:18'], shell=True)
    subprocess.call(['screen -dmS GOA310 python ./run.py -n GOA_orig -o orig_GOA_syncE_syncG -p 19:20'], shell=True)
    subprocess.call(['screen -dmS GOA311 python ./run.py -n GOA_orig -o orig_GOA_syncE_syncG -p 21:22'], shell=True)
    subprocess.call(['screen -dmS GOA312 python ./run.py -n GOA_orig -o orig_GOA_syncE_syncG -p 23:24'], shell=True)

    subprocess.call(['screen -dmS GOA41 python ./run.py -n GOA_orig_asyncE_syncG -o orig_GOA_asyncE_syncG -p 1:2'], shell=True)
    subprocess.call(['screen -dmS GOA42 python ./run.py -n GOA_orig_asyncE_syncG -o orig_GOA_asyncE_syncG -p 3:4'], shell=True)
    subprocess.call(['screen -dmS GOA43 python ./run.py -n GOA_orig_asyncE_syncG -o orig_GOA_asyncE_syncG -p 5:6'], shell=True)
    subprocess.call(['screen -dmS GOA44 python ./run.py -n GOA_orig_asyncE_syncG -o orig_GOA_asyncE_syncG -p 7:8'], shell=True)
    subprocess.call(['screen -dmS GOA45 python ./run.py -n GOA_orig_asyncE_syncG -o orig_GOA_asyncE_syncG -p 9:10'], shell=True)
    subprocess.call(['screen -dmS GOA46 python ./run.py -n GOA_orig_asyncE_syncG -o orig_GOA_asyncE_syncG -p 11:12'], shell=True)
    subprocess.call(['screen -dmS GOA47 python ./run.py -n GOA_orig_asyncE_syncG -o orig_GOA_asyncE_syncG -p 13:14'], shell=True)
    subprocess.call(['screen -dmS GOA48 python ./run.py -n GOA_orig_asyncE_syncG -o orig_GOA_asyncE_syncG -p 15:16'], shell=True)
    subprocess.call(['screen -dmS GOA49 python ./run.py -n GOA_orig_asyncE_syncG -o orig_GOA_asyncE_syncG -p 17:18'], shell=True)
    subprocess.call(['screen -dmS GOA410 python ./run.py -n GOA_orig_asyncE_syncG -o orig_GOA_asyncE_syncG -p 19:20'], shell=True)
    subprocess.call(['screen -dmS GOA411 python ./run.py -n GOA_orig_asyncE_syncG -o orig_GOA_asyncE_syncG -p 21:22'], shell=True)
    subprocess.call(['screen -dmS GOA412 python ./run.py -n GOA_orig_asyncE_syncG -o orig_GOA_asyncE_syncG -p 23:24'], shell=True)

    subprocess.call(['screen -dmS GOA51 python ./run.py -n GOA_orig_asyncE_asyncG -o orig_GOA_asyncE_asyncG -p 1:2'], shell=True)
    subprocess.call(['screen -dmS GOA52 python ./run.py -n GOA_orig_asyncE_asyncG -o orig_GOA_asyncE_asyncG -p 3:4'], shell=True)
    subprocess.call(['screen -dmS GOA53 python ./run.py -n GOA_orig_asyncE_asyncG -o orig_GOA_asyncE_asyncG -p 5:6'], shell=True)
    subprocess.call(['screen -dmS GOA54 python ./run.py -n GOA_orig_asyncE_asyncG -o orig_GOA_asyncE_asyncG -p 7:8'], shell=True)
    subprocess.call(['screen -dmS GOA55 python ./run.py -n GOA_orig_asyncE_asyncG -o orig_GOA_asyncE_asyncG -p 9:10'], shell=True)
    subprocess.call(['screen -dmS GOA56 python ./run.py -n GOA_orig_asyncE_asyncG -o orig_GOA_asyncE_asyncG -p 11:12'], shell=True)
    subprocess.call(['screen -dmS GOA57 python ./run.py -n GOA_orig_asyncE_asyncG -o orig_GOA_asyncE_asyncG -p 13:14'], shell=True)
    subprocess.call(['screen -dmS GOA58 python ./run.py -n GOA_orig_asyncE_asyncG -o orig_GOA_asyncE_asyncG -p 15:16'], shell=True)
    subprocess.call(['screen -dmS GOA59 python ./run.py -n GOA_orig_asyncE_asyncG -o orig_GOA_asyncE_asyncG -p 17:18'], shell=True)
    subprocess.call(['screen -dmS GOA510 python ./run.py -n GOA_orig_asyncE_asyncG -o orig_GOA_asyncE_asyncG -p 19:20'], shell=True)
    subprocess.call(['screen -dmS GOA511 python ./run.py -n GOA_orig_asyncE_asyncG -o orig_GOA_asyncE_asyncG -p 21:22'], shell=True)
    subprocess.call(['screen -dmS GOA512 python ./run.py -n GOA_orig_asyncE_asyncG -o orig_GOA_asyncE_asyncG -p 23:24'], shell=True)
    #
    subprocess.call(['screen -dmS GOA011 python ./run.py -n GOA_orig -o orig_GOA -p 1:2'], shell=True)
    subprocess.call(['screen -dmS GOA012 python ./run.py -n GOA_orig -o orig_GOA -p 3:4'], shell=True)
    subprocess.call(['screen -dmS GOA013 python ./run.py -n GOA_orig -o orig_GOA -p 5:6'], shell=True)
    subprocess.call(['screen -dmS GOA014 python ./run.py -n GOA_orig -o orig_GOA -p 7:8'], shell=True)
    subprocess.call(['screen -dmS GOA015 python ./run.py -n GOA_orig -o orig_GOA -p 9:10'], shell=True)
    subprocess.call(['screen -dmS GOA016 python ./run.py -n GOA_orig -o orig_GOA -p 11:12'], shell=True)
    subprocess.call(['screen -dmS GOA017 python ./run.py -n GOA_orig -o orig_GOA -p 13:14'], shell=True)
    subprocess.call(['screen -dmS GOA018 python ./run.py -n GOA_orig -o orig_GOA -p 15:16'], shell=True)
    subprocess.call(['screen -dmS GOA019 python ./run.py -n GOA_orig -o orig_GOA -p 17:18'], shell=True)
    subprocess.call(['screen -dmS GOA0110 python ./run.py -n GOA_orig -o orig_GOA -p 19:20'], shell=True)
    subprocess.call(['screen -dmS GOA0111 python ./run.py -n GOA_orig -o orig_GOA -p 21:22'], shell=True)
    subprocess.call(['screen -dmS GOA0112 python ./run.py -n GOA_orig -o orig_GOA -p 23:24'], shell=True)

    subprocess.call(['screen -dmS GOA021 python ./run.py -n GOA_UNIOA -o UNIOA_GOA -p 1:2'], shell=True)
    subprocess.call(['screen -dmS GOA022 python ./run.py -n GOA_UNIOA -o UNIOA_GOA -p 3:4'], shell=True)
    subprocess.call(['screen -dmS GOA023 python ./run.py -n GOA_UNIOA -o UNIOA_GOA -p 5:6'], shell=True)
    subprocess.call(['screen -dmS GOA024 python ./run.py -n GOA_UNIOA -o UNIOA_GOA -p 7:8'], shell=True)
    subprocess.call(['screen -dmS GOA025 python ./run.py -n GOA_UNIOA -o UNIOA_GOA -p 9:10'], shell=True)
    subprocess.call(['screen -dmS GOA026 python ./run.py -n GOA_UNIOA -o UNIOA_GOA -p 11:12'], shell=True)
    subprocess.call(['screen -dmS GOA027 python ./run.py -n GOA_UNIOA -o UNIOA_GOA -p 13:14'], shell=True)
    subprocess.call(['screen -dmS GOA028 python ./run.py -n GOA_UNIOA -o UNIOA_GOA -p 15:16'], shell=True)
    subprocess.call(['screen -dmS GOA029 python ./run.py -n GOA_UNIOA -o UNIOA_GOA -p 17:18'], shell=True)
    subprocess.call(['screen -dmS GOA0210 python ./run.py -n GOA_UNIOA -o UNIOA_GOA -p 19:20'], shell=True)
    subprocess.call(['screen -dmS GOA0211 python ./run.py -n GOA_UNIOA -o UNIOA_GOA -p 21:22'], shell=True)
    subprocess.call(['screen -dmS GOA0212 python ./run.py -n GOA_UNIOA -o UNIOA_GOA -p 23:24'], shell=True)
    # </editor-folder>

    # <editor-folder desc="3. CSA">
    subprocess.call(['screen -dmS CSA1 python ./run.py -n CSA_UNIOA            -o UNIOA_CSA_syncE'], shell=True)
    subprocess.call(['screen -dmS CSA2 python ./run.py -n CSA_UNIOA_asyncE     -o UNIOA_CSA_asyncE'],shell=True)
    subprocess.call(['screen -dmS CSA3 python ./run.py -n CSA_orig              -o orig_CSA_syncE'],shell=True)
    subprocess.call(['screen -dmS CSA4 python ./run.py -n CSA_orig_asyncE       -o orig_CSA_asyncE'],shell=True)
    #
    subprocess.call(['screen -dmS CSA01 python ./run.py -n CSA_orig             -o orig_CSA'],shell=True)
    subprocess.call(['screen -dmS CSA02 python ./run.py -n CSA_UNIOA           -o UNIOA_CSA'],shell=True)
    # </editor-folder>

    # <editor-folder desc="4. MFO">
    subprocess.call(['screen -dmS MFO1 python ./run.py -n MFO_UNIOA            -o UNIOA_MFO_syncE'],shell=True)
    subprocess.call(['screen -dmS MFO2 python ./run.py -n MFO_UNIOA_asyncE     -o UNIOA_MFO_asyncE'],shell=True)
    subprocess.call(['screen -dmS MFO3 python ./run.py -n MFO_orig              -o orig_MFO_syncE'],shell=True)
    subprocess.call(['screen -dmS MFO4 python ./run.py -n MFO_orig_asyncE       -o orig_MFO_asyncE'],shell=True)
    #
    subprocess.call(['screen -dmS MFO01 python ./run.py -n MFO_orig             -o orig_MFO'],shell=True)
    subprocess.call(['screen -dmS MFO02 python ./run.py -n MFO_UNIOA           -o UNIOA_MFO'],shell=True)
    # </editor-folder>

    # <editor-folder desc="6. BOA">
    subprocess.call(['screen -dmS BOA1 python ./run.py -n BOA_UNIOA              -o UNIOA_BOA_syncE_syncG'],shell=True)
    subprocess.call(['screen -dmS BOA2 python ./run.py -n BOA_UNIOA_asyncE_syncG -o UNIOA_BOA_asyncE_syncG'],shell=True)
    subprocess.call(['screen -dmS BOA3 python ./run.py -n BOA_orig                -o orig_BOA_asyncE_asyncG'],shell=True)
    subprocess.call(['screen -dmS BOA4 python ./run.py -n BOA_orig_syncE_syncG    -o orig_BOA_syncE_syncG'],shell=True)
    subprocess.call(['screen -dmS BOA5 python ./run.py -n BOA_orig_fix            -o orig_BOA_asyncE_syncG'],shell=True)
    #
    subprocess.call(['screen -dmS BOA01 python ./run.py -n BOA_orig_fix           -o orig_BOA_fix'],shell=True)
    subprocess.call(['screen -dmS BOA02 python ./run.py -n BOA_UNIOA             -o UNIOA_BOA'],shell=True)
    # </editor-folder>

    # <editor-folder desc="7. PSO">
    subprocess.call(['screen -dmS PSO1 python ./run.py -n PSO_UNIOA              -o UNIOA_PSO_syncE_syncG'],shell=True)
    subprocess.call(['screen -dmS PSO2 python ./run.py -n PSO_UNIOA_asyncE_syncG -o UNIOA_PSO_asyncE_syncG'],shell=True)
    subprocess.call(['screen -dmS PSO3 python ./run.py -n PSO_orig                -o orig_PSO_asyncE_asyncG'],shell=True)
    subprocess.call(['screen -dmS PSO4 python ./run.py -n PSO_orig_syncE_syncG    -o orig_PSO_syncE_syncG'],shell=True)
    subprocess.call(['screen -dmS PSO5 python ./run.py -n PSO_orig_fix            -o orig_PSO_asyncE_syncG'],shell=True)
    #
    subprocess.call(['screen -dmS PSO01 python ./run.py -n PSO_orig_fix           -o orig_PSO_fix'],shell=True)
    subprocess.call(['screen -dmS PSO02 python ./run.py -n PSO_UNIOA             -o UNIOA_PSO'],shell=True)
    # </editor-folder>