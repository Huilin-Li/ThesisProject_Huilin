import subprocess
##################
if __name__ == '__main__':
    # <editor-folder desc="4. MFO">
    subprocess.call(['screen -dmS MFO1 python ./run.py -n MFO_UNIOA -o UNIOA_MFO_syncE'],shell=True)
    subprocess.call(['screen -dmS MFO2 python ./run.py -n MFO_UNIOA_asyncE -o UNIOA_MFO_asyncE'],shell=True)
    subprocess.call(['screen -dmS MFO3 python ./run.py -n MFO_orig -o orig_MFO_asyncE'],shell=True)
    subprocess.call(['screen -dmS MFO4 python ./run.py -n MFO_orig_syncE -o orig_MFO_syncE'],shell=True)
    #
    subprocess.call(['screen -dmS MFO01 python ./run.py -n MFO_orig -o orig_MFO'],shell=True)
    subprocess.call(['screen -dmS MFO02 python ./run.py -n MFO_UNIOA -o UNIOA_MFO'],shell=True)
    # </editor-folder>