from itertools import zip_longest
MAGIC_NUMBER = 30


def subtract_req(lst, reqs):
    counter = get_counter(lst)
    reqs_used = []
    for pair in counter:
        if pair[0] == '1':
            reqs_used.append(pair[1])
    reqs_used = sorted(reqs_used, reverse=True)
    reqs = sorted(reqs, reverse=True)
    left_reqs = []

    while len(reqs) < len(reqs_used):
        reqs_used[1] += reqs_used[0]
        reqs_used.pop(0)

    for k in zip_longest(reqs, reqs_used, fillvalue=0):
        difference = k[0] - k[1]
        if difference:
            left_reqs.append(difference + 0.5)
    return left_reqs


def get_intervals(lst):
    counter = get_counter(lst)
    intervals_lst = lst[:]
    zeros_length = 0
    if counter[0][0] == '0':
        zeros_length = counter[0][1]
        intervals_lst = lst[zeros_length:]
    if '0' not in lst:
        return [], lst, []

    # print(lst[:lst.index('0')], lst[lst.index('0'):])
    if '0' in intervals_lst:
        return lst[:zeros_length], intervals_lst[:intervals_lst.index('0')], intervals_lst[intervals_lst.index('0'):]
    return lst[:zeros_length], intervals_lst, []


def req_fit_interval(lst, req):
    try:
        _, lst_cut, interval_2 = get_intervals(lst[:])
        if not lst_cut:
            return lst
    except TypeError:
        return lst
    counter = get_counter(lst_cut)
    acc_counter = accumulate_counter(counter)
    for index, pair in enumerate(acc_counter):
        if pair[0] == '1':
            if acc_counter[index - 1][1] > req[0]:
                return False
            if counter[index][1] > req[0]:
                return True
    return True


def two_req_fit(lst, req):
    interval_0, interval_1, interval_2 = get_intervals(lst[:])
    if len(req) == 1 and len:
        return False
    if len(interval_1) >= req[0] + 1 + req[1]:
        return True
    return False


def req_fit_next_interval(lst, req):
    interval_0, interval_1, interval_2 = get_intervals(lst[:])
    if not interval_2:
        return False
    if len(interval_2) < req[0]:
        return True
    _, interval_2, _ = get_intervals(interval_2[:])
    if '1' in interval_2:
        counter = get_counter(interval_2)
        num = 0
        for pair in counter:

            if pair[0] == '1':
                if len(pair) <= req[0]:
                    return True
                if num - 1 >= req[0]:
                    return True
            num += pair[1]
    return False


def can_connect(lst, req):
    interval_0, interval_1, interval_2 = get_intervals(lst)
    print(interval_1)
    counter = get_counter(interval_1)
    adv = accumulate_counter(counter)
    if counter[0][0] == 'u' and counter[0][1] > req[0]:
        return True

    interval_started = False
    length = 0
    for index, pair in enumerate(counter):
        print(pair)
        if pair[0] == '1':
            length += pair[1]
            if interval_started:
                break
            interval_started = True
        #         if '> req[0]
        elif interval_started:
            length += pair[1]
    print(counter)
    print(adv)
    if length > req[0]:
        return False


def fit_unknown_interval(lst, req):
    interval_0, interval_1, interval_2 = get_intervals(lst[:])
    if two_req_fit(lst[:], req):
        return lst
    if '1' not in interval_1:
        return lst
    interval_1 = simple_fix(len(interval_1), '', [req[0]], interval_1)
    return interval_0 + list(interval_1) + interval_2


def new_fit(lst, req):
    if len(req) == 1 or can_connect(lst[:], req) is True:
        return lst
    interval_0, interval_1, interval_2 = get_intervals(lst)
    print(f'{interval_0=} {interval_1=} {interval_2=}')
    if len(interval_1) == req[0]:
        return lst
    counter = get_counter(interval_1)
    if [i[0] for i in counter].count('1') == 1:
        return lst
    adv_counter = accumulate_counter(counter)
    for index, pair in enumerate(adv_counter):
        if pair[0] == '1':
            print(interval_1[:adv_counter[index + 1][1]])
            fit_interval = interval_1[:adv_counter[index + 1][1]]
            break
    if counter[index + 1][1] != 1:
        return lst
    print(f'{fit_interval=}')
    res = (simple_fix(len(fit_interval), '', [req[0]], fit_interval))
    # print(lst)
    print('list ', list(res))
    # print(interval_0 + list(res) + interval_1[adv_counter[index+1][1]:])
    return interval_0 + list(res) + interval_1[adv_counter[index + 1][1]:] + interval_2


