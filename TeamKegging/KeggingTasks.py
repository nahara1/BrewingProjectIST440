# Project: Brewing Automation System - Capstone Project
# Purpose Details: Kegging - KeggingTask Class
# Course: IST 440W - 001
# Author: Aaleem Siddiqui
# Date Developed: 4/4/2020
# Last Date Changed: 4/15/2020
# Rev: 6
from pip._vendor.distlib.compat import raw_input

import datetime


class KeggingTasks:
    def __init__(self, task_id, task_category, task_prerequisite, task_status, task_confirmation):
        self.task_status = task_status
        self.task_id = task_id
        self.task_category = task_category
        self.task_prerequisite = task_prerequisite
        self.task_confirmation = task_confirmation

    def Keggingtasksmain(self):  # kegging task start
        """
        kegging task list
        :param: task completion (y/n)
        :return: list of tasks (completed and not completed)
        """

        # list of tasks
        t1 = '1. Cleanse and sanitization of equipment'
        t2 = '2. Leak test for gas side of keg system'
        t3 = '3. Transfer beer to keg and seal keg'


        # declaring list, time stamp list, dummy RFID employee list
        taskList = [t1, t2, t3]
        timeStampList = []
        RFIDLinkToTask = []
        employeeRFID = ['1111', '2222', '3333', '4444']

        # declaring counters and defining length of task list
        length = len(taskList)
        taskCounter = 0
        taskStatusCounter = 0
        taskStatus = 0
        currentTimeStamp = 0

        # main loop for kegging tasks until completion
        while taskCounter < length:

            # prints completed / not completed based off counter (tasks must go in order)
            print("list of tasks:")
            print()
            for taskStatus in range(1, taskCounter + 1):
                print(taskList[taskStatusCounter] + " status: completed at " + timeStampList[taskStatusCounter] + " by RFID#" + RFIDLinkToTask[taskStatusCounter])
                taskStatusCounter += 1

            for taskStatus in range(taskCounter + 1, length + 1):
                print(taskList[taskStatusCounter] + " status: not completed")
                taskStatusCounter += 1

            # resets task status counter
            taskStatusCounter = 0
            print()

            # prints current task and asks if complete
            print("Current task: " + taskList[taskCounter])
            print()
            ans = raw_input("Has this been completed? Enter (y/n): ")
            if ans == 'y':
                while True:  # validation of RFID loop
                    taskRFID = raw_input("Please enter your RFID number: ")
                    if taskRFID in employeeRFID:  # checks to see if RFID is in list
                        taskCounter += 1
                        self.task_status = "{0:.1%}".format(taskCounter/length)  # percentage of task completion
                        print()
                        print("Current kegging tasks status: " + str(self.task_status))
                        currentTimeStamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())  # retrieves current timestamp
                        timeStampList.append(currentTimeStamp)  # adds current timestamp to list
                        RFIDLinkToTask.append(taskRFID)  # adds RFID to completed task
                        break
                    else:
                        print("Authentication Error")
            else:
                continue
            print()
            print("----------------------------------------------------")
            print()
        # exit of while loop / all tasks completed
        print()
        print("all kegging tasks completed.")

kt1 = KeggingTasks(1,'cellarman tasks','none','placeholder','yes')
kt1.Keggingtasksmain()