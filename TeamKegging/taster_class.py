# Project: Brewing Project
# Purpose Details: Taster Class
# Course: IST 440W
# Author: Team Kegging - Jun Baek
# Date Developed: 4/5/2020
# Last Date Changed: 4/15/2020
# Rev: 1.1


class TasterClass:  #Taster Class
    def __init__(self, tc_id, tc_name, tc_role):
        self.tc_id = tc_id
        self.tc_name = tc_name
        self.tc_role = tc_role

    def get_status(self):
        return "Taster_ID: {}\n" \
               "Taster_Name: {}\n" \
               "Taster_Role: {}\n".format(self.tc_id, self.tc_name, self.tc_role)

    def tasterclassmain():  # taster recording start

        """
        kegging task list
        :param: task completion (y/n)
        :return: list of tasks (completed and not completed)
        """

        # list of tasks
        # first task is to record beer quality
        # second task is to record beer taste
        # third task is to record beer ABV (alcohol by volume)

        t1 = 'task 1'
        t2 = 'task 2'
        t3 = 'task 3'


        # adding tasks to list
        taskList = [t1, t2, t3]
        timeStampList = []

        # declaring counters and defining length of task list
        length = len(taskList)
        taskCounter = 0
        taskStatusCounter = 0
        taskStatus = 0
        currentTimeStamp = 0

        # main loop for kegging tasks until completion
        while taskCounter < length:

            # prints completed / not completed based off counter
            print("list of tasks:")
            print()
            for taskStatus in range(1, taskCounter + 1):
                print(taskList[taskStatusCounter] + " status: completed at " + timeStampList[taskStatusCounter])
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
                currentTimeStamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
                timeStampList.append(currentTimeStamp)
            else:
                continue

        # exit of while loop / all tasks completed
        print()
        print("all taster tasks completed.")

    tasterclassmain()

testTaster = TasterClass(12, "Jun Baek", "Quality Assurance 1")

print(testTaster.get_status())