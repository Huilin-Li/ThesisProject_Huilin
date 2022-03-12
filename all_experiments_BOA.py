import subprocess
##################
if __name__ == '__main__':

    # <editor-folder desc="6. BOA">
    subprocess.call(['screen -dmS BOA1 python ./run.py -n BOA_UNIOA -o UNIOA_BOA_syncE_syncG'],shell=True)
    subprocess.call(['screen -dmS BOA2 python ./run.py -n BOA_UNIOA_asyncE_syncG -o UNIOA_BOA_asyncE_syncG'],shell=True)
    subprocess.call(['screen -dmS BOA3 python ./run.py -n BOA_orig -o orig_BOA_asyncE_asyncG'],shell=True)
    subprocess.call(['screen -dmS BOA4 python ./run.py -n BOA_orig_syncE_syncG -o orig_BOA_syncE_syncG'],shell=True)
    subprocess.call(['screen -dmS BOA5 python ./run.py -n BOA_orig_fix -o orig_BOA_asyncE_syncG'],shell=True)
    #
    subprocess.call(['screen -dmS BOA01 python ./run.py -n BOA_orig_fix -o orig_BOA_fix'],shell=True)
    subprocess.call(['screen -dmS BOA02 python ./run.py -n BOA_UNIOA -o UNIOA_BOA'],shell=True)
    # </editor-folder>
