import unittest
# from solve_with_hint_new_2 import *
from line_solver import *


class FixBoundaries(unittest.TestCase):
    maxDiff = None

    def test_fits_false_1(self):
        lst = ['1', '0', '1', 'u', 'u', 'u', 'u']
        req = [1, 3]
        count = get_counter(lst)
        result = fits(count, req, lst)
        self.assertFalse(result)

    def test_fits_true_1(self):
        lst = ['0', '0', '0', 'u', '1', '1', '1', 'u', 'u', '1', '0', '1', 'u', 'u', 'u', 'u', 'u']
        req = [4, 1, 2, 2, 3, 2]
        count = get_counter(lst)
        print('start string = ', lst)
        result = fits(count, req, lst)
        self.assertTrue(result)

    def test_push_walls_1(self):
        lst = ['1', '0', '1', 'u', 'u', 'u', 'u']
        req = [1, 3]
        right_result = ['1', '0', '1', '1', '1', '0', '0']
        result = mother_of_recursion(lst, req)
        self.assertEqual(result, right_result)

    def test_push_walls_2(self):
        lst = ['1', '0', 'u', '1', 'u', 'u', 'u']
        req = [1, 3]
        right_result = ['1', '0', 'u', '1', '1', 'u', '0']
        result = mother_of_recursion(lst, req)
        self.assertEqual(result, right_result)

    def test_row_2(self):
        lst = ['1', '1', '1', '1', '1', '1', '0', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '0', '0', '1', '1', '0', 'u', 'u',
               'u', 'u', '0', '1', '1', '1', '0', 'u', 'u', 'u', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1',
               'u', 'u', '1', '1', '1', '1', 'u', 'u', 'u', 'u', '0', '1', '1', '1', '0', '0', 'u', 'u', 'u', '1', '1',
               '1', '1', '1', '1', '1', '1', '1', '0', 'u', 'u', 'u', '1', '0', '0', '0', '0', 'u', 'u', 'u', '0', '0',
               '0', '1', '1', '1', '1', 'u', 'u', 'u', 'u', 'u', '0', '1']

        req = [6, 4, 2, 3, 3, 2, 8, 4, 2, 3, 10, 3, 3, 4, 2, 1]
        result = mother_of_recursion(lst[:], req)
        print('former = ', lst)
        print('result = ', lst)

    def test_col_5(self):
        lst = ['1', '1', '1', '0', '0', '0', 'u', '1', '1', '1', 'u', 'u', '1', '0', '1', 'u', 'u', 'u', 'u', 'u', 'u',
               'u', '0', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '1', '1', 'u', 'u', 'u', 'u', 'u', 'u',
               'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '0', 'u', 'u', 'u', 'u', '1', '1', 'u', 'u',
               '1', 'u', 'u', '1', '0', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '1', 'u',
               'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '1']
        req = [3, 4, 1, 2, 2, 3, 2, 5, 3, 4, 1, 3, 2, 1, 1, 6, 1, 2, 2, 4]
        result = mother_of_recursion(lst[:], req)
        print('former = ', lst)
        print('result = ', lst)

    def test_center_both(self):
        lst = ['u', 'u', '1', 'u', 'u']
        req = [5]
        right_result = ['1', '1', '1', '1', '1']
        result = fix_boundaries(lst, req)
        self.assertEqual(result, right_result)

    #
    def test_center_no_sides(self):
        lst = ['u', 'u', '1', 'u', 'u']
        req = [3]
        result = fix_boundaries(lst, req)
        right_result = ['u', 'u', '1', 'u', 'u']
        self.assertEqual(result, right_result)

    #
    def test_wrong_size(self):
        lst = ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '0', '1']
        reqs = [1, 2, 1]
        result = mother_of_recursion(lst, reqs)
        right_result = ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '0', '1']
        self.assertEqual(result, right_result)

    def test_push_walls(self):
        lst = ['1', '0', '0', 'u', 'u', '0', '0', '0', 'u', '1', '1']
        req = [1, 1, 3]
        result = mother_of_recursion(lst, req)
        right_result = ['1', '0', '0', 'u', 'u', '0', '0', '0', '1', '1', '1']
        self.assertEqual(result, right_result)

    def test_fits_bug(self):
        lst = ['u', '0', '1', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u']
        req = [1, 1, 1]
        counter = get_counter(lst)
        self.assertTrue(fits(counter, req, lst))
        # self.assertEqual(mother_of_reursion(lst, req), ['0', '0', '1', '1', '1', '1', '0', 'u'])

    def test_index_bug(self):
        lst = ['0', '0', '0', '0', '0', 'u', '1', 'u', '0', '1', '1']
        right_result = ['0', '0', '0', '0', '0', 'u', '1', 'u', '0', '1', '1']
        req = [2, 2]
        result = mother_of_recursion(lst[:], req)
        self.assertEqual(right_result, result)

    # def test_grow_size(self):
    #     lst = ['u', '1', 'u', 'u', '0', 'u', '1', 'u', '1', 'u', 'u', 'u', '0', '1']
    #     req = [2, 2, 2, 1]
    #     result = mother_of_recursion(lst, req)
    #     right_result = ['u', '1', 'u', '0', '0', 'u', '1', 'u', '1', 'u', 'u', 'u', '0', '1']
    #     self.assertEqual(result, right_result)

    def test_push_walls_1(self):
        lst = ['u', 'u', '1', 'u', 'u', 'u', 'u']
        req = [4]
        right_result = ['u', 'u', '1', '1', 'u', 'u', 'u']
        result = push_walls_fix(lst, req)
        self.assertEqual(result, right_result)

    def test_push_walls_2(self):
        lst = ['1', 'u', 'u', 'u', 'u', 'u', 'u']
        req = [4]
        right_result = ['1', '1', '1', '1', '0', 'u', 'u']
        result = push_walls_fix(lst, req)
        self.assertEqual(result, right_result)

    def test_push_walls_3(self):
        lst = ['0', 'u', 'u', '1', 'u', 'u', 'u']
        req = [4]
        right_result = ['0', 'u', 'u', '1', '1', 'u', 'u']
        result = push_walls_fix(lst, req)
        self.assertEqual(result, right_result)

    def test_push_walls_4(self):
        lst = ['0', '1', 'u', 'u', 'u', 'u', 'u']
        req = [4]
        right_result = ['0', '1', '1', '1', '1', '0', 'u']
        result = push_walls_fix(lst, req)
        self.assertEqual(result, right_result)

    def test_suck_walls_1(self):
        lst = ['u', 'u', 'u', 'u', '1', 'u', 'u']
        req = [4]
        right_result = ['0', 'u', 'u', 'u', '1', 'u', 'u']
        result = suck_walls_fix(lst, req)
        self.assertEqual(result, right_result)

    def test_suck_walls_2(self):
        lst = ['u', 'u', 'u', 'u', '1', '1', '1']
        req = [4]
        right_result = ['0', '0', '0', 'u', '1', '1', '1']
        result = suck_walls_fix(lst, req)
        self.assertEqual(result, right_result)

    def test_suck_walls_3(self):
        lst = ['0', 'u', 'u', 'u', '0', '1', '1', '1', 'u', 'u']
        req = [4]
        right_result = ['0', '0', '0', '0', '0', '1', '1', '1', 'u', 'u']
        result = suck_walls_fix(lst, req)
        self.assertEqual(result, right_result)

    def test_inaccessibility_1(self):
        lst = ['u', 'u', '0', 'u', '1', '1', '1']
        req = [4]
        right_result = ['0', '0', '0', 'u', '1', '1', '1']
        result = inaccessibility_fix(lst, req)
        self.assertEqual(result, right_result)

    def test_inaccessibility_2(self):
        lst = ['u', 'u', 'u', '0', 'u', '1', 'u', 'u']
        req = [4]
        right_result = ['0', '0', '0', '0', 'u', '1', 'u', 'u']
        result = inaccessibility_fix(lst, req)
        self.assertEqual(result, right_result)

    def test_inaccessibility_3(self):
        lst = ['u', 'u', 'u', '0', 'u', '1', 'u', 'u']
        req = [3]
        right_result = ['u', 'u', 'u', '0', 'u', '1', 'u', 'u']
        result = inaccessibility_fix(lst, req)
        self.assertEqual(result, right_result)

    def test_get_intervals_1(self):
        lst = ['0', 'u', 'u', 'u', 'u', 'u', '1', '0', 'u']
        right_result = (['0'], ['u', 'u', 'u', 'u', 'u', '1'], ['0', 'u'])
        result = get_intervals(lst)
        self.assertEqual(result, right_result)

    def test_get_intervals_2(self):
        lst = ['u', 'u', 'u', 'u', 'u', 'u', '1', '0', 'u']
        right_result = ([], ['u', 'u', 'u', 'u', 'u', 'u', '1'], ['0', 'u'])
        result = get_intervals(lst)
        self.assertEqual(result, right_result)

    def test_get_intervals_3(self):
        lst = ['u', 'u', 'u', 'u', 'u', 'u', '1', 'u', 'u']
        right_result = ([], ['u', 'u', 'u', 'u', 'u', 'u', '1', 'u', 'u'], [])
        result = get_intervals(lst)
        self.assertEqual(result, right_result)

    def test_two_req_fit_1(self):
        lst = ['u', 'u', 'u', '0', 'u', 'u', '1', 'u', 'u']
        req = [3, 4]
        result = two_req_fit(lst, req)
        self.assertFalse(result)

    def test_two_req_fit_2(self):
        lst = ['u', 'u', 'u', 'u', 'u', 'u', '1', 'u', 'u']
        req = [3, 4]
        result = two_req_fit(lst, req)
        self.assertTrue(result)

    def test_two_req_fit_3(self):
        lst = ['u', 'u', 'u', 'u', 'u', 'u', '1', 'u']
        req = [3, 4]
        result = two_req_fit(lst, req)
        self.assertTrue(result)

    def test_two_req_fit_4(self):
        lst = ['u', 'u', 'u', 'u', 'u', 'u', '1']
        req = [3, 4]
        result = two_req_fit(lst, req)
        self.assertFalse(result)

    def test_two_req_fit_5(self):
        lst = ['0', 'u', 'u', 'u', 'u', 'u', '1', 'u', 'u']
        req = [3, 4]
        result = two_req_fit(lst, req)
        self.assertTrue(result)

    def test_mother_1(self):
        lst = ['1', '0', '1', '1', '0', 'u', '1', 'u', '1', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u']
        req = [2, 2, 2, 1]
        req = [1, 2, 2, 1, 7]
        result = mother_of_recursion(lst[:], req)
        right_result = ['1', '0', '1', '1', '0', 'u', '1', 'u', '1', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u',
                        'u', 'u']
        # result = mother_of_recursion(result[:], req)
        print(result)
        print(lst)
        self.assertEqual(result, right_result)

    def test_can_connect_1(self):
        lst = ['u', '1', 'u', '1', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u']
        lst = ['0', '1', 'u', '1', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u']
        lst = ['0', 'u', 'u', 'u', '1', 'u', '1', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u']
        req = [2, 1, 7]
        result = can_connect(lst, req)
        self.assertTrue(result)
        print(result)

    def test_can_connect_2(self):
        lst = ['0', 'u', 'u', '1', 'u', '1', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u']
        req = [2, 1, 7]
        result = can_connect(lst, req)
        print('hi')
        new_fit(lst, req)
        self.assertFalse(result)

    # def test_broken_reqs(self):
    #     lst = [
    #         '1', '0', '1', '0', '0', '1', '0', '0', 'u', 'u', 'u', 'u', 'u', '1', '0', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '1', '1', '1', 'u', '0', '1']
    #     wrong_lst = [
    #         '1', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '1', '0', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '1', '1', '1', 'u', '0', '1']
    #     req = [1,1,1,2,3,1,3,2,1,4,2,7,13,9,5,4,1]
    #     self.maxDiff = None
    #     result = mother_of_recursion(lst[:], req)
    #
    #     self.assertEqual(result, wrong_lst)

    # def test_fit_unknown_interval(self):
    #     lst = ['0', '0', 'u', 'u', 'u', 'u', 'u', '1', '0', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '1', '1', '1', 'u', '0', '1']
    #     req = [2, 3, 1, 3, 2, 1, 4, 2, 7, 13, 9, 5, 4, 1]
    #     wrong_lst = ['0', '0', '0', '0', '0', '0', '1', '1', '0', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '1', '1', '1', 'u', '0', '1']
    #     self.maxDiff = None
    #     result = fit_unknown_interval(lst[:], req)
    #     self.assertEqual(result, wrong_lst)

    #    def test_1_to_0(self):
    #        lst = ['u', 'u', '1', '0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1', '1', '1', '0', 'u', '1', '1',
    #         '1', '1', '1', '1', '1', '1', '1', '1', '1', 'u', 'u', 'u', 'u', 'u', '1', '1', '1', '1', '1', '1', 'u', 'u',
    #         'u', 'u', 'u', '1', '1', 'u', 'u', 'u', 'u', '0', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1', '1']
    #        right_result = ['u', 'u', '1', '0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1', '1', '1', '0', 'u', '1', '1',
    #         '1', '1', '1', '1', '1', '1', '1', '1', '1', 'u', 'u', 'u', 'u', 'u', '1', '1', '1', '1', '1', '1', 'u', 'u',
    #         'u', 'u', 'u', '1', '1', 'u', 'u', 'u', 'u', '0', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1', '1']
    #        reqs = [1, 8, 3, 15, 10, 6, 8, 2]
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    # #    lst = ['u', 'u', '1', '1', '1', '0', '1', 'u', 'u', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', 'u',
    # #     'u', 'u', 'u', 'u', '1', '1', '1', 'u', 'u', 'u', 'u', 'u', '1', '1', '1', 'u', 'u', 'u', 'u', 'u', '1', '1', '1',
    # #     '1', '1', '1', 'u', 'u', 'u', 'u', '0', '0', 'u', '1', '1', '1', '1', '1', '1', '1', '1', 'u']
    # #    res[
    # #     'u', 'u', '1', '1', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1', '1', '1', '1', '1', '1', '1', '0', 'u', 'u', 'u', '1', '1', '1', 'u', 'u', 'u', 'u', 'u', '1', '1', '1', 'u', 'u', 'u', 'u', 'u', '1', '1', '1', '1', '1', '1', 'u', 'u', 'u', 'u', '0', '0', 'u', '1', '1', '1', '1', '1', '1', '1', '1', 'u']
    # #    self.req_rows[i]
    # #    [4, 17, 7, 7, 10, 9]
    # #

    def test_fits(self):
        lst = ['0', '0', 'u', 'u', 'u', 'u', '1', '1', '1', '1', '1', '1', 'u', 'u', 'u', 'u', 'u', '1', '1', '1', 'u',
               'u', 'u', 'u', 'u', '1', '1', '1', 'u', 'u', 'u', '0', '1']
        req = [10, 7, 7, 17, 4]
        # IT SHOULD FIT
        counter = get_counter(lst)
        res = fits(counter, req, lst)
        self.assertTrue(res)

    def test_new_fits(self):
        lst = ['u', 'u', '1', '1', '1', '0', '1', 'u', 'u', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
               '1', 'u',
               'u', 'u', 'u', 'u', '1', '1', '1', 'u', 'u', 'u', 'u', 'u', '1', '1', '1', 'u', 'u', 'u', 'u', 'u', '1',
               '1', '1',
               '1', '1', '1', 'u', 'u', 'u', 'u', '0', '0', 'u', '1', '1', '1', '1', '1', '1', '1', '1', 'u']
        reqs = [4, 17, 7, 7, 10, 9]
        right_res = ['0', '1', '1', '1', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
                     '1', '1', '1',
                     '0', 'u', 'u', 'u', '1', '1', '1', '1', 'u', 'u', 'u', 'u', '1', '1', '1', 'u', 'u', 'u', 'u', 'u',
                     '1', '1', '1',
                     '1', '1', '1', 'u', 'u', 'u', 'u', '0', '0', 'u', '1', '1', '1', '1', '1', '1', '1', '1', 'u']
        mom = mother_of_recursion(lst, reqs)
        self.assertEqual(mom, right_res)

    def test_wall_long(self):
        lst = ['u', 'u', 'u', 'u', '1', '1', '1', 'u', 'u', 'u', 'u', 'u']
        reqs = [4]
        right_res = ['0', '0', '0', 'u', '1', '1', '1', 'u', 'u', 'u', 'u', 'u']
        # suck_walls_fix(lst, reqs)
        mom = 1
        mom = suck_walls_fix(lst, reqs)
        # mom = suck_walls_fix(lst, reqs)
        self.assertEqual(mom, right_res)

    def test_wall_short(self):
        lst = ['u', 'u', '1', '1', '1', 'u', 'u', 'u', 'u', 'u']
        reqs = [4]
        reqs = [4, 3]
        right_res = ['0', 'u', '1', '1', '1', 'u', 'u', 'u', 'u', 'u']
        # suck_walls_fix(lst, reqs)
        mom = 1
        mom = mother_of_recursion(lst, reqs)
        # mom = suck_walls_fix(lst, reqs)
        self.assertEqual(mom, right_res)

    # def test_wall_short_2(self):
    #      lst = ['u', 'u', '1', '1', '1', 'u', 'u', 'u', 'u', 'u']
    #      reqs = [4]
    #      right_res = ['0', 'u', '1', '1', '1', 'u', '0', '0', '0', '0']
    #      # suck_walls_fix(lst, reqs)
    #      mom = mother_of_recursion(lst, reqs)
    #      # mom = suck_walls_fix(lst, reqs)
    #      self.assertEqual(mom, right_res)

    # def test_back_wall(self):
    #      lst = ['u', 'u', 'u', '1', '1', '0', 'u', 'u', 'u', 'u']
    #      reqs = [4, 3]
    #      right_res = ['0', '1', '1', '1', '1', '0', 'u', '1', '1', 'u']
    #      # suck_walls_fix(lst, reqs)
    #      # mom = 1
    #      # mom = fix_back(lst, reqs)
    #      mom = mother_of_recursion(lst, reqs)
    #      # mom = suck_walls_fix(lst, reqs)
    #      print('result = ', mom)
    #      self.assertEqual(mom, right_res)

    #     def test_push_0(self):
    #          lst =       ['1', '0', '0', '1', '0', '1', 'u', 'u', 'u', 'u', 'u']
    #          req = [1, 1, 1, 3]
    #          right_res = ['1', '0', '0', '1', '0', '1', '0', 'u', '1', '1', 'u']
    #          self.maxDiff = None
    #          print('start       ', lst)
    #          mom = mother_of_recursion(lst[:], req)
    #          print('start', lst)
    #          print('final', mom)
    # #          req = [1, 1, 3]
    # #          lst = ['0', '0', '1', '0', '1', 'u', 'u', 'u', 'u', 'u']
    # #          counter = get_counter(lst)
    # #          print(fits(counter, req, lst))
    #
    #          self.assertEqual(mom, right_res)

    #    def test_row_3(self):
    #         lst =     ['1', '1', '1', '1', '1', '1', '0', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '0', '0', '1', '1', '0', 'u', 'u', 'u', 'u', '0', '1', '1', '1', '0', 'u', 'u', 'u', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', 'u', 'u', '1', '1', '1', '1', 'u', 'u', 'u', 'u', '0', '1', '1', '1', '0', '0', 'u', 'u', 'u', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', 'u', 'u', 'u', '1', '0', '0', '0', '0', 'u', 'u', 'u', '0', '0', '0', '1', '1', '1', '1', 'u', 'u', 'u', 'u', 'u', '0', '1']
    #         correct =     ['1', '1', '1', '1', '1', '1', '0', 'u', 'u', 'u', '1', 'u', 'u', 'u', '0', '0', '1', '1', '0', 'u', 'u', 'u', 'u', '0', '1', '1', '1', '0', 'u', 'u', 'u', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', 'u', 'u', '1', '1', '1', '1', 'u', 'u', 'u', 'u', '0', '1', '1', '1', '0', '0', 'u', 'u', 'u', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', 'u', 'u', 'u', '1', '0', '0', '0', '0', 'u', 'u', 'u', '0', '0', '0', '1', '1', '1', '1', 'u', 'u', 'u', 'u', 'u', '0', '1']
    #         req = [6, 4, 2, 3, 3, 2, 8, 4, 2, 3, 10, 3, 3, 4, 2, 1]
    #         self.maxDiff = None
    #         # correct = ['1', '1', '1', '1', '1', '1', '0', 'u', 'u', 'u', '1', 'u', 'u', 'u', '0', '0', '1', '1', '0', 'u', '1', '1', 'u', '0', '1', '1', '1', '0', 'u', '1', 'u', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '1', '1', '1', '1', '0', 'u', '1', 'u', '0', '1', '1', '1', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '1', '1', '1', '0', '0', '0', '0', '1', '1', '1', '0', '0', '0', '1', '1', '1', '1', '0', 'u', 'u', 'u', 'u', '0', '1']
    #         result = mother_of_recursion(lst[:], req)
    # #        result = simple_fix(len(lst), '', req, lst)
    #
    #         print(result)
    #         print(''.join(lst))
    #         print(req)
    #         k = 0
    #         for index in range(len(result)):
    #             if lst[index] != result[index]:
    #                 k += 1
    #         print('k=', k)
    # #        self.assertEqual(result, incorrect)
    #         self.assertEqual(result, correct)

    def test_fit_unknown_1(self):
        lst = ['0', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '0', 'u', 'u', 'u', 'u', 'u', 'u', '0', '0',
               'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '1', '1', '1', '1', '1', '1', 'u', 'u', 'u', 'u', 'u',
               '0', 'u', 'u', 'u', 'u', 'u', 'u', '0', 'u', 'u', 'u', 'u', 'u', 'u', '1', '1', '1', '1', '1', '1', '0',
               'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '0', '1', 'u',
               'u', 'u', 'u', 'u', 'u', 'u', '1']
        req = [9, 5, 4, 10, 3, 9, 3, 6, 3, 1, 2, 2]
        result = fit_unknown_interval(lst[:], req)
        print('result', result)

    def test_abundant_ones(self):
        lst = ['1', '1', '1', '1', '1', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '0', 'u', 'u', 'u',
               'u', 'u', 'u', '0', '0', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '1', '1', '1', '1', '1', '1',
               'u', 'u', 'u', 'u', 'u', '0', 'u', 'u', 'u', 'u', 'u', 'u', '0', 'u', 'u', 'u', 'u', 'u', 'u', '1', '1',
               '1', '1', '1', '1', '0', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u',
               'u', 'u', '0', '1', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '1']

        req = [5, 9, 5, 4, 10, 3, 9, 3, 6, 3, 1, 2, 2]
        result = mother_of_recursion(lst[:], req)
        print(result)

    def test_fits_false(self):
        counter = [('1', 1), ('0', 1), ('1', 1), ('u', 62), ('1', 1), ('u', 26), ('1', 2), ('0', 1), ('1', 1)]
        req = [1, 2, 6, 1, 1, 1, 2, 1, 5, 3, 2, 2, 3, 1, 2, 3, 2, 2, 1]
        lst = ['1', '0', '1', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u',
               'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u',
               'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u',
               'u', 'u', '1', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u',
               'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '1', '1', '0', '1']
        result = fits(counter, req, lst)
        print(result)
        self.assertFalse(result)

    def test_row_doesnt_push(self):
        lst = ['1', '0', '1', '1', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u',
               'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '1', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u',
               'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u',
               'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u',
               'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '1', '0', '1']
        req = [1, 2, 2, 3, 2, 1, 3, 2, 2, 3, 5, 1, 2, 1, 1, 1, 6, 2, 1]
        result = mother_of_recursion(lst[:], req)
        incorrect = ['1', '0', '1', '1', '0', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u',
                     'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '1', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u',
                     'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u',
                     'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u',
                     'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '0', '1', '1', '0', '1']
        self.assertEqual(result, incorrect)

    #     def test_push(self):
    #
    #         lst =  ['1', '0', '1', '1', '1', '1', 'u', 'u', 'u', 'u', 'u', 'u', '1', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u',
    #      'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '1', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u',
    #      'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '0', 'u', 'u',
    #      'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u',
    #      '0', '0', '1', '1']
    #         req = [1, 4, 2, 4, 1, 1, 2, 6, 2, 1, 5, 1, 2, 3, 1, 7, 2]
    #         result = mother_of_recursion(lst[:], req)
    #         print(result)

    # def test_error_1(self):
    #
    #     lst = ['1', '1', '1', '1', '1', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '0', 'u', 'u', 'u', 'u', 'u',
    #  'u', '0', '0', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '1', '1', '1', '1', '1', '1', 'u', 'u', 'u', 'u',
    #  'u', '0', 'u', 'u', 'u', 'u', 'u', 'u', '0', 'u', 'u', 'u', 'u', 'u', 'u', '1', '1', '1', '1', '1', '1', '0', 'u',
    #  'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '0', '1', 'u', 'u', 'u', 'u',
    #  'u', 'u', 'u', '1']
    #     req = [5, 9, 5, 4, 10, 3, 9, 3, 6, 3, 1, 2, 2]
    #     wrong = ['1', '1', '1', '1', '1', '0', 'u', 'u', '1', '1', '1', '1', '1', '1', '1', 'u', 'u', '0', 'u', '1', '1', '1', '1', 'u', '0', '0', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '1', '1', '1', '1', '1', '1', 'u', 'u', 'u', 'u', 'u', '0', 'u', 'u', 'u', 'u', 'u', 'u', '0', 'u', 'u', 'u', 'u', 'u', 'u', '1', '1', '1', '1', '1', '1', '0', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '0', '1', 'u', 'u', 'u', 'u', 'u', '0', '1', '1']
    #     result = mother_of_recursion(lst[:], req)
    #     print(result)

    # def test_suck_wall_1(self):
    #     lst = ['1', '0', '1', '0', 'u', 'u', '1', 'u', 'u', 'u', 'u', 'u', 'u']
    #     req = [1, 1, 2]
    #     result = mother_of_recursion(lst[:], req)
    #     print(result)

    def test_void(self):
        lst = ['1', '1', '1', '0', '0', 'u', '0', 'u', '1', '0', '0', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u',
               'u', 'u', 'u', '0', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '1', '1', 'u', 'u', 'u', '1', '1', 'u',
               'u', '1', '0', '1', 'u', '1', '1', 'u', '1', '1', '0', '0', 'u', '1', '0', 'u', 'u', 'u', 'u', 'u', 'u',
               'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '1', '1', 'u', 'u', 'u', 'u', 'u', 'u', '0', 'u', '1', '1',
               'u', 'u', 'u', 'u', 'u', 'u', '1', '1', 'u', '0', '1', '1']

        req = [3, 2, 4, 3, 11, 5, 4, 2, 2, 2, 3, 6, 3, 2]

        right_result = ['1', '1', '1', '0', '0', '0', '0', '1', '1', '0', '0', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u',
                        'u', 'u', 'u', 'u', 'u', '0', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '1', '1', 'u', 'u',
                        'u', '1', '1', 'u', 'u', '1', '0', '1', 'u', '1', '1', 'u', '1', '1', '0', '0', 'u', '1', '0',
                        'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '1', '1', 'u', 'u',
                        'u', 'u', 'u', 'u', '0', 'u', '1', '1', 'u', 'u', 'u', 'u', 'u', 'u', '1', '1', 'u', '0', '1',
                        '1']
        self.maxDiff = None
        result = mother_of_recursion(lst[:], req)
        print('start ', lst)
        print('result', result)
        self.assertEqual(result, right_result)

    # def test_col_unk(self):
    #     lst = ['1', '1', '0', '1', '1', '0', '0', '0', 'u', '0', '1', '1', '1', '1', 'u', '0', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '0', '1', '0', '0', '1']
    #     req = [2, 2, 1, 4, 7, 11, 4, 1, 1, 3, 3, 9, 1, 4, 1, 2]
    #     result = mother_of_recursion(lst[:], req)
    #     right_result = lst = ['1', '1', '0', '1', '1', '0', '0', '0', 'u', '0', '1', '1', '1', '1', 'u', '0', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '0', '1', '0', '0', '1']
    #     print('start ', lst)
    #     print('result', result)
    #     self.assertEqual(result, right_result)

    def test_col_80(self):
        lst = ['1', '0', '1', '0', '0', '1', '0', '0', 'u', 'u', 'u', 'u', 'u', '1', '0', 'u', 'u', 'u', 'u', 'u', 'u',
               'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u',
               'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u',
               'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u',
               'u', 'u', 'u', 'u', 'u', 'u', '1', '1', '1', 'u', '0', '1']
        wrong = ['1', '0', '1', '0', '0', '1', '0', '0', 'u', 'u', 'u', 'u', 'u', '1', '0', 'u', 'u', 'u', 'u', 'u',
                 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u',
                 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u',
                 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u',
                 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', '1', '1', '1', 'u', '0', '1']
        req = [1, 1, 1, 2, 3, 1, 3, 2, 1, 4, 2, 7, 13, 9, 5, 4, 1]
        result = mother_of_recursion(lst[:], req)
        print('start ', lst)
        print('result', result)
        self.assertEqual(result, wrong)


if __name__ == '__main__':
    unittest.main()
