# Project: Brewing Automation System - Capstone Project
# Purpose Details: Kegging - KeggingTask Class
# Course: IST 440W - 001
# Author: Aaleem Siddiqui
# Date Developed: 4/4/2020
# Last Date Changed: 4/18/2020
# Rev: 9
from pip._vendor.distlib.compat import raw_input

import datetime

loglist = []


class KeggingTasks:
    def __init__(self, task_id, task_category, task_prerequisite, task_status, task_confirmation):
        self.task_status = task_status
        self.task_id = task_id
        self.task_category = task_category
        self.task_prerequisite = task_prerequisite
        self.task_confirmation = task_confirmation

    def keg_log(self, batch_id, bb_stage, log_message):
        currentTimeStamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        status_log = "{\"batch_id\":\"" + str(batch_id) + "\", \"brew_batch_stage\":\"" + str(bb_stage) + "\", \"log\":\"" + currentTimeStamp + " " + str(log_message) + "\"}"
        # ServiceNowLog.ServiceNowLog.create_new_log(ServiceNowLog, status_log)
        # print(status_log)
        loglist.append(status_log)

    def Keggingtasksmain(self):  # kegging task start
        """
        kegging task list
        :param: task completion (y/n)
        :return: list of tasks (completed and not completed)
        """

        #  batch ID confirmation loop
        while True:
            self.keg_log(1, "kegging", "Starting Cellarman tasks")  # logging to service now
            batch_id = raw_input("Please enter the batch ID: ")  # user input for batch ID
            confirm_batch_id = raw_input("Are you sure? Enter (y/n): ")
            if confirm_batch_id == 'y':
                self.keg_log(1, "kegging", "Batch ID entered as: " + batch_id)  # logging to service now
                break
            else:
                print("Confirmation failed. Please try again.")
                self.keg_log(1, "kegging", "Batch ID Confirmation Mismatch")  # logging to service now
                print()

        print()
        print("----------------------------------------------------")
        print()

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
                print(taskList[taskStatusCounter] + " status: completed at " + timeStampList[
                    taskStatusCounter] + " by RFID#" + RFIDLinkToTask[taskStatusCounter])
                taskStatusCounter += 1

            for taskStatus in range(taskCounter + 1, length + 1):
                print(taskList[taskStatusCounter] + " status: not completed")
                taskStatusCounter += 1

            # resets task status counter
            taskStatusCounter = 0
            print()

            # prints current task and asks if complete
            print("Current task: " + taskList[taskCounter])
            self.keg_log(1, "kegging", "Current task: " + taskList[taskCounter] + " INITIATED.")  # logging to service now
            print()
            ans = raw_input("Has this task been completed? Enter (y/n): ")
            if ans == 'y':
                while True:  # validation of RFID loop
                    taskRFID = raw_input("Please enter your RFID number: ")
                    if taskRFID in employeeRFID:  # checks to see if RFID is in list
                        print()
                        print("Current kegging tasks status: " + str(self.task_status))
                        self.keg_log(batch_id, "kegging", "Current task: " + taskList[taskCounter] + " COMPLETED.")  # logging to service now
                        currentTimeStamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())  # retrieves current timestamp
                        timeStampList.append(currentTimeStamp)  # adds current timestamp to list
                        RFIDLinkToTask.append(taskRFID)  # adds RFID to completed task
                        taskCounter += 1
                        self.task_status = "{0:.1%}".format(taskCounter / length)  # percentage of task completion
                        self.keg_log(batch_id, "Kegging", "Current kegging tasks status: " + str(self.task_status))  # logging to service now
                        break
                    else:
                        print("Authentication Error")
                        self.keg_log(1, "kegging", "RFID Mismatch")  # logging to service now
            else:
                continue
            print()
            print("----------------------------------------------------")
            print()
        # exit of while loop / all tasks completed
        print()
        print("All kegging tasks completed.")
        self.keg_log(batch_id, "Kegging", "All Cellarman tasks completed.")  # logging to service now


kt1 = KeggingTasks(1, 'cellarman tasks', 'none', 'placeholder', 'yes')
kt1.Keggingtasksmain()
print()

# prints log that gets sent to service now (for dev)
for n in loglist:
    print(n)
