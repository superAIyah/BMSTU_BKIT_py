from aiogram.utils.helper import Helper, HelperMode, ListItem

# класс с состояниями
class TestStates(Helper):
    mode = HelperMode.snake_case

    TEST_STATE_1 = ListItem()
    TEST_STATE_2 = ListItem()
    TEST_STATE_3 = ListItem()

if __name__ == '__main__':
    print(TestStates.all())