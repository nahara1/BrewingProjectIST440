# Project: Brewing Automation System - Capstone Project
# Purpose Details: Kegging - KeggingTask Class
# Course: IST 440W - 001
# Author: Aaleem Siddiqui
# Date Developed: 4/4/2020
# Last Date Changed: 4/14/2020
# Rev: 3
from pip._vendor.distlib.compat import raw_input


class KeggingTasks:
    def __init__(self, task_id, task_category, task_prerequisite, task_status, task_confirmation):
        self.task_id = task_id
        self.task_category = task_category
        self.task_prerequisite = task_prerequisite
        self.task_status = task_status
        self.task_confirmation = task_confirmation

    def Keggingtasksmain():  # kegging task start

        # list of tasks
        t1 = 'task 1'
        t2 = 'task 2'
        t3 = 'task 3'
        t4 = 'task 4'
        t5 = 'task 5'
        t6 = 'task 6'
        t7 = 'task 7'
        t8 = 'task 8'

        # adding tasks to list
        taskList = [t1, t2, t3, t4, t5, t6, t7, t8]

        # declaring counters and defining length of task list
        length = len(taskList)
        taskCounter = 0
        taskStatusCounter = 0
        taskStatus = 0

        # main loop for kegging tasks until completion
        while taskCounter < length:

            # prints completed / not completed based off counter (tasks must go in order)
            print("list of tasks:")
            print()
            for taskStatus in range(1, taskCounter + 1):
                print(taskList[taskStatusCounter] + " status: completed")
                taskStatusCounter += 1

            for taskStatus in range(taskCounter + 1, length + 1):
                print(taskList[taskStatusCounter] + " status: not completed")
                taskStatusCounter += 1

            # resets task status counter
            taskStatusCounter = 0
            print()

            # prints current task and asks if complete
            print("current task: " + taskList[taskCounter])
            ans = raw_input("has this been completed? Enter (y/n): ")
            if ans == 'y':
                taskCounter += 1
            else:
                continue

        # exit of while loop / all tasks completed
        print()
        print("all kegging tasks completed.")

    Keggingtasksmain()
