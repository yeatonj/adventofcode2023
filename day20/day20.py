# File for day 20 of AoC 2023
# Written by Joshua Yeaton on 1/3/2024

import queue

def process_input(file_name):
    module_dic = {}

    # First, add each module
    f = open(file_name)
    for line in f:
        line = line.strip()
        spl_line = line.split(' -> ')
        module_details = {}
        if spl_line[0][0] == '%' or spl_line[0][0] == '&':
            module_details.update({'type':spl_line[0][0], 'out':[], 'in':{}, 'cur_val':0})
            module_dic.update({spl_line[0][1:]:module_details})
        else:
            module_details.update({'type':'b', 'out':[]})
            module_dic.update({'broadcaster':module_details})
    f.close()

    # Then, assign inputs and outputs
    f = open(file_name)
    for line in f:
        line = line.strip()
        spl_line = line.split(' -> ')
        cons = spl_line[1]
        cons = cons.split(',')
        if spl_line[0][0] == '%' or spl_line[0][0] == '&':
            temp_out = module_dic.get(spl_line[0][1:]).get('out')
            for con in cons:
                con = con.strip()
                temp_out.append(con)
                if con not in module_dic:
                    module_dic.update({con:{'type':'', 'out':[], 'in':{}}})
                temp_in = module_dic.get(con).get('in')
                cur_ins = len(temp_in)
                temp_in.update({spl_line[0][1:]:(2**(cur_ins))})
        else:
            temp_out = module_dic.get('broadcaster').get('out')
            for con in cons:
                con = con.strip()
                temp_out.append(con)
    f.close()
    # Finally, assign extra details to the conjunction modules
    for module in module_dic:
        module_details = module_dic.get(module)
        if module_details.get('type') == '&':
            max_val = 2**(len(module_details.get('in'))) - 1
            module_details.update({'max_in':max_val})
    return module_dic

# simulates a button press
def press_button(modules, presses):
    low_sent = 1 # accounts for initial button press
    high_sent = 0
    module_queue = queue.SimpleQueue()
    init_outs = modules.get('broadcaster').get('out')
    for out in init_outs:
        module_queue.put((out, 0, 'broadcaster'))
    
    # counter = 0
    while (not module_queue.empty()):
        # print(counter)
        # counter += 1
        cur_signal = module_queue.get()
        if cur_signal[1] == 0:
            low_sent += 1
        else:
            high_sent += 1
        process_signal(modules, module_queue, cur_signal, presses)

    return (low_sent, high_sent)

# Processes a signal to a module
def process_signal(modules, module_queue, cur_signal, presses):
    signaled_module = cur_signal[0]
    signal = cur_signal[1]
    if signaled_module == 'rx' and signal == 0:
        print('done, with ' + str(presses) + ' presses.')
        exit()
    signal_from = cur_signal[2]
    mod_type = modules.get(signaled_module).get('type')
    # print(mod_type)
    if mod_type == '':
        return
    elif mod_type == '%':
        if signal == 1:
            return
        # we flip the current bit and send that as a signal
        cur_bit = modules.get(signaled_module).get('cur_val')
        new_bit = int(not cur_bit)
        modules.get(signaled_module).update({'cur_val':new_bit})
        for sig_mod in modules.get(signaled_module).get('out'):
            module_queue.put((sig_mod, new_bit, signaled_module))
    else:
        # We have a conjunction module
        sig_power = modules.get(signaled_module).get('in').get(signal_from)
        max_in = modules.get(signaled_module).get('max_in')
        if signal == 0:
            temp = max_in - sig_power
            new_val = modules.get(signaled_module).get('cur_val') & temp
        else:
            new_val = modules.get(signaled_module).get('cur_val') | sig_power
        modules.get(signaled_module).update({'cur_val':new_val})
        # now, signal the outputs if necessary
        if max_in & new_val == max_in:
            # signal with 0
            for sig_mod in modules.get(signaled_module).get('out'):
                module_queue.put((sig_mod, 0, signaled_module))
        else:
            # signal with 1
            for sig_mod in modules.get(signaled_module).get('out'):
                module_queue.put((sig_mod, 1, signaled_module))
    # print()
    return 

if __name__ == '__main__':
    file_name = 'data.txt'
    # file_name = 'data-test.txt'

    modules = process_input(file_name)

    # for mod in modules:
    #     print(modules.get(mod))

    # PART 1 -----------------------------
    # total_low = 0
    # total_high = 0
    # for i in range(1000):
    #     (low_sent, high_sent) = press_button(modules, i)
    #     total_low += low_sent
    #     total_high += high_sent
    # print(total_low)
    # print(total_high)
    # solution = total_high * total_low
    # print('Solution is: ' + str(solution))

    # PART 2 --------------------------
    i = 0
    while(True):
        i += 1
        if i % 10000 == 0:
            print('Iteration: ' + str(i))
        (low_sent, high_sent) = press_button(modules, i)