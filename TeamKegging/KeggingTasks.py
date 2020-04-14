# Project: Brewing Automation System - Capstone Project
# Purpose Details: Kegging - KeggingTask Class
# Course: IST 440W - 001
# Author: Ronald Salguero
# Date Developed: 4/4/2020
# Last Date Changed:
# Rev: 1

class KeggingTasks:
    def __init__(self, task_id, task_category, task_prerequisite, task_status, task_confirmation):
        self.task_id = task_id
        self.task_category = task_category
        self.task_prerequisite = task_prerequisite
        self.task_status = task_status
        self.task_confirmation = task_confirmation

    def main():
        t1 = 'task1'
        t2 = 'task2'
        t3 = 'task3'
        t4 = 'task4'
        t5 = 'task5'
        list = [t1, t2, t3, t4, t5]

        length = len(list)
        i = 0

        while i < length:
            print(list[i])
            i += 1

    main()