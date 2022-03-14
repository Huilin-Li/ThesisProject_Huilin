import argparse
from settings import *

#
# main python script for executing algorithms
#

parser = argparse.ArgumentParser(description='Experiments.')

parser.add_argument('-n', '--name', type=str, required=True, metavar='', help='Optimizer name.')
parser.add_argument('-o', '--OutputFileName', type=str, required=True, metavar='', help='Data folder and Algorithm name.')
parser.add_argument('-p', '--problems', type=str, default= '1:24', metavar='', help='Problems used in experiments (default: from Problem-1 to Problem-24).')
parser.add_argument('-d', '--dimensions', type=str, default='5,20', metavar='', help='Dimensions used in experiments (default: Dimension-5 and Dimension-20).')
parser.add_argument('-i', '--instances', type=int, default=5, metavar='', help='Number of instances used in experiments (default: 5 instances).')
parser.add_argument('-r', '--runs', type=int, default=5, metavar='', help='Number of experiments executed per problem per instance per dimension (default: 5 runs).')

args = parser.parse_args()

if __name__ == "__main__":
    # obtain information from terminal
    optimizer_name =args.name
    output_name = args.OutputFileName
    p_str = args.problems
    d_str = args.dimensions
    i_int= args.instances
    r_int = args.runs

    # extract inputs
    problems = problems_option(problems_input=p_str)
    instances = instances_option(instances_input=i_int)
    dimensions = dimension_option(dimensions_input=d_str)
    num_runs = run_option(runs_input=r_int)

    # parameter settings of optimizers
    paras_set = {}

    print('######################################################################################')
    optimizer_running(problems, instances, dimensions, num_runs, paras_set, optimizer_name, output_name)













     
    
    



