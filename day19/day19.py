# File for day 19 of AoC 2023
# Written by Joshua Yeaton on 1/1/2024

def add_line(line, flow_dic):
    line_segs = line[0:-1].split('{')
    flow_name = line_segs[0]
    flows = line_segs[1].split(',')
    actual_flows = []
    for flow in flows:
        actual_flows.append(flow.split(':'))
    flow_dic.update({flow_name:actual_flows})

def query_vals(line, flow_dic):
    local_vals = {}
    var_vals = line[1:-1].split(',')
    for var in var_vals:
        var_spl = var.split('=')
        local_vals.update({var_spl[0]:int(var_spl[1])})
    cur_wf = 'in'
    task_res = False
    # use exec?? ugh
    while(cur_wf != 'A' and cur_wf != 'R'):
        cur_wf_tasks = flow_dic.get(cur_wf)
        for task in cur_wf_tasks:
            if len(task) == 1:
                cur_wf = task[0]
            else:
                task_res = eval(task[0], None, local_vals)
                if task_res:
                    cur_wf = task[1]
                    break
    if cur_wf == 'R':
        return 0
    else:
        return sum(local_vals.values())

if __name__ == '__main__':
    file_name = 'data.txt'
    # file_name = 'data-test.txt'

    f = open(file_name)

    querying = False
    flow_dic = {}

    total = 0
    
    for line in f:
        line = line.strip()
        if not querying and line == '':
            querying = True
        elif not querying:
            add_line(line, flow_dic)
        else:
            total += query_vals(line, flow_dic)

    print(total)  

    f.close()