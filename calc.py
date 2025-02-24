from .. import loader, utils
import math

@loader.tds
class CalculatorMod(loader.Module):
    """Калькулятор с поддержкой математических операций и функций."""
    strings = {
        "name": "Calculator",
        "usage": "Используйте: .calc <выражение>",
        "result": "Результат: {}",
        "description": (
            "📚 **Доступные операции и функции:**\n\n"
            "➕ **Основные операции:**\n"
            "- Сложение (`+`)\n"
            "- Вычитание (`-`)\n"
            "- Умножение (`*`)\n"
            "- Деление (`/`)\n"
            "- Целочисленное деление (`//`)\n"
            "- Остаток от деления (`%`)\n"
            "- Возведение в степень (`**`)\n\n"
            "📐 **Математические функции:**\n"
            "- `sin(x)` — синус угла в радианах\n"
            "- `cos(x)` — косинус угла в радианах\n"
            "- `tan(x)` — тангенс угла в радианах\n"
            "- `sqrt(x)` — квадратный корень\n"
            "- `log(x)` — натуральный логарифм\n"
            "- `log10(x)` — десятичный логарифм\n"
            "- `exp(x)` — экспонента (e^x)\n"
            "- `radians(x)` — преобразует градусы в радианы\n"
            "- `degrees(x)` — преобразует радианы в градусы\n"
            "- `ceil(x)` — округление вверх\n"
            "- `floor(x)` — округление вниз\n"
            "- `factorial(x)` — факториал числа\n"
            "- `gcd(x, y)` — наибольший общий делитель\n"
            "- `pow(x, y)` — возведение в степень (x^y)\n"
            "- `abs(x)` — модуль числа\n"
            "- `round(x, n)` — округление числа `x` до `n` знаков после запятой\n\n"
            "🔢 **Константы:**\n"
            "- `pi` — число π (3.14159...)\n"
            "- `e` — число Эйлера (2.71828...)\n\n"
          
        )
    }

    def __init__(self):
        self.name = self.strings["name"]

    @loader.command(ru_doc="Вычислить математическое выражение")
    async def calccmd(self, message):
        args = utils.get_args_raw(message)
        if not args:
            await message.edit(self.strings["usage"])
            return

        try:
            result = eval(args, {"__builtins__": None}, {
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "sqrt": math.sqrt,
                "log": math.log,
                "log10": math.log10,
                "exp": math.exp,
                "radians": math.radians,
                "degrees": math.degrees,
                "pi": math.pi,
                "e": math.e,
                "ceil": math.ceil,
                "floor": math.floor,
                "factorial": math.factorial,
                "gcd": math.gcd,
                "pow": math.pow,
                "abs": abs,
                "round": round,
            })
            await message.edit(self.strings["result"].format(result))
        except Exception as e:
            await message.edit(f"Ошибка: {e}")
