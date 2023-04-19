from HabitualTracker import heatmap, bar, line, parse, check_title, resort_weekdays, check_data
from pandas import read_csv
from pytest import raises

def test_heatmap(fakedata):
    with raises(KeyError):
        heatmap(fakedata)

def test_bar(fakedata):
    with raises(AttributeError):
        bar(fakedata)

def test_line(fakedata):
    with raises(AttributeError):
        line(fakedata)

def test_parse():
    assert parse("A.csv") == True
    assert parse("not a csv") == False
    with raises(TypeError):
        parse(18)
        parse(True)
        parse(0.01)

def test_check_title(fakedata, realdata):
    assert check_title(realdata) == False
    assert check_title(fakedata) == True
    with raises(TypeError):
        check_title(1)
        check_title(0.01)
        check_title("Nonsense")

def test_resort_weekdays():
    test_weekdays = [
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
    ]
    assert resort_weekdays(4) == test_weekdays
    with raises(TypeError):
        resort_weekdays("Sunday")
        resort_weekdays(0.01)

def test_check_data(fakedata, realdata):
    assert check_data(realdata) == False
    with raises(TypeError):
        check_data("Nonsense")
        check_data(18)
    with raises(KeyError):
        check_data(fakedata)

def main():

    fakedata = read_csv("test.csv")
    realdata = read_csv("data.csv")

    test_heatmap(fakedata)
    test_bar(fakedata)
    test_line(fakedata)
    test_parse()
    test_check_title(fakedata, realdata)
    test_resort_weekdays()
    test_check_data(fakedata,realdata)

if __name__ == "__main__":
    main()