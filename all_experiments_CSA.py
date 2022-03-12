import subprocess
##################
if __name__ == '__main__':

    # <editor-folder desc="3. CSA">
    subprocess.call(['screen -dmS CSA1 python ./run.py -n CSA_UNIOA -o UNIOA_CSA_syncE'], shell=True)
    subprocess.call(['screen -dmS CSA2 python ./run.py -n CSA_UNIOA_asyncE -o UNIOA_CSA_asyncE'],shell=True)
    subprocess.call(['screen -dmS CSA3 python ./run.py -n CSA_orig -o orig_CSA_syncE'],shell=True)
    subprocess.call(['screen -dmS CSA4 python ./run.py -n CSA_orig_asyncE -o orig_CSA_asyncE'],shell=True)
    #
    subprocess.call(['screen -dmS CSA01 python ./run.py -n CSA_orig -o orig_CSA'],shell=True)
    subprocess.call(['screen -dmS CSA02 python ./run.py -n CSA_UNIOA -o UNIOA_CSA'],shell=True)
    # </editor-folder>
