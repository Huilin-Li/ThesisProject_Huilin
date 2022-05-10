import subprocess
##################
if __name__ == '__main__':

    # <editor-folder desc="5. MBO">
    ########################## -1
    subprocess.call(['screen -dmS MBO11 python  ./run.py -n MBO_UNIOA -o UNIOA_MBO_syncE_syncG -p 1:3'], shell=True)
    subprocess.call(['screen -dmS MBO12 python  ./run.py -n MBO_UNIOA -o UNIOA_MBO_syncE_syncG -p 4:6'], shell=True)
    subprocess.call(['screen -dmS MBO13 python  ./run.py -n MBO_UNIOA -o UNIOA_MBO_syncE_syncG -p 7:9'], shell=True)
    subprocess.call(['screen -dmS MBO14 python  ./run.py -n MBO_UNIOA -o UNIOA_MBO_syncE_syncG -p 10:12'], shell=True)
    subprocess.call(['screen -dmS MBO15 python  ./run.py -n MBO_UNIOA -o UNIOA_MBO_syncE_syncG -p 13:15'], shell=True)
    subprocess.call(['screen -dmS MBO16 python  ./run.py -n MBO_UNIOA -o UNIOA_MBO_syncE_syncG -p 16:18'], shell=True)
    subprocess.call(['screen -dmS MBO17 python  ./run.py -n MBO_UNIOA -o UNIOA_MBO_syncE_syncG -p 19:21'], shell=True)
    subprocess.call(['screen -dmS MBO18 python  ./run.py -n MBO_UNIOA -o UNIOA_MBO_syncE_syncG -p 22:24'], shell=True)

    ########################## -2
    # subprocess.call(['screen -dmS MBO21 python ./run.py -n MBO_UNIOA_asyncE_syncG -o UNIOA_MBO_asyncE_syncG -p 1:3'], shell=True)
    # subprocess.call(['screen -dmS MBO22 python ./run.py -n MBO_UNIOA_asyncE_syncG -o UNIOA_MBO_asyncE_syncG -p 4:6'], shell=True)
    # subprocess.call(['screen -dmS MBO23 python ./run.py -n MBO_UNIOA_asyncE_syncG -o UNIOA_MBO_asyncE_syncG -p 7:9'], shell=True)
    # subprocess.call(['screen -dmS MBO24 python ./run.py -n MBO_UNIOA_asyncE_syncG -o UNIOA_MBO_asyncE_syncG -p 10:12'], shell=True)
    # subprocess.call(['screen -dmS MBO25 python ./run.py -n MBO_UNIOA_asyncE_syncG -o UNIOA_MBO_asyncE_syncG -p 13:15'], shell=True)
    # subprocess.call(['screen -dmS MBO26 python ./run.py -n MBO_UNIOA_asyncE_syncG -o UNIOA_MBO_asyncE_syncG -p 16:18'], shell=True)
    # subprocess.call(['screen -dmS MBO27 python ./run.py -n MBO_UNIOA_asyncE_syncG -o UNIOA_MBO_asyncE_syncG -p 19:21'], shell=True)
    # subprocess.call(['screen -dmS MBO28 python ./run.py -n MBO_UNIOA_asyncE_syncG -o UNIOA_MBO_asyncE_syncG -p 22:24'], shell=True)

    # ########################## -3
    subprocess.call(['screen -dmS MBO31 python ./run.py -n MBO_orig -o orig_MBO_syncE_syncG -p 1:3'], shell=True)
    subprocess.call(['screen -dmS MBO32 python ./run.py -n MBO_orig -o orig_MBO_syncE_syncG -p 4:6'], shell=True)
    subprocess.call(['screen -dmS MBO33 python ./run.py -n MBO_orig -o orig_MBO_syncE_syncG -p 7:9'], shell=True)
    subprocess.call(['screen -dmS MBO34 python ./run.py -n MBO_orig -o orig_MBO_syncE_syncG -p 10:12'], shell=True)
    subprocess.call(['screen -dmS MBO35 python ./run.py -n MBO_orig -o orig_MBO_syncE_syncG -p 13:15'], shell=True)
    subprocess.call(['screen -dmS MBO36 python ./run.py -n MBO_orig -o orig_MBO_syncE_syncG -p 16:18'], shell=True)
    subprocess.call(['screen -dmS MBO37 python ./run.py -n MBO_orig -o orig_MBO_syncE_syncG -p 19:21'], shell=True)
    subprocess.call(['screen -dmS MBO38 python ./run.py -n MBO_orig -o orig_MBO_syncE_syncG -p 22:24'], shell=True)

    # ########################## -4
    subprocess.call(['screen -dmS MBO41 python ./run.py -n MBO_orig_asyncE_syncG -o orig_MBO_asyncE_syncG -p 1:3'], shell=True)
    subprocess.call(['screen -dmS MBO42 python ./run.py -n MBO_orig_asyncE_syncG -o orig_MBO_asyncE_syncG -p 4:6'], shell=True)
    subprocess.call(['screen -dmS MBO43 python ./run.py -n MBO_orig_asyncE_syncG -o orig_MBO_asyncE_syncG -p 7:9'], shell=True)
    subprocess.call(['screen -dmS MBO44 python ./run.py -n MBO_orig_asyncE_syncG -o orig_MBO_asyncE_syncG -p 10:12'], shell=True)
    subprocess.call(['screen -dmS MBO45 python ./run.py -n MBO_orig_asyncE_syncG -o orig_MBO_asyncE_syncG -p 13:15'], shell=True)
    subprocess.call(['screen -dmS MBO46 python ./run.py -n MBO_orig_asyncE_syncG -o orig_MBO_asyncE_syncG -p 16:18'], shell=True)
    subprocess.call(['screen -dmS MBO47 python ./run.py -n MBO_orig_asyncE_syncG -o orig_MBO_asyncE_syncG -p 19:21'], shell=True)
    subprocess.call(['screen -dmS MBO48 python ./run.py -n MBO_orig_asyncE_syncG -o orig_MBO_asyncE_syncG -p 22:24'], shell=True)

    # ########################## -5
    subprocess.call(['screen -dmS MBO51 python ./run.py -n MBO_orig_asyncE_asyncG -o orig_MBO_asyncE_asyncG -p 1:3'], shell=True)
    subprocess.call(['screen -dmS MBO52 python ./run.py -n MBO_orig_asyncE_asyncG -o orig_MBO_asyncE_asyncG -p 4:6'], shell=True)
    subprocess.call(['screen -dmS MBO53 python ./run.py -n MBO_orig_asyncE_asyncG -o orig_MBO_asyncE_asyncG -p 7:9'], shell=True)
    subprocess.call(['screen -dmS MBO54 python ./run.py -n MBO_orig_asyncE_asyncG -o orig_MBO_asyncE_asyncG -p 10:12'], shell=True)
    subprocess.call(['screen -dmS MBO55 python ./run.py -n MBO_orig_asyncE_asyncG -o orig_MBO_asyncE_asyncG -p 13:15'], shell=True)
    subprocess.call(['screen -dmS MBO56 python ./run.py -n MBO_orig_asyncE_asyncG -o orig_MBO_asyncE_asyncG -p 16:18'], shell=True)
    subprocess.call(['screen -dmS MBO57 python ./run.py -n MBO_orig_asyncE_asyncG -o orig_MBO_asyncE_asyncG -p 19:21'], shell=True)
    subprocess.call(['screen -dmS MBO58 python ./run.py -n MBO_orig_asyncE_asyncG -o orig_MBO_asyncE_asyncG -p 22:24'], shell=True)

    #
    # #
    # ########################## -6
    subprocess.call(['screen -dmS MBO011 python ./run.py -n MBO_orig -o orig_MBO -p 1:3'], shell=True)
    subprocess.call(['screen -dmS MBO012 python ./run.py -n MBO_orig -o orig_MBO -p 4:6'], shell=True)
    subprocess.call(['screen -dmS MBO013 python ./run.py -n MBO_orig -o orig_MBO -p 7:9'], shell=True)
    subprocess.call(['screen -dmS MBO014 python ./run.py -n MBO_orig -o orig_MBO -p 10:12'], shell=True)
    subprocess.call(['screen -dmS MBO015 python ./run.py -n MBO_orig -o orig_MBO -p 13:15'], shell=True)
    subprocess.call(['screen -dmS MBO016 python ./run.py -n MBO_orig -o orig_MBO -p 16:18'], shell=True)
    subprocess.call(['screen -dmS MBO017 python ./run.py -n MBO_orig -o orig_MBO -p 19:21'], shell=True)
    subprocess.call(['screen -dmS MBO018 python ./run.py -n MBO_orig -o orig_MBO -p 22:24'], shell=True)
    # ########################## -7
    # subprocess.call(['screen -dmS MBO021 python ./run.py -n MBO_UNIOA -o UNIOA_MBO -p 1:3'], shell=True)
    # subprocess.call(['screen -dmS MBO022 python ./run.py -n MBO_UNIOA -o UNIOA_MBO -p 4:6'], shell=True)
    # subprocess.call(['screen -dmS MBO023 python ./run.py -n MBO_UNIOA -o UNIOA_MBO -p 7:9'], shell=True)
    # subprocess.call(['screen -dmS MBO024 python ./run.py -n MBO_UNIOA -o UNIOA_MBO -p 10:12'], shell=True)
    # subprocess.call(['screen -dmS MBO025 python ./run.py -n MBO_UNIOA -o UNIOA_MBO -p 13:15'], shell=True)
    # subprocess.call(['screen -dmS MBO026 python ./run.py -n MBO_UNIOA -o UNIOA_MBO -p 16:18'], shell=True)
    # subprocess.call(['screen -dmS MBO027 python ./run.py -n MBO_UNIOA -o UNIOA_MBO -p 19:21'], shell=True)
    # subprocess.call(['screen -dmS MBO028 python ./run.py -n MBO_UNIOA -o UNIOA_MBO -p 22:24'], shell=True)
    # </editor-folder>
