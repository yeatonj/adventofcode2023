# File for day 19 of AoC 2023
# Written by Joshua Yeaton on 1/3/2024

def add_line(line, flow_dic):
    line_segs = line[0:-1].split('{')
    flow_name = line_segs[0]
    flows = line_segs[1].split(',')
    actual_flows = []
    for flow in flows:
        actual_flow = flow.split(':')
        actual_flows.append(actual_flow)
    flow_dic.update({flow_name:actual_flows})

def query_vals(line, flow_dic):
    # !! update this to populate the values
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
    file_name = 'data-test.txt'

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

    print('Part 1 solution is: ' + str(total))

    accept_nodes = []
    reject_nodes = []
    reverse_flow_dic = {}

    # Now we need to reverse the tree - how do we get from a leaf to 'in'?
    for entry in flow_dic:
        temp = flow_dic.get(entry)
        for index, val in enumerate(temp):
            if 'A' in val:
                accept_nodes.append((entry, index))
            if 'R' in val:
                reject_nodes.append((entry, index))
            if len(val) == 2 and val[1] not in 'AR':
                if val[1] not in reverse_flow_dic:
                    reverse_flow_dic.update({val[1]:[(entry, index)]})
                else:
                    cur_val = reverse_flow_dic.get(val[1])
                    cur_val.append((entry, index))
                    reverse_flow_dic.update({val[1]:cur_val})
            elif len(val) == 1 and val[0] not in 'AR':
                if val[0] not in reverse_flow_dic:
                    reverse_flow_dic.update({val[0]:[(entry, index)]})
                else:
                    cur_val = reverse_flow_dic.get(val[0])
                    cur_val.append((entry, index))
                    reverse_flow_dic.update({val[0]:cur_val})
    
    
    # print(accept_nodes)
    # print(reject_nodes)
    # print(reverse_flow_dic)

    for fin_node in accept_nodes:
        cur_node = fin_node
        print(cur_node, end=' (P)')
        while (cur_node != ('in', 0)):
            node_name = cur_node[0]
            node_num = cur_node[1]
            if node_num > 0:
                while (node_num > 0):
                    next_node = (node_name, node_num - 1)
                    node_num -= 1
                    cur_node = next_node
                    print(' <- ', end='')
                    print(cur_node, end=' (F)')
            else:
                next_node = reverse_flow_dic.get(node_name)[0]
                cur_node = next_node
                print(' <- ', end='')
                print(cur_node, end=' (P)')
            
        print()
        print()
    

    f.close()