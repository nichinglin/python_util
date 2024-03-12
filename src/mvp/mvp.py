import tkinter as tk


class View(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MVP Example")
        self.geometry("200x100")

        self.label = tk.Label(self, text="Value:")
        self.label.pack()

        self.button = tk.Button(self, text="Increase", command=self.on_increase)
        self.button.pack()

    def set_value(self, value):
        self.label.config(text=f"Value: {value}")

    def on_increase(self):
        self.presenter.increase_value()


class Model:
    def __init__(self):
        self._value = 0

    @property
    def value(self):
        return self._value

    def set_value(self, value):
        self._value = value


class Presenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.presenter = self  # Set the presenter reference in the view

    def increase_value(self):
        new_value = self.model.value + 1
        self.model.set_value(new_value)
        self.view.set_value(new_value)


def main():
    model = Model()
    view = View()
    presenter = Presenter(model, view)
    view.mainloop()


if __name__ == "__main__":
    main()
