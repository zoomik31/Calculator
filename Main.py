import kivy.uix.button
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Calculator(App):

    def build(self):

        self.count_4, self.count_3, self.count_2, self.count_1 = 0, 0, 0, 0
        self.degree = 4

        degree_choise = BoxLayout(orientation='horizontal')
        all_box = BoxLayout(orientation='horizontal')
        summ_degree = BoxLayout(orientation='vertical')
        cell = BoxLayout(orientation='vertical')

        btn_up = Button(text='up', on_press=self.degree_up)
        self.text_degree = Label(text=str(self.degree), font_size=30)
        summ = TextInput(font_size=15, multiline = False)
        btn_down = Button(text="down", on_press=self.degree_down)
        btn_reset = Button(text="reset", on_press=self.reset)

        cell_4name = Label(text="4", font_size=30)
        self.cell_4inp = TextInput(text='0', font_size=50, multiline = False, disabled= False, on_text_validate=self.on_enter)
        cell_3name = Label(text="3", font_size=30)
        self.cell_3inp = TextInput(text='0', font_size=50, multiline = False, disabled= False, on_text_validate=self.on_enter)
        cell_2name = Label(text="2", font_size=30)
        self.cell_2inp = TextInput(text='0', font_size=50, multiline = False, on_text_validate=self.on_enter)
        cell_1name = Label(text="1", font_size=30)
        self.cell_1inp = TextInput(text='0', font_size=50, multiline = False, on_text_validate=self.on_enter)

        degree_choise.add_widget(btn_down)
        summ_degree.add_widget(self.text_degree)
        summ_degree.add_widget(summ)
        summ_degree.add_widget(btn_reset)
        degree_choise.add_widget(summ_degree)
        degree_choise.add_widget((btn_up))

        cell4 = BoxLayout(orientation='horizontal')
        cell3 = BoxLayout(orientation='horizontal')
        cell2 = BoxLayout(orientation='horizontal')
        cell1 = BoxLayout(orientation='horizontal')

        cell4.add_widget(cell_4name)
        cell4.add_widget(self.cell_4inp)
        cell3.add_widget(cell_3name)
        cell3.add_widget(self.cell_3inp)
        cell2.add_widget(cell_2name)
        cell2.add_widget(self.cell_2inp)
        cell1.add_widget(cell_1name)
        cell1.add_widget(self.cell_1inp)
        cell.add_widget(cell4)
        cell.add_widget(cell3)
        cell.add_widget(cell2)
        cell.add_widget(cell1)

        all_box.add_widget(cell)
        all_box.add_widget(degree_choise)

        return all_box

    def on_enter(instance, value):
        if instance.degree == 4:
            if value == instance.cell_4inp:
                instance.count_4 += int(instance.cell_4inp.text)
                print(instance.count_4, instance.cell_4inp.text)
                instance.cell_4inp.text = str(instance.count_4)

            elif value == instance.cell_3inp:
                instance.count_3 += int(instance.cell_3inp.text)
                print(instance.count_3, instance.cell_3inp.text)
                instance.cell_3inp.text = str(instance.count_3)
                if instance.count_3 >= 3:
                    instance.count_4 += instance.count_3 // 3
                    instance.count_3 %= 3
                    instance.cell_3inp.text = str(instance.count_3)
                    instance.cell_4inp.text = str(instance.count_4)

            elif value == instance.cell_2inp:
                instance.count_2 += int(instance.cell_2inp.text)
                print(instance.count_2, instance.cell_2inp.text)
                instance.cell_2inp.text = str(instance.count_2)
                if instance.count_2 >= 3:
                    instance.count_3 += instance.count_2 // 3
                    instance.count_2 %= 3
                    instance.cell_2inp.text = str(instance.count_2)
                    instance.cell_3inp.text = str(instance.count_3)
                    if instance.count_3 >= 3:
                        instance.count_4 += instance.count_3 // 3
                        instance.count_3 %= 3
                        instance.cell_3inp.text = str(instance.count_3)
                        instance.cell_4inp.text = str(instance.count_4)

            elif value == instance.cell_1inp:
                instance.count_1 += int(instance.cell_1inp.text)
                print(instance.count_1, instance.cell_1inp.text)
                instance.cell_1inp.text = str(instance.count_1)

                if instance.count_1 >= 3:
                    instance.count_2 += instance.count_1 // 3
                    instance.count_1 %= 3
                    instance.cell_1inp.text = str(instance.count_1)
                    instance.cell_2inp.text = str(instance.count_2)
                    if instance.count_2 >= 3:
                        instance.count_3 += instance.count_2 // 3
                        instance.count_2 %= 3
                        instance.cell_2inp.text = str(instance.count_2)
                        instance.cell_3inp.text = str(instance.count_3)
                        if instance.count_3 >= 3:
                            instance.count_4 += instance.count_3 // 3
                            instance.count_3 %= 3
                            instance.cell_3inp.text = str(instance.count_3)
                            instance.cell_4inp.text = str(instance.count_4)
        if instance.degree == 3:
            if value == instance.cell_3inp:
                instance.count_3 += int(instance.cell_3inp.text)
                print(instance.count_3, instance.cell_3inp.text)
                instance.cell_3inp.text = str(instance.count_3)
            elif value == instance.cell_2inp:
                instance.count_2 += int(instance.cell_2inp.text)
                print(instance.count_2, instance.cell_2inp.text)
                instance.cell_2inp.text = str(instance.count_2)
                if instance.count_2 >= 3:
                    instance.count_3 += instance.count_2 // 3
                    instance.count_2 %= 3
                    instance.cell_2inp.text = str(instance.count_2)
                    instance.cell_3inp.text = str(instance.count_3)
            elif value == instance.cell_1inp:
                instance.count_1 += int(instance.cell_1inp.text)
                print(instance.count_1, instance.cell_1inp.text)
                instance.cell_1inp.text = str(instance.count_1)

                if instance.count_1 >= 3:
                    instance.count_2 += instance.count_1 // 3
                    instance.count_1 %= 3
                    instance.cell_1inp.text = str(instance.count_1)
                    instance.cell_2inp.text = str(instance.count_2)
                    if instance.count_2 >= 3:
                        instance.count_3 += instance.count_2 // 3
                        instance.count_2 %= 3
                        instance.cell_2inp.text = str(instance.count_2)
                        instance.cell_3inp.text = str(instance.count_3)


        if instance.degree == 2:
            if value == instance.cell_2inp:
                instance.count_2 += int(instance.cell_2inp.text)
                print(instance.count_2, instance.cell_2inp.text)
                instance.cell_2inp.text = str(instance.count_2)
            elif value == instance.cell_1inp:
                instance.count_1 += int(instance.cell_1inp.text)
                print(instance.count_1, instance.cell_1inp.text)
                instance.cell_1inp.text = str(instance.count_1)

                if instance.count_1 >= 3:
                    instance.count_2 += instance.count_1 // 3
                    instance.count_1 %= 3
                    instance.cell_1inp.text = str(instance.count_1)
                    instance.cell_2inp.text = str(instance.count_2)


    def reset(instance, value):
        instance.count_1, instance.count_2, instance.count_3, instance.count_4 = 0, 0, 0, 0
        instance.cell_1inp.text, instance.cell_2inp.text, instance.cell_3inp.text, instance.cell_4inp.text = str(instance.count_1), str(instance.count_2), str(instance.count_3), str(instance.count_4)

    def degree_up(instance, value):

        if instance.degree == 4:
            instance.degree = 2
            instance.reset(value)
            instance.text_degree.text = str(instance.degree)
        elif instance.degree < 4:
            instance.degree += 1
            instance.text_degree.text = str(instance.degree)
            instance.reset(value)

        if instance.degree == 4:
            instance.cell_4inp.disabled = False
            instance.cell_3inp.disabled = False
        elif instance.degree == 3:
            instance.cell_4inp.disabled = True
            instance.cell_3inp.disabled = False
        elif instance.degree == 2:
            instance.cell_4inp.disabled = True
            instance.cell_3inp.disabled = True

    def degree_down(instance, value):

        if instance.degree == 2:
            instance.degree = 4
            instance.text_degree.text = str(instance.degree)
            instance.reset(value)

        elif instance.degree > 2:
            instance.degree -= 1
            instance.text_degree.text = str(instance.degree)
            instance.reset(value)

        if instance.degree == 4:
            instance.cell_4inp.disabled = False
            instance.cell_3inp.disabled = False
        elif instance.degree == 3:
            instance.cell_4inp.disabled = True
            instance.cell_3inp.disabled = False
        elif instance.degree == 2:
            instance.cell_4inp.disabled = True
            instance.cell_3inp.disabled = True

if __name__ == "__main__":
    Calculator().run()