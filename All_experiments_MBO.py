import subprocess
##################
if __name__ == '__main__':
    # <editor-folder desc="5. MBO">
    subprocess.call(['screen -dmS MBO11 python ./run.py -n MBO_UNIOA -o UNIOA_MBO_syncE_syncG -p 1:2'],shell=True)
    subprocess.call(['screen -dmS MBO12 python ./run.py -n MBO_UNIOA -o UNIOA_MBO_syncE_syncG -p 3:4'],shell=True)
    subprocess.call(['screen -dmS MBO13 python ./run.py -n MBO_UNIOA -o UNIOA_MBO_syncE_syncG -p 5:6'],shell=True)
    subprocess.call(['screen -dmS MBO14 python ./run.py -n MBO_UNIOA -o UNIOA_MBO_syncE_syncG -p 7:8'],shell=True)
    subprocess.call(['screen -dmS MBO15 python ./run.py -n MBO_UNIOA -o UNIOA_MBO_syncE_syncG -p 9:10'],shell=True)
    subprocess.call(['screen -dmS MBO16 python ./run.py -n MBO_UNIOA -o UNIOA_MBO_syncE_syncG -p 11:12'],shell=True)
    subprocess.call(['screen -dmS MBO17 python ./run.py -n MBO_UNIOA -o UNIOA_MBO_syncE_syncG -p 13:14'],shell=True)
    subprocess.call(['screen -dmS MBO18 python ./run.py -n MBO_UNIOA -o UNIOA_MBO_syncE_syncG -p 15:16'],shell=True)
    subprocess.call(['screen -dmS MBO19 python ./run.py -n MBO_UNIOA -o UNIOA_MBO_syncE_syncG -p 17:18'],shell=True)
    subprocess.call(['screen -dmS MBO110 python ./run.py -n MBO_UNIOA -o UNIOA_MBO_syncE_syncG -p 19:20'],shell=True)
    subprocess.call(['screen -dmS MBO111 python ./run.py -n MBO_UNIOA -o UNIOA_MBO_syncE_syncG -p 21:22'],shell=True)
    subprocess.call(['screen -dmS MBO112 python ./run.py -n MBO_UNIOA -o UNIOA_MBO_syncE_syncG -p 23:24'],shell=True)

    subprocess.call(['screen -dmS MBO21 python ./run.py -n MBO_UNIOA_asyncE_syncG -o UNIOA_MBO_asyncE_syncG -p 1:2'],shell=True)
    subprocess.call(['screen -dmS MBO22 python ./run.py -n MBO_UNIOA_asyncE_syncG -o UNIOA_MBO_asyncE_syncG -p 3:4'],shell=True)
    subprocess.call(['screen -dmS MBO23 python ./run.py -n MBO_UNIOA_asyncE_syncG -o UNIOA_MBO_asyncE_syncG -p 5:6'],shell=True)
    subprocess.call(['screen -dmS MBO24 python ./run.py -n MBO_UNIOA_asyncE_syncG -o UNIOA_MBO_asyncE_syncG -p 7:8'],shell=True)
    subprocess.call(['screen -dmS MBO25 python ./run.py -n MBO_UNIOA_asyncE_syncG -o UNIOA_MBO_asyncE_syncG -p 9:10'],shell=True)
    subprocess.call(['screen -dmS MBO26 python ./run.py -n MBO_UNIOA_asyncE_syncG -o UNIOA_MBO_asyncE_syncG -p 11:12'],shell=True)
    subprocess.call(['screen -dmS MBO27 python ./run.py -n MBO_UNIOA_asyncE_syncG -o UNIOA_MBO_asyncE_syncG -p 13:14'],shell=True)
    subprocess.call(['screen -dmS MBO28 python ./run.py -n MBO_UNIOA_asyncE_syncG -o UNIOA_MBO_asyncE_syncG -p 15:16'],shell=True)
    subprocess.call(['screen -dmS MBO29 python ./run.py -n MBO_UNIOA_asyncE_syncG -o UNIOA_MBO_asyncE_syncG -p 17:18'],shell=True)
    subprocess.call(['screen -dmS MBO210 python ./run.py -n MBO_UNIOA_asyncE_syncG -o UNIOA_MBO_asyncE_syncG -p 19:20'],shell=True)
    subprocess.call(['screen -dmS MBO211 python ./run.py -n MBO_UNIOA_asyncE_syncG -o UNIOA_MBO_asyncE_syncG -p 21:22'],shell=True)
    subprocess.call(['screen -dmS MBO212 python ./run.py -n MBO_UNIOA_asyncE_syncG -o UNIOA_MBO_asyncE_syncG -p 23:24'],shell=True)

    subprocess.call(['screen -dmS MBO31 python ./run.py -n MBO_SEP -o SEP_MBO_syncE_syncG -p 1:2'],shell=True)
    subprocess.call(['screen -dmS MBO32 python ./run.py -n MBO_SEP -o SEP_MBO_syncE_syncG -p 3:4'],shell=True)
    subprocess.call(['screen -dmS MBO33 python ./run.py -n MBO_SEP -o SEP_MBO_syncE_syncG -p 5:6'],shell=True)
    subprocess.call(['screen -dmS MBO34 python ./run.py -n MBO_SEP -o SEP_MBO_syncE_syncG -p 7:8'],shell=True)
    subprocess.call(['screen -dmS MBO35 python ./run.py -n MBO_SEP -o SEP_MBO_syncE_syncG -p 9:10'],shell=True)
    subprocess.call(['screen -dmS MBO36 python ./run.py -n MBO_SEP -o SEP_MBO_syncE_syncG -p 11:12'],shell=True)
    subprocess.call(['screen -dmS MBO37 python ./run.py -n MBO_SEP -o SEP_MBO_syncE_syncG -p 13:14'],shell=True)
    subprocess.call(['screen -dmS MBO38 python ./run.py -n MBO_SEP -o SEP_MBO_syncE_syncG -p 15:16'],shell=True)
    subprocess.call(['screen -dmS MBO39 python ./run.py -n MBO_SEP -o SEP_MBO_syncE_syncG -p 17:18'],shell=True)
    subprocess.call(['screen -dmS MBO310 python ./run.py -n MBO_SEP -o SEP_MBO_syncE_syncG -p 19:20'],shell=True)
    subprocess.call(['screen -dmS MBO311 python ./run.py -n MBO_SEP -o SEP_MBO_syncE_syncG -p 21:22'],shell=True)
    subprocess.call(['screen -dmS MBO312 python ./run.py -n MBO_SEP -o SEP_MBO_syncE_syncG -p 23:24'],shell=True)

    subprocess.call(['screen -dmS MBO41 python ./run.py -n MBO_SEP_asyncE_syncG -o SEP_MBO_asyncE_syncG -p 1:2'],shell=True)
    subprocess.call(['screen -dmS MBO42 python ./run.py -n MBO_SEP_asyncE_syncG -o SEP_MBO_asyncE_syncG -p 3:4'],shell=True)
    subprocess.call(['screen -dmS MBO43 python ./run.py -n MBO_SEP_asyncE_syncG -o SEP_MBO_asyncE_syncG -p 5:6'],shell=True)
    subprocess.call(['screen -dmS MBO44 python ./run.py -n MBO_SEP_asyncE_syncG -o SEP_MBO_asyncE_syncG -p 7:8'],shell=True)
    subprocess.call(['screen -dmS MBO45 python ./run.py -n MBO_SEP_asyncE_syncG -o SEP_MBO_asyncE_syncG -p 9:10'],shell=True)
    subprocess.call(['screen -dmS MBO46 python ./run.py -n MBO_SEP_asyncE_syncG -o SEP_MBO_asyncE_syncG -p 11:12'],shell=True)
    subprocess.call(['screen -dmS MBO47 python ./run.py -n MBO_SEP_asyncE_syncG -o SEP_MBO_asyncE_syncG -p 13:14'],shell=True)
    subprocess.call(['screen -dmS MBO48 python ./run.py -n MBO_SEP_asyncE_syncG -o SEP_MBO_asyncE_syncG -p 15:16'],shell=True)
    subprocess.call(['screen -dmS MBO49 python ./run.py -n MBO_SEP_asyncE_syncG -o SEP_MBO_asyncE_syncG -p 17:18'],shell=True)
    subprocess.call(['screen -dmS MBO410 python ./run.py -n MBO_SEP_asyncE_syncG -o SEP_MBO_asyncE_syncG -p 19:20'],shell=True)
    subprocess.call(['screen -dmS MBO411 python ./run.py -n MBO_SEP_asyncE_syncG -o SEP_MBO_asyncE_syncG -p 21:22'],shell=True)
    subprocess.call(['screen -dmS MBO412 python ./run.py -n MBO_SEP_asyncE_syncG -o SEP_MBO_asyncE_syncG -p 23:24'],shell=True)

    subprocess.call(['screen -dmS MBO51 python ./run.py -n MBO_SEP_asyncE_asyncG -o SEP_MBO_asyncE_asyncG -p 1:2'],shell=True)
    subprocess.call(['screen -dmS MBO52 python ./run.py -n MBO_SEP_asyncE_asyncG -o SEP_MBO_asyncE_asyncG -p 3:4'],shell=True)
    subprocess.call(['screen -dmS MBO53 python ./run.py -n MBO_SEP_asyncE_asyncG -o SEP_MBO_asyncE_asyncG -p 5:6'],shell=True)
    subprocess.call(['screen -dmS MBO54 python ./run.py -n MBO_SEP_asyncE_asyncG -o SEP_MBO_asyncE_asyncG -p 7:8'],shell=True)
    subprocess.call(['screen -dmS MBO55 python ./run.py -n MBO_SEP_asyncE_asyncG -o SEP_MBO_asyncE_asyncG -p 9:10'],shell=True)
    subprocess.call(['screen -dmS MBO56 python ./run.py -n MBO_SEP_asyncE_asyncG -o SEP_MBO_asyncE_asyncG -p 11:12'],shell=True)
    subprocess.call(['screen -dmS MBO57 python ./run.py -n MBO_SEP_asyncE_asyncG -o SEP_MBO_asyncE_asyncG -p 13:14'],shell=True)
    subprocess.call(['screen -dmS MBO58 python ./run.py -n MBO_SEP_asyncE_asyncG -o SEP_MBO_asyncE_asyncG -p 15:16'],shell=True)
    subprocess.call(['screen -dmS MBO59 python ./run.py -n MBO_SEP_asyncE_asyncG -o SEP_MBO_asyncE_asyncG -p 17:18'],shell=True)
    subprocess.call(['screen -dmS MBO510 python ./run.py -n MBO_SEP_asyncE_asyncG -o SEP_MBO_asyncE_asyncG -p 19:20'],shell=True)
    subprocess.call(['screen -dmS MBO511 python ./run.py -n MBO_SEP_asyncE_asyncG -o SEP_MBO_asyncE_asyncG -p 21:22'],shell=True)
    subprocess.call(['screen -dmS MBO512 python ./run.py -n MBO_SEP_asyncE_asyncG -o SEP_MBO_asyncE_asyncG -p 23:24'],shell=True)

    #
    subprocess.call(['screen -dmS MBO011 python ./run.py -n MBO_SEP -o SEP_MBO -p 1:2'],shell=True)
    subprocess.call(['screen -dmS MBO012 python ./run.py -n MBO_SEP -o SEP_MBO -p 3:4'],shell=True)
    subprocess.call(['screen -dmS MBO013 python ./run.py -n MBO_SEP -o SEP_MBO -p 5:6'],shell=True)
    subprocess.call(['screen -dmS MBO014 python ./run.py -n MBO_SEP -o SEP_MBO -p 7:8'],shell=True)
    subprocess.call(['screen -dmS MBO015 python ./run.py -n MBO_SEP -o SEP_MBO -p 9:10'],shell=True)
    subprocess.call(['screen -dmS MBO016 python ./run.py -n MBO_SEP -o SEP_MBO -p 11:12'],shell=True)
    subprocess.call(['screen -dmS MBO017 python ./run.py -n MBO_SEP -o SEP_MBO -p 13:14'],shell=True)
    subprocess.call(['screen -dmS MBO018 python ./run.py -n MBO_SEP -o SEP_MBO -p 15:16'],shell=True)
    subprocess.call(['screen -dmS MBO019 python ./run.py -n MBO_SEP -o SEP_MBO -p 17:18'],shell=True)
    subprocess.call(['screen -dmS MBO0110 python ./run.py -n MBO_SEP -o SEP_MBO -p 19:20'],shell=True)
    subprocess.call(['screen -dmS MBO0111 python ./run.py -n MBO_SEP -o SEP_MBO -p 21:22'],shell=True)
    subprocess.call(['screen -dmS MBO0112 python ./run.py -n MBO_SEP -o SEP_MBO -p 23:24'],shell=True)

    subprocess.call(['screen -dmS MBO021 python ./run.py -n MBO_UNIOA -o UNIOA_BA -p 1:2'],shell=True)
    subprocess.call(['screen -dmS MBO022 python ./run.py -n MBO_UNIOA -o UNIOA_BA -p 3:4'],shell=True)
    subprocess.call(['screen -dmS MBO023 python ./run.py -n MBO_UNIOA -o UNIOA_BA -p 5:6'],shell=True)
    subprocess.call(['screen -dmS MBO024 python ./run.py -n MBO_UNIOA -o UNIOA_BA -p 7:8'],shell=True)
    subprocess.call(['screen -dmS MBO025 python ./run.py -n MBO_UNIOA -o UNIOA_BA -p 9:10'],shell=True)
    subprocess.call(['screen -dmS MBO026 python ./run.py -n MBO_UNIOA -o UNIOA_BA -p 11:12'],shell=True)
    subprocess.call(['screen -dmS MBO027 python ./run.py -n MBO_UNIOA -o UNIOA_BA -p 13:14'],shell=True)
    subprocess.call(['screen -dmS MBO028 python ./run.py -n MBO_UNIOA -o UNIOA_BA -p 15:16'],shell=True)
    subprocess.call(['screen -dmS MBO029 python ./run.py -n MBO_UNIOA -o UNIOA_BA -p 17:18'],shell=True)
    subprocess.call(['screen -dmS MBO0210 python ./run.py -n MBO_UNIOA -o UNIOA_BA -p 19:20'],shell=True)
    subprocess.call(['screen -dmS MBO0211 python ./run.py -n MBO_UNIOA -o UNIOA_BA -p 21:22'],shell=True)
    subprocess.call(['screen -dmS MBO0212 python ./run.py -n MBO_UNIOA -o UNIOA_BA -p 23:24'],shell=True)
    # </editor-folder>









