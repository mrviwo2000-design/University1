import pytest
from script import MathCalculator


class TestMathCalculator:
    """Тестирующий класс для MathCalculator"""

    @pytest.fixture
    def calculator(self):
        """Фикстура для создания экземпляра калькулятора"""
        return MathCalculator()

    # Группа: basic_operations
    @pytest.mark.basic_operations
    def test_add(self, calculator):
        """Тест сложения"""
        assert calculator.add(2, 3) == 5
        assert calculator.add(-1, 1) == 0
        assert calculator.add(0, 0) == 0

    @pytest.mark.basic_operations
    def test_subtract(self, calculator):
        """Тест вычитания"""
        assert calculator.subtract(5, 3) == 2
        assert calculator.subtract(0, 5) == -5
        assert calculator.subtract(-1, -1) == 0

    @pytest.mark.basic_operations
    def test_multiply(self, calculator):
        """Тест умножения"""
        assert calculator.multiply(4, 3) == 12
        assert calculator.multiply(0, 5) == 0
        assert calculator.multiply(-2, 3) == -6

    @pytest.mark.basic_operations
    @pytest.mark.parametrize("a, b, expected", [
        (10, 2, 5),
        (1, 4, 0.25),
        (-6, 3, -2),
        (0, 5, 0),
    ])
    def test_divide_parametrized(self, calculator, a, b, expected):
        """Параметризованный тест деления"""
        assert calculator.divide(a, b) == expected

    # Группа: advanced_operations
    @pytest.mark.advanced_operations
    def test_power(self, calculator):
        """Тест возведения в степень"""
        assert calculator.power(2, 3) == 8
        assert calculator.power(5, 0) == 1
        assert calculator.power(4, 0.5) == 2

    @pytest.mark.advanced_operations
    @pytest.mark.parametrize("n, expected", [
        (0, 1),
        (1, 1),
        (5, 120),
        (7, 5040),
    ])
    def test_factorial_parametrized(self, calculator, n, expected):
        """Параметризованный тест факториала"""
        assert calculator.factorial(n) == expected

    # Группа: number_theory
    @pytest.mark.number_theory
    def test_is_prime(self, calculator):
        """Тест проверки простых чисел"""
        assert calculator.is_prime(2) == True
        assert calculator.is_prime(17) == True
        assert calculator.is_prime(4) == False
        assert calculator.is_prime(1) == False
        assert calculator.is_prime(0) == False

    @pytest.mark.number_theory
    def test_fibonacci(self, calculator):
        """Тест чисел Фибоначчи"""
        assert calculator.fibonacci(0) == 0
        assert calculator.fibonacci(1) == 1
        assert calculator.fibonacci(5) == 5
        assert calculator.fibonacci(10) == 55

    # Группа: exception_tests
    @pytest.mark.exception_tests
    def test_divide_by_zero(self, calculator):
        """Тест исключения при делении на ноль"""
        with pytest.raises(ValueError, match="Деление на ноль невозможно"):
            calculator.divide(5, 0)

    @pytest.mark.exception_tests
    def test_factorial_negative(self, calculator):
        """Тест исключения при факториале отрицательного числа"""
        with pytest.raises(ValueError, match="Факториал отрицательного числа не определен"):
            calculator.factorial(-5)

    @pytest.mark.exception_tests
    def test_power_zero_negative(self, calculator):
        """Тест исключения при возведении нуля в отрицательную степень"""
        with pytest.raises(ValueError, match="Ноль в отрицательной степени не определен"):
            calculator.power(0, -2)

    @pytest.mark.exception_tests
    def test_fibonacci_negative(self, calculator):
        """Тест исключения при отрицательном индексе Фибоначчи"""
        with pytest.raises(ValueError, match="Число Фибоначчи для отрицательного индекса не определено"):
            calculator.fibonacci(-1)


class TestMathCalculatorPrecision:
    """Тесты для проверки точности вычислений с плавающей точкой"""

    @pytest.fixture
    def calculator(self):
        return MathCalculator()

    @pytest.mark.precision
    def test_float_addition_precision(self, calculator):
        """Тест точности сложения дробных чисел"""
        result = calculator.add(0.1, 0.2)
        expected = 0.3
        assert result == pytest.approx(expected)

    @pytest.mark.precision
    def test_float_multiplication_precision(self, calculator):
        """Тест точности умножения дробных чисел"""
        result = calculator.multiply(0.1, 0.1)
        expected = 0.01
        assert result == pytest.approx(expected)

    @pytest.mark.precision
    def test_float_division_precision(self, calculator):
        """Тест точности деления дробных чисел"""
        result = calculator.divide(1.0, 3.0)
        expected = 1.0 / 3.0
        assert result == pytest.approx(expected)

    @pytest.mark.precision
    @pytest.mark.parametrize("a, b, expected", [
        (0.1, 0.2, 0.3),
        (0.2, 0.3, 0.5),
        (1.5, 2.5, 4.0),
    ])
    def test_float_addition_parametrized(self, calculator, a, b, expected):
        """Параметризованный тест сложения с плавающей точкой"""
        result = calculator.add(a, b)
        assert result == pytest.approx(expected)

    @pytest.mark.precision
    @pytest.mark.parametrize("a, b, expected", [
        (0.1, 0.1, 0.01),
        (0.2, 0.3, 0.06),
        (1.5, 2.5, 3.75),
    ])
    def test_float_multiplication_parametrized(self, calculator, a, b, expected):
        """Параметризованный тест умножения с плавающей точкой"""
        result = calculator.multiply(a, b)
        assert result == pytest.approx(expected)


class TestMathCalculatorBoundaries:
    """Тесты для проверки граничных значений"""

    @pytest.fixture
    def calculator(self):
        return MathCalculator()

    @pytest.mark.boundary
    def test_large_numbers(self, calculator):
        """Тест работы с большими числами"""
        large_num = 1e15
        assert calculator.add(large_num, large_num) == 2e15
        assert calculator.multiply(large_num, 2) == 2e15

    @pytest.mark.boundary
    def test_small_numbers(self, calculator):
        """Тест работы с очень маленькими числами"""
        small_num = 1e-15
        result = calculator.multiply(small_num, small_num)
        assert result == pytest.approx(1e-30)

    @pytest.mark.boundary
    def test_zero_operations(self, calculator):
        """Тест операций с нулем"""
        assert calculator.add(0, 5) == 5
        assert calculator.multiply(0, 5) == 0
        assert calculator.power(5, 0) == 1


class TestMathCalculatorEdgeCases:
    """Тесты для проверки особых случаев"""

    @pytest.fixture
    def calculator(self):
        return MathCalculator()

    @pytest.mark.edge_cases
    def test_prime_edge_cases(self, calculator):
        """Тест граничных случаев для простых чисел"""
        assert calculator.is_prime(2) == True
        assert calculator.is_prime(97) == True
        assert calculator.is_prime(100) == False

    @pytest.mark.edge_cases
    def test_fibonacci_edge_cases(self, calculator):
        """Тест граничных случаев для чисел Фибоначчи"""
        assert calculator.fibonacci(0) == 0
        assert calculator.fibonacci(1) == 1
        assert calculator.fibonacci(20) == 6765

    @pytest.mark.edge_cases
    def test_factorial_edge_cases(self, calculator):
        """Тест граничных случаев для факториала"""
        assert calculator.factorial(0) == 1
        assert calculator.factorial(1) == 1
        assert calculator.factorial(10) == 3628800
