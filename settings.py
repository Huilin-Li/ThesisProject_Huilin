import sys
import time
import ioh
from UNIOA_implement import *
from orig_implement import *
from datetime import datetime

#
# extract information from terminal
#


def optimizer_running(problems, instances, dimensions, num_runs, paras_set, optimizer_name, output_name):
    Which_alg = output_name.split("_")[1]
    folder_name = Which_alg + '_folder'
    data_name = output_name
    st = time.time()
    print('--->   ' + output_name + ' is optmizting', flush=True)
    logger = ioh.logger.Analyzer(folder_name='DataFiles/'+folder_name+'/'+data_name, algorithm_name=output_name)
    for p_id in problems:
        print('P-id={}'.format(p_id), end=":", flush=True)
        for d in dimensions:
            print('d-{}'.format(d), end=":", flush=True)
            for i_id in instances:
                print('{}'.format(i_id), end="", flush=True)
                func = ioh.get_problem(fid=p_id, dim=d, iid=i_id)
                print('', end='(', flush=True)
                for rep in range(num_runs):
                    #func.attach_logger(logger)
                    print('{}'.format(rep), end="", flush=True)
                    func.attach_logger(logger)
                    opt = eval(optimizer_name)(func, paras_set)
                    opt()
                    func.reset()
                print('', end=')', flush=True)

    print('costs', round((time.time() - st) / 60, 2), 'minutes')
    with open("DataFiles/runningtime_" + Which_alg + ".txt", "a+") as text_file:
        date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        runningtime = round((time.time() - st) / 60, 2)
        print("{} | {}: {} minutes.".format(date, output_name, runningtime), file=text_file)

def problems_option(problems_input):
    print('###############################################################################################')
    problems = []
    if problems_input.isdigit():
        print('###   You will optimize problem {} '.format(problems_input), flush=True)
        problems.append(int(problems_input))
    elif ',' in problems_input:
        print('###   You will optimize problem ', end="", flush=True)
        for i in range(len(problems_input.split(','))):
            if i == len(problems_input.split(',')) - 1:
                print(problems_input.split(',')[i], end=" ", flush=True)
                print()
            else:
                print(problems_input.split(',')[i], end=", ", flush=True)
        problems = [int(P_id) for P_id in problems_input.split(',')]
    elif ':' in problems_input:
        print('###   You will optimize problem ', end="", flush=True)
        for i in range(int(problems_input.split(':')[0]), int(problems_input.split(':')[1]) + 1):
            if i == int(problems_input.split(':')[1]):
                print(i, end="  ", flush=True)
                print()
            else:
                print(i, end=", ", flush=True)
        a = int(problems_input.split(':')[0])
        b = int(problems_input.split(':')[1]) + 1
        problems = list(range(a, b))
    else:
        print('Error: Please re-enter Problem ID!')
    return problems

def instances_option(instances_input):
    print('###   You will optimize {} instances per problem.'.format(int(instances_input)), flush=True)
    instances = list(range(1, instances_input + 1))
    return instances

def dimension_option(dimensions_input):
    dimensions = []
    if dimensions_input.isdigit():
        print('###   You will optimize problems at dimension {} '.format(dimensions_input), flush=True)
        dimensions.append(int(dimensions_input))
    elif ',' in dimensions_input:
        print('###   You will optimize problems at dimension ', end="", flush=True)
        for i in range(len(dimensions_input.split(','))):
            if i == len(dimensions_input.split(',')) - 1:
                print(dimensions_input.split(',')[i], end=" ", flush=True)
                print()
            else:
                print(dimensions_input.split(',')[i], end=", ", flush=True)
        dimensions = [int(d) for d in dimensions_input.split(',')]
    elif ':' in dimensions_input:
        print('###   You will optimize problems at dimension ', end="", flush=True)
        for i in range(int(dimensions_input.split(':')[0]), int(dimensions_input.split(':')[1]) + 1):
            if i == int(dimensions_input.split(':')[1]):
                print(i, end="  ", flush=True)
                print()
            else:
                print(i, end=", ", flush=True)
        a = int(dimensions_input.split(':')[0])
        b = int(dimensions_input.split(':')[1]) + 1
        dimensions = list(range(a, b))
    else:
        print('Error: Please re-enter dimension!')
    return dimensions

def run_option(runs_input):
    print('###   You will experiment {} runs per problem per instance per dimension.'.format(int(runs_input)), flush=True)
    return runs_input


