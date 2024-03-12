from enum import auto
from strenum import StrEnum


class Register:
    tasks = {}

    @classmethod
    def register_task(cls, task_name):
        def decorator(handler_class):
            if task_name in cls.tasks:
                raise ValueError(f"Task '{task_name}' is already registered.")
            cls.tasks[task_name] = handler_class()
            return handler_class

        return decorator

    def execute_task(self, task_name, *args, **kwargs):
        if not (task_name in self.tasks):
            raise ValueError(f"Task '{task_name}' is not registered.")
        instance = self.tasks[task_name]
        return instance.execute(*args, **kwargs)

    def run_task(self, task_name, *args, **kwargs):
        if not (task_name in self.tasks):
            raise ValueError(f"Task '{task_name}' is not registered.")
        instance = self.tasks[task_name]
        return instance.run(*args, **kwargs)


class TaskEnum(StrEnum):
    Task1 = auto()
    Task2 = auto()


class TaskRepository:
    def execute(self):
        raise NotImplementedError(
            f"{self.__class__.__name__} does not implement execute method."
        )

    def run(self):
        raise NotImplementedError(
            f"{self.__class__.__name__} does not implement run method."
        )


# Decorator to register tasks
@Register.register_task(TaskEnum.Task1)
class TaskHandler1(TaskRepository):
    def execute(self):
        print("Task 1 is executed.")

    def run(self):
        print("Task 1 is running...")
        return True


@Register.register_task(TaskEnum.Task2)
class TaskHandler2(TaskRepository):
    def execute(self, param):
        print(f"Task 2 is executed with parameter: {param}")

    def run(self):
        print("Task 2 is running...")
        return True


def main():
    task_register = Register()
    # Execute tasks
    task_register.execute_task(TaskEnum.Task1)
    task_register.execute_task(TaskEnum.Task2, "some_parameter")

    msg = task_register.run_task(TaskEnum.Task1)
    print(msg)
    task_register.run_task(TaskEnum.Task2)


if __name__ == "__main__":
    main()
