import subprocess
##################
if __name__ == '__main__':
    # <editor-folder desc="1. BA">
    subprocess.call(['screen -dmS BA1 python ./run.py -n BA_UNIOA              -o UNIOA_BA_syncE_syncG'], shell=True)
    subprocess.call(['screen -dmS BA2 python ./run.py -n BA_UNIOA_asyncE_syncG -o UNIOA_BA_asyncE_syncG'], shell=True)
    subprocess.call(['screen -dmS BA3 python ./run.py -n BA_SEP                -o SEP_BA_asyncE_asyncG'], shell=True)
    subprocess.call(['screen -dmS BA4 python ./run.py -n BA_SEP_syncE_syncG    -o SEP_BA_syncE_syncG'], shell=True)
    subprocess.call(['screen -dmS BA5 python ./run.py -n BA_SEP_fix            -o SEP_BA_asyncE_syncG'], shell=True)
    #
    subprocess.call(['screen -dmS BA01 python ./run.py -n BA_SEP_fix           -o SEP_BA_fix'], shell=True)
    subprocess.call(['screen -dmS BA02 python ./run.py -n BA_UNIOA             -o UNIOA_BA'], shell=True)
    # </editor-folder>

    # <editor-folder desc="3. CSA">
    subprocess.call(['screen -dmS CSA1 python ./run.py -n CSA_UNIOA            -o UNIOA_CSA_syncE'], shell=True)
    subprocess.call(['screen -dmS CSA2 python ./run.py -n CSA_UNIOA_asyncE     -o UNIOA_CSA_asyncE'],shell=True)
    subprocess.call(['screen -dmS CSA3 python ./run.py -n CSA_SEP              -o SEP_CSA_syncE'],shell=True)
    subprocess.call(['screen -dmS CSA4 python ./run.py -n CSA_SEP_asyncE       -o SEP_CSA_asyncE'],shell=True)
    #
    subprocess.call(['screen -dmS CSA01 python ./run.py -n CSA_SEP             -o SEP_CSA'],shell=True)
    subprocess.call(['screen -dmS CSA02 python ./run.py -n CSA_UNIOA           -o UNIOA_CSA'],shell=True)
    # </editor-folder>

    # <editor-folder desc="4. MFO">
    subprocess.call(['screen -dmS MFO1 python ./run.py -n MFO_UNIOA            -o UNIOA_MFO_syncE'],shell=True)
    subprocess.call(['screen -dmS MFO2 python ./run.py -n MFO_UNIOA_asyncE     -o UNIOA_MFO_asyncE'],shell=True)
    subprocess.call(['screen -dmS MFO3 python ./run.py -n MFO_SEP              -o SEP_MFO_syncE'],shell=True)
    subprocess.call(['screen -dmS MFO4 python ./run.py -n MFO_SEP_asyncE       -o SEP_MFO_asyncE'],shell=True)
    #
    subprocess.call(['screen -dmS MFO01 python ./run.py -n MFO_SEP             -o SEP_MFO'],shell=True)
    subprocess.call(['screen -dmS MFO02 python ./run.py -n MFO_UNIOA           -o UNIOA_MFO'],shell=True)
    # </editor-folder>

    # <editor-folder desc="6. BOA">
    subprocess.call(['screen -dmS BOA1 python ./run.py -n BOA_UNIOA              -o UNIOA_BOA_syncE_syncG'],shell=True)
    subprocess.call(['screen -dmS BOA2 python ./run.py -n BOA_UNIOA_asyncE_syncG -o UNIOA_BOA_asyncE_syncG'],shell=True)
    subprocess.call(['screen -dmS BOA3 python ./run.py -n BOA_SEP                -o SEP_BOA_asyncE_asyncG'],shell=True)
    subprocess.call(['screen -dmS BOA4 python ./run.py -n BOA_SEP_syncE_syncG    -o SEP_BOA_syncE_syncG'],shell=True)
    subprocess.call(['screen -dmS BOA5 python ./run.py -n BOA_SEP_fix            -o SEP_BOA_asyncE_syncG'],shell=True)
    #
    subprocess.call(['screen -dmS BOA01 python ./run.py -n BOA_SEP_fix           -o SEP_BOA_fix'],shell=True)
    subprocess.call(['screen -dmS BOA02 python ./run.py -n BOA_UNIOA             -o UNIOA_BOA'],shell=True)
    # </editor-folder>

    # <editor-folder desc="7. PSO">
    subprocess.call(['screen -dmS PSO1 python ./run.py -n PSO_UNIOA              -o UNIOA_PSO_syncE_syncG'],shell=True)
    subprocess.call(['screen -dmS PSO2 python ./run.py -n PSO_UNIOA_asyncE_syncG -o UNIOA_PSO_asyncE_syncG'],shell=True)
    subprocess.call(['screen -dmS PSO3 python ./run.py -n PSO_SEP                -o SEP_PSO_asyncE_asyncG'],shell=True)
    subprocess.call(['screen -dmS PSO4 python ./run.py -n PSO_SEP_syncE_syncG    -o SEP_PSO_syncE_syncG'],shell=True)
    subprocess.call(['screen -dmS PSO5 python ./run.py -n PSO_SEP_fix            -o SEP_PSO_asyncE_syncG'],shell=True)
    #
    subprocess.call(['screen -dmS PSO01 python ./run.py -n PSO_SEP_fix           -o SEP_PSO_fix'],shell=True)
    subprocess.call(['screen -dmS PSO02 python ./run.py -n PSO_UNIOA             -o UNIOA_PSO'],shell=True)
    # </editor-folder>