def fits(counter, req, string):
    if len(req) == 1:
        return True
    nums = req[0] + 1 + req[1]
    start_index = 0
    if counter[0][0] == '0':
        start_index = counter[0][1]
    number = 0
    for index, pair in enumerate(counter):
        if start_index and index == 0 and pair[0] == '0':
            continue
        if pair[0] == '0':
            if '1' not in string[:start_index + number]:
                return True
            return nums <= number
        number += pair[1]
    return nums <= number


def get_counter(lst):
    num = 0
    element = ''
    results = []
    for item in lst:
        if item != element:
            results.append((element, num))
            element = item
            num = 1
            continue
        num += 1
    if element and num:
        results.append((element, num))

    return results[1:]


def accumulate_counter(counter):
    sum_result = -1
    new_counter = []
    for k in counter:
        sum_result += k[1]
        new_counter.append([k[0], sum_result])
    return new_counter


def sum_req(requirements):
    res = 0
    for k in requirements:
        # res += (k - 2)
        # res += (1.05 * k + 0.9)
        res += (k + 0.9)
    # res -= hint.count('1')
    # res -= hint.count('0')
    return res


def fix_back(string, req):
    counter = get_counter(string)
    f = fits(counter, req, string)
    reqs = req[:]
    reqs.append(0)
    #    print('fits', f, counter, req, string)
    if not f:
        for index, k in enumerate(counter):
            if k[0] == '1':
                length = k[1]
                try:
                    if counter[index + 1][0] != '0':
                        return string
                    #                    print('index > 0', index > 0, counter[index - 1])
                    if index > 0 and counter[index - 1][0] == '0':
                        return string

                    if index > 0 and counter[index - 1][0] == 'u':
                        #                        print('in index')
                        if counter[index - 1][1] > reqs[0] + 1 + reqs[1]:
                            return string
                    # string = (string[:string.index('1') - length] * ['0'] +
                    # string[string.index('1') - length:string.index('1') - length:string.index('1') - length + req[0]] * ['1'] + string[string.index('1') - length + req[0]:])
                    # print(len(string))
                    # print('zeros = ', string.index('1') - req[0] + length)
                    # print('ones', req[0])
                    # print(len(string[string.index('1') + length + req[0]:]))
                    # print((string[string.index('1') - length + req[0]:]))
                    if '0' in string[string.index('1') + length - req[0]:string.index('1') + length]:
                        return string
                    string = (string.index('1') - req[0] + length) * ['0'] + req[0] * ['1'] + string[string.index(
                        '1') + length:]
                    #                    print('after if')
                    #                    print(len(string))
                    return string
                    break
                except IndexError:
                    return string
                break
    return string


def fix_boundaries(string, req):
    if '1' in string:
        if string.index('1') < req[0]:
            length = req[0] - string.index('1')
            string[string.index('1'):req[0]] = ['1'] * length

    else:
        return str(string)
    string = string[::-1]
    if string.index('1') < req[-1]:
        length = req[-1] - string.index('1')
        string[string.index('1'):req[-1]] = ['1'] * length
    string = string[::-1]
    return string


def fix_boundaries_copy(string, req):
    if '1' in string:
        if string.index('1') < req[0]:
            length = req[0] - string.index('1')
            string[string.index('1'):req[0]] = ['1'] * length

    # else:
    #     return str(string)
    if '0' in string and string.index('0') < req[0]:
        length = string.index('0')
        string[:string.index('0')] = ['0'] * length

    # string = string[::-1]
    # if string.index('1') < req[-1]:
    #     length = req[-1] - string.index('1')
    #     string[string.index('1'):req[-1]] = ['1'] * length
    # string = string[::-1]
    return string


