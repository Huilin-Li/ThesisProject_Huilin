import subprocess
##################
if __name__ == '__main__':
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