from distance import Millimeter, Centimeter, Meter, Inch

conversion_err = 'Неверный результат конвертации'

def test_value_type():
    instance = Millimeter(Meter(13))
    assert isinstance(instance._value, float), 'Неверный тип атрибута _value'

def test_init_millimeter():
    instance = Millimeter(84.33)
    assert instance.as_millimeters() == 84.33, 'Неверное значение атрибута _value'

def test_convert_millimeters_to_meters():
    assert Meter(Millimeter(99.62)).as_millimeters() == 99.62, conversion_err

def test_convert_centimeters_to_meters():
    assert Meter(Centimeter(61.3)).as_millimeters() == 613, conversion_err

def test_convert_inches_to_meters():
    assert Meter(Inch(47.04)).as_millimeters() == 1194.816, conversion_err

def test_convert_millimeters_to_inches():
    assert Inch(Millimeter(26.91)).as_millimeters() == 26.91, conversion_err

def test_convert_centimeters_to_inches():
    assert Inch(Centimeter(14.27)).as_millimeters() == 142.7, conversion_err

def test_convert_meters_to_inches():
    assert Inch(Meter(20.58)).as_millimeters() == 20580, conversion_err