def inaccessibility_fix(string, req):
    if '0' in string and string.index('0') < req[0]:
        # print('in adc')
        biggest_index = 0
        for index, k in enumerate(string):
            if k == '0' and index < req[0]:
                biggest_index = index
        length = biggest_index
        # length = string.index('0')
        string[:biggest_index] = ['0'] * biggest_index
        # string[:string.index('0')] = ['0'] * length
    return string


def suck_walls_fix(string, req):
    counter = get_counter(string)
    adv_counter = accumulate_counter(counter)
    # print(counter)
    length_of_zero = 0
    if counter[0][0] == '0':
        length_of_zero = counter[0][1]
    interval_0, interval_1, interval_2 = get_intervals(string)
    # print(interval_0, interval_1, interval_2)
    if len(interval_1) < req[0]:
        return interval_0 + ['0'] * len(interval_1) + interval_2

    if '1' in string and string.index('1') <= (req[0] + length_of_zero):
        length = 0
        for k in counter:
            if k[0] == '1':
                length = string.index('1') - (req[0] - k[1])
                break
        if length > 0:
            res = ['0'] * length + string[length:]
            return res
    return string


def push_walls_fix(string, req):
    # print(req)
    if '1' in string:
        start_index = 0
        if '0' in string and string.index('0') < req[0]:
            # print('in push', string, req)
            counter = get_counter(string)
            # print(counter)
            start_index = counter[0][1]

        if string.index('1') < req[0] + start_index:
            # print('in push', string, req)
            # print('string index', string.index('1'), req[0], start_index)
            length = req[0] - string.index('1') + start_index
            # print(length)
            string[string.index('1'):string.index('1') + length] = ['1'] * length
            if length == req[0]:
                try:
                    string[start_index + length] = '0'
                except IndexError:
                    pass

    return string


# def fix_both_bounds(string, req):
#     forward_string = fix_boundaries_copy(string, req)
#
#
#     whole_string = fix_boundaries_copy(forward_string[::-1], req[::-1])
#     print('backward res', forward_string)
#     return whole_string[::-1]

def mother_of_recursion(string, reqs):
    # going = True
    if '1' not in string:
        return string
    string = recursive_boundary_fix(string, reqs)
    # print('forward res              ', string)
    #    print('before backwards')
    #     print('before backwards')
    #     print('before backwards')
    #     print('before backwards')
    #     print('before backwards')
    #    print('before backwards')
    #    print('before backwards')
    # print(string)

    string = recursive_boundary_fix(string[::-1], reqs[::-1])
    # return string
    return string[::-1]

    # while going:
    #     string = inaccessibility_fix(string, req)
    #     string = push_walls_fix(string, req)
    #     count = get_counter(string)
    pass


def grandmother(string, reqs):
    old_count = string.count('u')
    new_count = 0
    while old_count != new_count:
        old_count = string.count('u')
        string = mother_of_recursion(string, reqs)
        new_count = string.count('u')
    return string


def recursive_boundary_fix(string, req):
    #    print()
    #    print(f'recursive boundary {string=} \n {req=}')
    string = inaccessibility_fix(string, req)
    #    print('                  inadcc ', string)
    string = push_walls_fix(string, req)
    #    print('                    push ', string)
    string = suck_walls_fix(string, req)
    #    print('                    suck ', string)
    string = fix_back(string, req)
    #    print('                    back ', string)

    #    string_new = fit_unknown_interval(string[:], req)
    #    print('     fit unknown_interval', string)

    #    if string_new != string:
    #        print('NOT EQUALS')
    # string = new_fit(string[:], req)
    # print(' new fit unknown_interval', string)

    # if fit_unknown_interval(string, req):
    #     pass
    #    print()
    counter = get_counter(string)
    # print('normal before', counter)
    f = fits(counter, req, string)
    #    print('fits = ', f)
    if len(req) == 1 or f:
        # print('fits')
        return string
    # print('not fits')
    start = True
    acc_counter = accumulate_counter(counter)
    counter_index = 0
    if acc_counter[0][0] == '1' or acc_counter[0][0] == '0':
        start = False
        counter_index = 1
    for index, pair in enumerate(acc_counter[counter_index:]):

        if start and pair[0] == '1':
            start = False
            continue
        if pair[0] == '0':
            # print('pair', pair, start)
            if start:
                start = False
                continue
            try:
                # print('using recursion')
                # return_val = string + recursive_boundary_fix(string[pair[1]+1:], req[1:])
                rec_index = acc_counter[counter_index + index - 1][1] + 1
                return_val = string[:rec_index] + recursive_boundary_fix(string[rec_index:], req[1:])
                return return_val
            except IndexError:
                # print('ret val error')
                return string
    return string


