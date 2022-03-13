import subprocess
##################
if __name__ == '__main__':
    # <editor-folder desc="1. BA">
    subprocess.call(['screen -dmS BA1 python ./all_experiments/run.py -n BA_UNIOA -o UNIOA_BA_syncE_syncG'], shell=True)
    subprocess.call(['screen -dmS BA2 python ./run.py -n BA_UNIOA_asyncE_syncG -o UNIOA_BA_asyncE_syncG'], shell=True)
    subprocess.call(['screen -dmS BA3 python ./run.py -n BA_orig -o orig_BA_asyncE_asyncG'], shell=True)
    subprocess.call(['screen -dmS BA4 python ./run.py -n BA_orig_syncE_syncG -o orig_BA_syncE_syncG'], shell=True)
    subprocess.call(['screen -dmS BA5 python ./run.py -n BA_orig_fix -o orig_BA_asyncE_syncG'], shell=True)
    #
    subprocess.call(['screen -dmS BA01 python ./run.py -n BA_orig_fix -o orig_BA_fix'], shell=True)
    subprocess.call(['screen -dmS BA02 python ./run.py -n BA_UNIOA -o UNIOA_BA'], shell=True)
    # </editor-folder>
