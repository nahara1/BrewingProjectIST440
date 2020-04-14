# Project: Brewing Automation System - Capstone Project
# Purpose Details: Kegging - KeggingTask Class
# Course: IST 440W - 001
# Author: Aaleem
# Date Developed: 4/4/2020
# Last Date Changed: 4/14/2020
# Rev: 2
from pip._vendor.distlib.compat import raw_input


class KeggingTasks:
    def __init__(self, task_id, task_category, task_prerequisite, task_status, task_confirmation):
        self.task_id = task_id
        self.task_category = task_category
        self.task_prerequisite = task_prerequisite
        self.task_status = task_status
        self.task_confirmation = task_confirmation

    def Keggingtasksmain():
        """

        :return:
        """
        t1 = 'task 1'
        t2 = 'task 2'
        t3 = 'task 3'
        t4 = 'task 4'
        t5 = 'task 5'
        t6 = 'task 6'
        t7 = 'task 7'
        t8 = 'task 8'
        taskList = [t1, t2, t3, t4, t5, t6, t7, t8]

        length = len(taskList)
        i = 0
        j = 0
        k = 0

        while i < length:
            print("list of tasks:")
            print()
            for i in range < length:
                print(taskList[k] + " status: completed")
                k += 1

            for i in range > length:
                print(taskList[k] + " status: not completed")


            print()
            ans = raw_input("has " + taskList[i] + " been completed? Enter (y/n): ")
            if ans == 'y':
                i += 1
                j += 1
                k = 0
            else:
                k = 0
                continue

        print()
        print("all kegging tasks completed.")

    Keggingtasksmain()