def fix0(length, s, d, output_lst, hint, req_sum, dict_of_res):
    if not d and '1' in hint[-length:]:
        return
    if not d:
        s = s + '0' * length
        return my_new_fix(0, s, d, output_lst, hint, True, req_sum, dict_of_res)

    s = s + '0'
    return my_new_fix(length - 1, s, d, output_lst, hint, True, req_sum, dict_of_res)


def fix1(length, s, d, output_lst, hint, req_sum, dict_of_res):
    s = s + '1' * d[0]
    d = d[:]
    req_sum -= (d[0] + 1)
    el = d.pop(0)
    return_val = my_new_fix(length - el, s, d, output_lst, hint, False, req_sum, dict_of_res)
    return return_val


def string_letter_and(string1, string2):
    return ''.join([string1[i] if string1[i] == string2[i] else 'u' for i in range(len(string1))])


def fix0_simple(length, s, d, hint):
    if not d and '1' in hint[-length:]:
        return

    s = s + '0'
    return simple_fix(length - 1, s, d, hint, True)


def fix1_simple(length, s, d, hint):
    s = s + '1' * d[0]
    d = d[:]
    el = d.pop(0)
    return_val = simple_fix(length - el, s, d, hint, False)
    return return_val


def simple_fix(length, res_string, req_lst, hint, last_el_0=True):
    # dict_of_res = {}
    req_sum = sum([i + 1 for i in req_lst]) - 1
    if length == 0:
        return res_string

    val1 = val2 = None
    if length > req_sum and hint[-length] != '1':
        #        print('fix 0', length)
        val1 = fix0_simple(length, res_string, req_lst, hint)
    if req_lst and last_el_0:
        start = -length
        end = -length + req_lst[0]
        interval = hint[start:end]
        if not end:
            interval = hint[start:]
        if '0' not in interval:
            val2 = fix1_simple(length, res_string, req_lst, hint)
    if val1 and val2:
        return_val = string_letter_and(val1, val2)
        return return_val
    return_val = val1 or val2
    return return_val


def my_new_fix(length, res_string, req_lst, output_lst, hint, last_el_0, req_sum=0, dict_of_res={}):
    # dict_of_res = {}
    # req_tuple =
    dic_key = (tuple(req_lst), ''.join(hint[-length:]), last_el_0)
    if length == 0:
        return res_string

    if length < MAGIC_NUMBER and dic_key in dict_of_res:
        return res_string + dict_of_res[dic_key]
    val1 = val2 = None
    if length > req_sum and hint[-length] != '1':
        val1 = fix0(length, res_string, req_lst, output_lst, hint, req_sum, dict_of_res)
    if req_lst and last_el_0:
        start = -length
        end = -length + req_lst[0]
        interval = hint[start:end]
        if not end:
            interval = hint[start:]

        if '0' not in interval:
            val2 = fix1(length, res_string, req_lst, output_lst, hint, req_sum, dict_of_res)
    if val1 and val2:
        return_val = string_letter_and(val1, val2)
        if length < MAGIC_NUMBER:
            dict_of_res[dic_key] = return_val[-length:]
        return return_val
    return_val = val1 or val2
    if length < MAGIC_NUMBER and return_val:
        dict_of_res[dic_key] = return_val[-length:]
    return return_val


def get_line_with_hint(length, req, dict_of_res, hint):
    if hint.count('u') == 0:
        return hint
    all_lines = []
    req_sum = sum([i + 1 for i in req]) - 1
    res = my_new_fix(length, '', req, all_lines, hint, True, req_sum, dict_of_res)
    return res
