class Solution:
    def __init__(self):
        self.row_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}
        self.col_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}
        self.box_dict = {'00': [], '01': [], '02': [], '10': [], '11': [], '12': [], '20': [], '21': [], '22': []}
        self.full_set = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        self.not_dict = dict()
        self.process_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}
        self.current_entry = ''
    
    def deepcopy_dict(self, dict_obj):

        temp = dict()
        for x in list(dict_obj.keys()):

            if isinstance(dict_obj[x], list):    
                temp[x] = [i for i in dict_obj[x]]
            elif isinstance(dict_obj[x], set):
                temp[x] = {j for j in dict_obj[x]}

        return temp

    def deepcopy_list(self, list_obj):
        temp = []
        for x in list_obj:
            if isinstance(x, list):
                temp.append([i for i in x])

        return temp

    
    def solveCurrent(self, board):
        #print(f'CURRENT ENTRY -- {self.current_entry}')
        #print(f'ROW_DICT -- {self.row_dict}\n\nCOLL -- {self.col_dict}\n\nBBBBOXX -- {self.box_dict}')
        # init_process_dict = self.deepcopy_dict(self.process_dict)
        # init_not_dict = self.deepcopy_dict(self.not_dict)
        
        # init_row_dict = self.deepcopy_dict(self.row_dict)
        # init_col_dict = self.deepcopy_dict(self.col_dict)
        # init_box_dict = self.deepcopy_dict(self.box_dict)
        while self.process_dict[0]:
            for elem in self.process_dict[0]:
                val = list(self.not_dict[f'{elem[0]}{elem[1]}'])[0]
                if val in self.row_dict[int(elem[0])] or val in self.col_dict[int(elem[1])] or val in self.box_dict[f'{int(int(elem[0])/3)}{int(int(elem[1])/3)}']:
                    #print(f'CURRENT ENTRY FAILED -- {self.current_entry} ----- for elem {elem} --- {val}')
                    # self.process_dict = self.deepcopy_dict(init_process_dict)
                    # self.not_dict = self.deepcopy_dict(init_not_dict)
                    # self.row_dict = self.deepcopy_dict(init_row_dict)
                    # self.col_dict = self.deepcopy_dict(init_col_dict)
                    # self.box_dict = self.deepcopy_dict(init_box_dict)
                    return False
                self.row_dict[int(elem[0])].append(val)
                self.col_dict[int(elem[1])].append(val)
                self.box_dict[f'{int(int(elem[0])/3)}{int(int(elem[1])/3)}'].append(val)
                board[int(elem[0])][int(elem[1])] = val
                del self.not_dict[f'{elem[0]}{elem[1]}']

            
            # print('Printing In Between --')
            # for x in board:
                # print(x)
            self.process_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}

            for i in range(9):
                for j in range(9):
                    curr_val = board[i][j]
                    if curr_val == '.':
                        curr_set = set(self.row_dict[i] + self.col_dict[j] + self.box_dict[f'{int(i/3)}{int(j/3)}'])
                        curr_ops = self.full_set - curr_set
                        if len(curr_ops) == 0:
                            # self.process_dict = self.deepcopy_dict(init_process_dict)
                            # self.not_dict = self.deepcopy_dict(init_not_dict)
                            # self.row_dict = self.deepcopy_dict(init_row_dict)
                            # self.col_dict = self.deepcopy_dict(init_col_dict)
                            # self.box_dict = self.deepcopy_dict(init_box_dict)
                            return False
                        self.process_dict[len(curr_ops) - 1].append(f'{i}{j}')
                        self.not_dict[f'{i}{j}'] = curr_ops

            int_process_dict = self.deepcopy_dict(self.process_dict)
            int_not_dict = self.deepcopy_dict(self.not_dict)
            int_board = self.deepcopy_list(board)

            int_row_dict = self.deepcopy_dict(self.row_dict)
            int_col_dict = self.deepcopy_dict(self.col_dict)
            int_box_dict = self.deepcopy_dict(self.box_dict)

            if not self.process_dict[0] and self.not_dict:

                for p in range(1, 9):
                    #print(f'BEFORE ENTERING -- {self.process_dict} --- {self.not_dict}')
                    #print(f'BEFORE ENTERING')
                    process_dict_p = int_process_dict[p]
                    if process_dict_p:
                        for q in process_dict_p:

                            self.process_dict[0] = [q]
                            self.process_dict[p] = list(set(process_dict_p) - {q})
                            temp_process_dict = self.deepcopy_dict(self.process_dict)
                            # print(f'PROCESSING ----- Q - {q} \n CURRENT NOT DICT -- {int_not_dict[q]}')
                            
                            for r in int_not_dict[q]:
                                
                                self.not_dict[q] = {r}
                                self.current_entry = f'{q} : {r} : {int_not_dict[q]}'
                                # print(f'NOT DICT -- {self.not_dict}\nPROCESS DICT -- {self.process_dict}')
                                board = self.solveCurrent(board)
                                if board:
                                    return board
                                else:
                                    board = self.deepcopy_list(int_board)
                                    self.not_dict = self.deepcopy_dict(int_not_dict)
                                    self.process_dict = self.deepcopy_dict(temp_process_dict)
                                    self.row_dict = self.deepcopy_dict(int_row_dict)
                                    self.col_dict = self.deepcopy_dict(int_col_dict)
                                    self.box_dict = self.deepcopy_dict(int_box_dict)

                            # self.process_dict = self.deepcopy_dict(init_process_dict)
                            # self.not_dict = self.deepcopy_dict(init_not_dict)
                            # self.row_dict = self.deepcopy_dict(init_row_dict)
                            # self.col_dict = self.deepcopy_dict(init_col_dict)
                            # self.box_dict = self.deepcopy_dict(init_box_dict)
                            return False
                        


            # print(f'Print process_dict -- {self.process_dict}')
            # print(f'Print not_dict -- {self.not_dict}')
        # print('PRINTING BOARD')
        # for x in board:
        #     print(' '.join(x))
        
        return board

    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """  
        for i in range(9):
            for j in range(9):
                curr_val = board[i][j]
                if curr_val != '.':
                    self.row_dict[i].append(curr_val)
                    self.col_dict[j].append(curr_val)
                    self.box_dict[f'{int(i/3)}{int(j/3)}'].append(curr_val)
                else:
                    self.not_dict[f'{i}{j}'] = '.'

        for i in range(9):
            for j in range(9):
                curr_val = board[i][j]
                if curr_val == '.':
                    curr_set = set(self.row_dict[i] + self.col_dict[j] + self.box_dict[f'{int(i/3)}{int(j/3)}'])
                    curr_ops = self.full_set - curr_set

                    if len(curr_ops) == 0:
                        return False
                    self.process_dict[len(curr_ops) - 1].append(f'{i}{j}')
                    self.not_dict[f'{i}{j}'] = curr_ops
        
        # print(self.process_dict)
        final_board = self.solveCurrent(board)
        #print(f'FFFFFFFF ---- {self.not_dict}')
        return final_board

board = [["8",".",".","7",".","3","1",".","4"],[".",".",".",".",".",".",".","7","."],[".",".","9","2",".",".",".",".","."],["4",".",".",".",".","1","6",".","3"],[".",".",".",".",".",".",".",".","5"],[".","8",".",".","4",".",".",".","."],[".","2",".","3",".",".","7",".","6"],["6",".",".",".",".",".",".","5","."],[".",".",".",".",".","7",".","8","."]]
# print('Printing Initial')
for x in board:
    print(' '.join(x))
solved_board = Solution().solveSudoku(board)
print('\n\n')
#print(solved_board)
for x in solved_board:
    print(' '.join(x))